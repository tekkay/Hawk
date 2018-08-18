import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if voice.name == 'brazil':
        engine.setProperty('voice', voice.id)

engine.say('Oi bom dia, como vai?')
engine.runAndWait()
