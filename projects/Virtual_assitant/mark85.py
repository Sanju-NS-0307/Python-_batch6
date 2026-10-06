#virtiual assistant 

#TTS-->gTTS(google text to speech)-->pip install gTTS
#playsound --> pip install playsound=1.2.2
'''
import gtts
from gtts import gTTS
import playsound
#now we will give a text to convert into audio
text=' telidu'
g=gTTS(text)
#save as audio file(.mp3)
g.save('audio.mp3')
playsound.playsound('audio.mp3')

#let us make virtual assistant

import string

import gtts
from gtts import gTTS
import playsound
import speech_recognition as sr
from time import ctime #it returns current time
import os
import uuid
import webbrowser


#first we will make our virtual assistant to understand what we speak
def listen():
    """Speech Recognition"""
    #we will make our system to check the microphone as source
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('hey there')
        audio=r.listen(source,phrase_time_limit=5)
    #what ever we speak lets store in data
    data=""
    #now we will give our exception handling here to avoid any errors
    try:
        data=r.recognize_google(audio,language="en-US")
        print("You said: "+data)
    except sr.UnknownValueError:
        print("make sure you speak louder,so it can be heard")
    except sr.RequestError as e:
        print("Request failed,please check your internet connection")
    return data
    #text=gTTS(data)
    #text.save('new.mp3')
    #playsound.playsound('new.mp3')
#listen() #needs to have pyaudio-->pip install pyaudio

#we will create separate functions for responding back and virtual assistant
#actions

def respond(String):
    """Responding function to get audio saved and text is spoken back"""

    print(String)

    # Create a unique filename
    filename = os.path.abspath("Speech%s.mp3" % str(uuid.uuid4()))

    # Convert text to speech
    tts = gTTS(text=String, lang="en")

    # Save audio
    tts.save(filename)

    
    

    # Play audio
    playsound.playsound(filename)

    # Delete audio after playing
    os.remove(filename)
#next we will make our virtual assistant to function

def va(data):
    """now we will map our conditions"""
    if "hello" in data:
        listening =True
        respond("hello there")
    elif "how are you" in data:
        respond("I am fine, what about you")
    elif "what time is it" in data:
        respond(ctime())
    elif "open Google" in data:
        listening=True
        url="https://www.google.com"
        webbrowser.open(url)
        print("Success")
        respond("opened google")
    elif "play my favourite song" in data:
        listening=True
        url="https://youtu.be/7zEqrXp83e0?si=bXrQlHVm3MilQdbr"
        webbrowser.open(url)
        print("Success")
        respond("opened youtube")
    elif "locate"in data:
        listening=True
        url="https://www.google.com/maps/search/"+data.split("locate")[-1]
        webbrowser.open(url)# returns the location of the place we want to locate
        print("Success")
        respond("opened maps")
    
    elif "time" in data:
        listening=True
        respond(ctime())# returns current time
    elif "stop talking" in data or "exit" in data:
            respond("ok,bhai")
            listening=False
    try:
        return listening
    except UnboundLocalError:
        print("mismatched,speak again")
respond("hi sanju")
listening=True
while listening:
    data=listen()
    listening=va(data)

#your task is make your virtual assistant
#play RPS game
#play number guessing game
#create a qr code
#open your desired file in your system
'''
# virtual assistant

# TTS --> gTTS
# pip install gTTS

# playsound
# pip install playsound==1.2.2

# speech recognition
# pip install SpeechRecognition
# pip install PyAudio

# QR code
# pip install PyQRCode
# pip install pypng


import gtts
from gtts import gTTS
import playsound
import speech_recognition as sr
from time import ctime
import os
import uuid
import webbrowser
import random
import pyqrcode
import png


# --------------------------------------------------
# SPEECH RECOGNITION
# --------------------------------------------------

def listen():
    """Speech Recognition"""

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("hey there")
        audio = r.listen(source, phrase_time_limit=5)

    data = ""

    try:
        data = r.recognize_google(audio, language="en-US")
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Make sure you speak louder, so it can be heard")

    except sr.RequestError:
        print("Request failed, please check your internet connection")

    return data.lower()


# --------------------------------------------------
# TEXT TO SPEECH
# --------------------------------------------------

def respond(String):
    """Responding function"""

    print(String)

    filename = os.path.abspath(
        "Speech%s.mp3" % str(uuid.uuid4())
    )

    tts = gTTS(text=String, lang="en")

    tts.save(filename)

    playsound.playsound(filename)

    os.remove(filename)


# --------------------------------------------------
# ROCK PAPER SCISSORS
# --------------------------------------------------

def rock_paper_scissors():

    respond("Let's play rock paper scissors")

    player = input(
        "Enter your choice: rock, paper or scissors: "
    ).lower()

    computer = random.choice(
        ["rock", "paper", "scissors"]
    )

    print("Computer chose:", computer)

    if player not in ["rock", "paper", "scissors"]:
        respond("Invalid choice")
        return

    if player == computer:

        respond("It's a tie")

    elif (
        player == "rock" and computer == "scissors"
        or
        player == "scissors" and computer == "paper"
        or
        player == "paper" and computer == "rock"
    ):

        respond("You win")

    else:

        respond("Computer wins")


# --------------------------------------------------
# NUMBER GUESSING GAME
# --------------------------------------------------

def number_guessing():

    respond("Let's play the number guessing game")

    number = random.randint(1, 10)

    print("I have selected a number between 1 and 10")

    while True:

        guess = int(input("Enter your guess: "))

        if guess == number:

            respond("Congratulations, you guessed the correct number")
            break

        elif guess < number:

            print("Try a higher number")
            respond("Try a higher number")

        else:

            print("Try a lower number")
            respond("Try a lower number")


# --------------------------------------------------
# CREATE QR CODE
# --------------------------------------------------

def create_qr():

    respond("Creating your QR code")

    link = "https://www.linkedin.com/in/ch-sanjay-kumar-b13b51376/"

    qr_code = pyqrcode.create(link)

    qr_code.png("qr_code.png", scale=10)

    respond("QR code has been created")

    print("QR code saved as qr_code.png")


# --------------------------------------------------
# OPEN FILE
# --------------------------------------------------

def open_file():

    file_path = input(
        "Enter the complete file path: "
    )

    if os.path.exists(file_path):

        os.startfile(file_path)

        respond("File opened successfully")

    else:

        respond("Sorry, the file does not exist")


# --------------------------------------------------
# VIRTUAL ASSISTANT
# --------------------------------------------------

def va(data):

    if "hello" in data:

        respond("Hello there")
        return True


    elif "how are you" in data:

        respond("I am fine, what about you")
        return True


    elif "what time is it" in data or "time" in data:

        respond(ctime())
        return True


    elif "open google" in data:

        url = "https://www.google.com"

        webbrowser.open(url)

        respond("Opened Google")
        return True


    elif "play my favourite song" in data:

        url = "https://youtu.be/7zEqrXp83e0?si=bXrQlHVm3MilQdbr"

        webbrowser.open(url)

        respond("Opened YouTube")
        return True


    elif "locate" in data:

        place = data.split("locate")[-1]

        url = "https://www.google.com/maps/search/" + place

        webbrowser.open(url)

        respond("Opened maps")
        return True


    # ----------------------------------------------
    # ROCK PAPER SCISSORS
    # ----------------------------------------------

    elif (
        "rock paper scissors" in data
        or "rps" in data
        or "play rps" in data
    ):

        rock_paper_scissors()
        return True


    # ----------------------------------------------
    # NUMBER GUESSING GAME
    # ----------------------------------------------

    elif (
        "number guessing" in data
        or "guessing game" in data
        or "guess number" in data
    ):

        number_guessing()
        return True


    # ----------------------------------------------
    # QR CODE
    # ----------------------------------------------

    elif (
        "create qr" in data
        or "generate qr" in data
        or "qr code" in data
    ):

        create_qr()
        return True


    # ----------------------------------------------
    # OPEN FILE
    # ----------------------------------------------

    elif (
        "open file" in data
        or "open my file" in data
    ):

        open_file()
        return True


    # ----------------------------------------------
    # EXIT
    # ----------------------------------------------

    elif (
        "stop talking" in data
        or "exit" in data
        or "quit" in data
    ):

        respond("Okay bhai")
        return False


    else:

        respond("Sorry, I did not understand")

        return True


# --------------------------------------------------
# START VIRTUAL ASSISTANT
# --------------------------------------------------

respond("Hi Sanju")

listening = True

while listening:

    data = listen()

    listening = va(data)
