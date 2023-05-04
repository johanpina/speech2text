# speech2text
This repo contains a development for medical audio transcription  and estructure or info extraction from transcription


## Installing
### configurate the environment
```
$ python -m venv .env
$ source .env/bin/activate  #On linux
$ sudo bash install.sh 
> .env/Scripts/activate     #On Windows 

```
### create a .envv file with API_KEY of openai chatgpt
```
OPENAI_API_KEY=yourAPIKEY

```

## Running Program

```
uvicorn main:app --reload
```
