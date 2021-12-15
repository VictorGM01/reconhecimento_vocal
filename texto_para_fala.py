from gtts import gTTS
from playsound import playsound


def texto_para_fala(texto: str, nome_arquivo: str):
    print('Conversão iniciada...')
    audio = gTTS(texto, lang='pt')
    audio.save(fr'audios\{nome_arquivo}.mp3')
    playsound(fr'audios\{nome_arquivo}.mp3')
