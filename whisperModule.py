import os
from openai import OpenAI
import time

# Configuración de la API de OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv(filename='.envv'))

client  = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def run_whisper_api(input_path: str):
    # Define la carpeta de salida y crea la subcarpeta 'textos'
    begin = time.time()
    output_dir = os.path.join("procesados", "textos")
    os.makedirs(output_dir, exist_ok=True)

    # Leer el archivo de audio y enviarlo a la API de Whisper de OpenAI
    with open(input_path, "rb") as audio_file:
        result = client.audio.transcriptions.create(model="whisper-1", file=audio_file,response_format="text")
        
    if result:
        # Guardar el texto de la transcripción
        document_path = os.path.join(output_dir, f"{os.path.basename(input_path).split('.')[0]}.txt")
        with open(document_path, "w") as document:
            document.write(result)
        print("Se guardó la transcripción en:", document_path)
    else:
        print("Error ejecutando la transcripción")
    
    total = time.time() - begin
    print("El tiempo de transcripción es:", total)
    return result