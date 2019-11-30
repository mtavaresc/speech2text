import os

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def listen_mic():
    # Allow the mic to listen the user
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = mic.listen(source)

    try:
        phrase = mic.recognize_google(audio, language='pt-BR')
        print(f"You said: {phrase}")
        return phrase
    except sr.UnknownValueError:
        print("I don't understand!")


def create_folder(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def create_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    create_folder(os.path.join(os.getcwd(), 'audios'))
    tts.save(os.path.join(os.getcwd(), 'audios', 'hello.mp3'))
    print("I'm learning what you said...")
    playsound(os.path.join(os.getcwd(), 'audios', 'hello.mp3'))


if __name__ == '__main__':
    quote = listen_mic()
    create_audio(quote)
