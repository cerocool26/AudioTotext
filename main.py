import  speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Di algo")
    audio = r.listen(source)
    try:
        texto = r.recognize_google(audio,language='es-Es')
        print("Esto es lo que has dicho : {}".format(texto))
        with open("audio.wav", "wb") as audio_file:
            audio_file.write(audio.get_wav_data())
    except:
        print("Lo siento no entendi")
