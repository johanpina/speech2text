from fastapi import FastAPI, UploadFile, File
from chatgpt import get_completion, promptMedico
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from whisperModule import process_audio_file, run_whisper_command
import schemas
import os 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")


@app.post("/api/prompt_medico")
async def process_text(text_data: schemas.TextData):
    print("entrando a la solicitud")
    prompt = promptMedico(text_data.texto)
    #print(prompt)
    response = get_completion(prompt)
    return {"response": response}

@app.post("/api/process_audio",response_model=schemas.TextData)
async def process_audio(uploaded_file: UploadFile = File(...)):
    # Guardar el archivo temporalmente en el disco
    input_file = f"temp_{uploaded_file.filename}"
    with open(input_file, "wb") as f:
        f.write(await uploaded_file.read())

    processed_file = None
    # Procesar el archivo de audio y eliminar el archivo temporal
    try:
        processed_file = process_audio_file(input_file)
    finally:
        os.remove(input_file)

    if not processed_file:
        raise HTMLResponse(status_code=400, content="Error procesando el audio")
    
    text_file = run_whisper_command(input_path = processed_file)
    
    return schemas.TextData(texto=text_file)