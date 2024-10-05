import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%P')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 4)
        info = wikipedia.search(person, 4)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('explain', '')
        talk('explaining' + thing)
        pywhatkit.search(thing)
        print(thing)
    elif 'lets go for date' in command:
        talk('sorry i have a headache' + 'but let me think about it')
    elif 'are you single' in command:
        talk('yes iam proud to be single')
    elif 'explain about' in command:
        detail = command.replace('explain', '')
        detail = wikipedia.search(detail, 5)
        pywhatkit.search(detail)
        print(detail)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('dont understand say again')


while True:
    run_alexa()