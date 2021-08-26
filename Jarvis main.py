import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup


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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_jaine():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what are you doing' in command:
        talk('I am just trying to obey you ')
    elif 'your day' in command:
        talk('It was awesome.Thanks for asking')
    elif 'hello' in command:
        talk('Hi How are you')
    elif 'fine' in command:
        talk('Oh thats very good')
    elif 'all good' in command:
        talk('yeah i am completely fine.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'temperature' in command:
        search = 'temperature in rampurhat'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = data.find('div',class_='BNeawe').text
        talk(f'current{search}is {temp}')
    elif 'thank you' in command:
        talk('Mention not.')
    elif 'send a message' in command:
        talk('your whatsapp message will be send in a while.')
        pywhatkit.sendwhatmsg('+917908172788', 'Hi..How are you?', 17, 26)










    else:
        talk('Please repeat it!I didnot get it.')





while True:
    run_jaine()