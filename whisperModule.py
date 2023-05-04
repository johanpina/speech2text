
import subprocess
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import whisper
import time
model = whisper.load_model("medium")


def process_audio_file(file_path: str, output_folder: str = "procesados"):
    # Crear el directorio de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Validar y transformar el archivo de audio
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension.lower() not in [".wav", ".mp3"]:
        raise ValueError("El archivo debe ser .wav o .mp3")

    audio_format = "wav"
    output_name = os.path.join(output_folder, os.path.basename(file_name) + ".wav")
    output_name = output_name.replace("(", "_").replace(")", "_").strip()
    # DEBUG print(file_path)
    if file_extension.lower() == ".mp3":
        sound = AudioSegment.from_mp3(file_path)
    else:
        sound = AudioSegment.from_wav(file_path)

    audio_chunks = split_on_silence(sound, min_silence_len=100, silence_thresh=-45, keep_silence=50)

    # Unir los fragmentos y guardar el archivo resultante
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk

    combined.export(output_name, format=audio_format)
    return output_name

## acá vamos a colocar las funciones de audios

def run_whisper_command(input_path: str, model_engine=model):
    # Define la carpeta de salida y crea la subcarpeta 'textos'
    begin = time.time()
    output_dir = os.path.join("procesados", "textos")
    os.makedirs(output_dir, exist_ok=True)

    result = model_engine.transcribe(input_path)

    if result:
        document = open(output_dir+'/'+input_path.split('/')[-1].split(".")[0]+'.txt','w')
        document.write(result["text"])
        document.close()
        #print("Se guardó la transcripción en: ",document)
    else:
        pass #print("Error ejecutando la transcripción")
    #print(result["text"])
    total = time.time() - begin

    print("El tiempo de whisper es: ", total)
    return result["text"]


