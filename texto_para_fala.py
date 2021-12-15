from gtts import gTTS
from playsound import playsound


def texto_para_fala(texto):
    print('Conversão iniciada...')
    audio = gTTS(texto, lang='pt')
    audio.save('audio_python.mp3')
    playsound('audio_python.mp3')
