import speech_recognition as sr


def voz_para_texto():
    rec = sr.Recognizer()  # responsável por reconhecer o que está sendo falado

    # Habilita o microfone do computador
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)  # Ajusta o reconhecedor de voz aos ruídos captados pelo microfone

        print('Pronto, você já pode falar: ')
        voz = rec.listen(mic)  # Capta o som

        try:
            # Realiza o reconhecimento vocal e transcreve o que foi dito
            texto = rec.recognize_google(voz, language='pt-BR')

            print(texto)

        except sr.UnknownValueError:
            print('Não foi possível entender o que foi dito... ')


voz_para_texto()
