from gtts import gTTS
from playsound import playsound


def texto_para_fala(texto: str):
    print('Conversão iniciada...')
    audio = gTTS(texto, lang='pt')
    audio.save(r'audios\audio_gerado.mp3')
    playsound(r'audios\audio_gerado.mp3')


# Chamada da função
texto_para_fala(texto='Este áudio foi gerado usando a linguagem de programação Python')
