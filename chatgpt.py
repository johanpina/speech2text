import os
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv(filename='.envv'))

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion(prompt: str, model:str="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0,
    response_format={"type": "json_object"}
    )
    return response.choices[0].message.content


def promptMedico(texto: str):
    text = f"""vamos a actuar como un analista médico, tu trabajo es tomar el texto entree triple comillas (''') y realizar los siguientes pasos para generar un informe resumen:
            los pasos son:
            -extraiga el nombre del paciente
            -resuma los hallazgos clínicos que se reportan en el texto
            -de una conclusion diagnostica presunta(el médico será el que decide al final)
            El formato de salida es:
            -nombre: aqui va el nombre
            -sintomas: dame una lista separada por comas de los síntomas
            -diagnostico: dame un resumen del examen que se le practica al paciente (maximo 20 palabras)
            -examen:infiere el tipo de examen que se le realiza a la paciente
            -hallazgos: dame un resumen de los hallazgos clínicos que se reportan en el texto
            -tratamiento: dame un resumen del tratamiento que se le da al paciente
            -pronostico: dame un resumen del pronostico del paciente
            -observaciones: dame un resumen de las observaciones que se le hacen al paciente
            '''{texto}'''
            el formato de salida debe ser JSON
            """
    return text
