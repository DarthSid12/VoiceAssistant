# Enter all of these pip installs in your command prompt running as administrator
from turtledemo.clock import setup

import pyttsx3  # pip install pyttsx3
import cv2  # pip install opencv-python
import reverse_geocoder as rg
import geocoder  # pip install geocoder
from PyLyrics import *
from currency_converter import CurrencyConverter  # pip install currency_converter
import speech_recognition as sr  # pip install speechRecognition
import datetime

CODE = {' ': '_',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from playsound import playsound  # pip install playsound
import nltk
from nltk.corpus import wordnet
from time import sleep
rp = 0
import math
import pyjokes  # pip install pyjokes
from selenium import webdriver  # pip install selenium
import re
from random import choice, random

iop = 0
import tkinter as Tkinter  # pip install tkinter
from random import *
from turtle import *  # pip install turtle
from freegames import floor, vector, line, path  # pip install freegames
import requests  # pip install requests
import json  # pip install json
import time
import random
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbrowser
import os  # pip install os
from os import *
import smtplib
import pi  # pip install pi
import PyDictionary

dictionary = PyDictionary.PyDictionary()
qu = 'h'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# set voices[' '].id to 0 for male voice and 1 for female
engine.setProperty('voice', voices[0].id)
ghjs = 0
hour = 34
minute = 90


# Code to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def bol(a):
    engine.say(a)


# Code to speak and print
def speaks(audio):
    print(audio)
    speak(audio)


# Code to take input using voice and checking if name is in it.Also checks alarm
def superListen(hour, minute):
    uisdd = 0
    while uisdd == 0:
        hjdn = datetime.datetime.today().strftime("%H")
        mrin = (datetime.datetime.today().strftime("%M"))
        if hour == hjdn and minute == mrin:
            speak('Beep beep. Alarm ringing. Beep Beep. Say stop to stop')
            jkd = listen('?')
            if 'stop' in jkd:
                hour = 34
                minute = 90
        sample_rate = 48000
        print("Listening")
        chunk_size = 2048
        r = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        for i, microphone_name in enumerate(mic_list):
            device_id = i
            break
        with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                           chunk_size=chunk_size) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                rp = 1

            except sr.UnknownValueError:
                print("Sorry sir. I was unable to understand you")
                text = "iur"
                rp = 2
        text = text.lower()
        # Change or add callnames heree
        if 'jarvis' in text:
            jill = text
            print('You said', jill)
            break
    return jill


def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " "
    return encodedSentence


# Code to take input using voice

def listen(drf4frf4fihfur):
    iop = 0
    uisdd = 0
    while uisdd == 0:
        sample_rate = 48000
        print("Listening")
        chunk_size = 2048
        r = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        for i, microphone_name in enumerate(mic_list):
            device_id = i
            break
        with sr.Microphone(device_index=device_id, sample_rate=sample_rate,
                           chunk_size=chunk_size) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                return text
                break
            except sr.UnknownValueError:
                print("Sorry sir. I was unable to understand you")
                iop = 1


# Code to wish user accorsing to the time
def location():
    x = str(geocoder.ip('me'))
    x = x.split()
    x = x[5]
    jr = re.findall('(.+),', x)
    result = jr[0]
    return result


# Code to wish user accorsing to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


# Using google API to find restaurants/hotels
def around(value):
    api_key = 'AIzaSyBZyAuVmGMBsddv0hMIa0CfqD2yhH2g2zc'

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    quest = value
    r = requests.get(url + 'query=' + quest +
                     '&key=' + api_key)
    x = r.json()
    y = x['results']
    return y


# Code to login into smtp server and send email. Please enter your own email id and password
def sendEmail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('siddharth1411agrawal@gmail.com', 'mischiefmanage')
    server.sendmail('siddharth1411agrawal@gmail.com', to, msg)
    server.close()


clear = lambda: os.system('cls')
if __name__ == "__main__":
    # This Function will clean any command before execution of this python file
    clear()
    wishMe()
    # Starting query based answers

while True:
    time.sleep(1)
    speak("How may I help you sir.")
    qu = superListen(hour, minute)
    query = qu.lower()
    # Code to print the first 3 lines of a particula topic
    if 'wikipedia' in query:
        speak('Please enter topic sir')
        topic = listen('?')
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    # Code to open the google browser
    elif "open" in query.lower() and 'google' in query:
        webbrowser.open("google.com")
    # Code to start word file. Change of path is necessary according to your own computer
    elif "open" in query.lower() and 'word' in query:
        speak("Opening Microsoft Word")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Word 2010')  # To get the path, Search word, open in file and instead of >> add\. Then\\(name of file)
    # Code to start excel. Change of path is necessary. Follow the above intsrtuctions
    elif "open" in query.lower() and 'excel' in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Excel 2010')
        # Code to start powerpoint. Same instructions as above 2
    elif "open" in query.lower() and 'powerpoint' in query:
        speak("Opening Microsoft PowerPoint")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft PowerPoint 2010')
        # to open anything in youtube
    elif 'youtube' in query.lower():
        g = listen('?')
        d = re.findall('.*youtube(.+)', g)
        try:
            ya = d[0]
        except:
            speak("What should I search")
            ya = listen("F")
        v = ya.split()
        word = ''
        for i in v:
            word = word + i + '+'
        x = word + ' '
        y = ('https://www.youtube.com/results?search_query=' + x)
        webbrowser.open(y, new=2)

    # These songs will work according to your computer. You need to enter the path for them to work. Else an error will come
    elif 'play' in query and 'intention' in query:
        playsound("D:\INTENTIONS.mp3")
    elif 'play' in query and 'beautiful people' in query:
        playsound("D:\BP.mp3")
    elif 'play' in query and 'dark side' in query:
        playsound("D:\DS.mp3")
    elif 'play' in query and 'alone part 2' in query:
        playsound("D:\Alone.mp3")
    elif 'play' in query and 'yummy' in query:
        playsound("D:\Yummy.mp3")
        # Searching on google directly
    elif 'google' in query:
        g = listen('?')

        d = re.findall('.*google(.+)', g)

        try:
            ya = d[0]
        except:
            speak('What should i search')
            ya = listen("k")
        v = ya.split()
        word = ''
        for i in v:
            word = word + i + '+'
        x = word + ' '
        y = (
                    'http://www.google.com/search?q=' + x + '&oq=' + x + '&aqs=chrome..69i57j0l7.2937j0j7&sourceid=chrome&ie=UTF-8')
        webbrowser.open(y, new=2)
    # Same code to search on google just different input in query
    elif 'search' in query:
        g = listen('?')

        d = re.findall('.*google(.+)', g)

        ya = d[0]
        v = ya.split()
        word = ''
        for i in v:
            word = word + i + '+'
        x = word + ' '
        y = (
                    'http://www.google.com/search?q=' + x + '&oq=' + x + '&aqs=chrome..69i57j0l7.2937j0j7&sourceid=chrome&ie=UTF-8')
    elif 'lyrics' in query:
        speak('Enter the artist')
        djf = listen("E")
        speak('Enter the song')
        kdf = listen('d')
        try:
            print(PyLyrics.getLyrics(djf, kdf))
            speak("Do you want me to sing this?")
            jdh = inout('k')
            if 'yes' in jdh:
                speak(PyLyrics.getLyrics(r'Taylor Swift', 'Blank Space'))
        except:
            speak('Song or singer not found')
    elif 'location' in query:
        x = location()
        speak(x)
        sp = 'You are at ' + x
        speaks(sp)
    elif 'convert' in query and 'morse code' in query:
        speak("ENter the text to be converted")
        message = listen("Ente")
        code = convertToMorseCode(message)
        speak("Here you go")
        print(code)
    # Finding the weather using API. Enter you own API key. Finds current location itself
    elif 'weather' in query:
        api_key = "4b91fd5f8223af49d9c2b39fd7883851"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        if "me" in query or 'my' in query:
            city_name = location()
        else:
            speak("Enter city name")
            city_name = listen("? ")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x['main']
            cur = y["temp"]
            current_temperature = (cur - 273.15) // 1
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature= " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidity) + "%" +
                  "\n description = " +
                  str(weather_description))
            speech = "The temperature is " + str(
                current_temperature) + " degree celsius. The atmospheric pressure is " + str(
                current_pressure) + " H P A and the humidity is " + str(
                current_humidity) + "% while the weather descrption is " + str(weather_description)
            speak(speech)
        else:
            print(" City Not Found ")
            # Code to convert any value of a country to some else. Structure of input should be:Convert 100 USD(ANy country's value or country name) to INR(Sam for this)
    elif "convert" in query:
        jirk = 0
        jirkr = 0
        c = CurrencyConverter()
        jasj = query.split()
        try:
            valu = jasj[1]
            value = int(valu)
            val = str(value)
        except:
            value = listen("Enter the value")
        try:
            country2 = jasj[4].upper()

        except:
            country2 = listen("Enter the country to convert to")
            jirk = 1
        try:
            country1 = jasj[2].upper()

        except:
            country1 = listen("Enter the country to convert from")
            jirkr = 1

        if jirkr == 1:
            jin = country1.lower()
            if jin == "usa":
                country1 = "USD"
            elif jin == "eur":
                country1 = "EUR"
            elif jin == "afghanistan":
                country1 = "AFN"
            elif jin == "albania":
                country1 = "ALL"
            elif jin == "algeria":
                country1 = "DZD"
            elif jin == "anguilla":
                country1 = "XCD"
            elif jin == "argentina":
                country1 = "ARS"
            elif jin == "armenia":
                country1 = "AMD"
            elif jin == "aruba":
                country1 = "AWG"
            elif jin == "australia":
                country1 = "AUD"
            elif jin == "azerbaijan":
                country1 = "AZN"
            elif jin == "bangladesh":
                country1 = "BDT"
            elif jin == "india":
                country1 = "INR"



            elif jin == "barbados":
                country1 = "BBD"
            elif jin == "belgium":
                country1 = "EUR"
            elif jin == "bhutan":
                country1 = "BTN"
            elif jin == "bolivia":
                country1 = "BOB"
            elif jin == "brazil":
                country1 = "BRL"
            elif jin == "britain":
                country1 = "USD"
            elif jin == "african republic":
                country1 = "XAF"
            elif jin == "australia":
                country1 = "AUD"
            elif jin == "colombia":
                country1 = "COP"



            elif jin == "canada":
                country1 = "CAD"
            elif jin == "denmark":
                country1 = "DKK"
            elif jin == "egypt":
                country1 = "EGP"
            elif jin == "france":
                country1 = "EUR"
            elif jin == "finland":
                country1 = "EUR"
            elif jin == "germany":
                country1 = "EUR"
            elif jin == "greenland":
                country1 = "DKK"
            elif jin == "hong kong":
                country1 = "HKD"
            elif jin == "hungary":
                country1 = "HUF"
            elif jin == "iceland":
                country1 = "ISK"
            elif jin == "indonesia":
                country1 = "IDR"
            elif jin == "iran":
                country1 = "IRR"
            elif jin == "iraq":
                country1 = "IQD"
            elif jin == "japan":
                country1 = "JPY"
            elif jin == "kenya":
                country1 = "KES"
            elif jin == "madagascar":
                country1 = "MGA"
            elif jin == "mexico":
                country1 = "MXN"
            elif jin == "mauritius":
                country1 = "MUR"
            elif jin == "nepal":
                country1 = "NPR"
            elif jin == "new zealand":
                country1 = "NZD"
            elif jin == "north korea":
                country1 = "KPW"
            elif jin == "norway":
                country1 = "NOK"
            elif jin == "pakistan":
                country1 = "PKR"
            elif jin == "russia":
                country1 = "RUB"
            elif jin == "saudi arabia":
                country1 = "SAR"
            elif jin == "singapore":
                country1 = "SGD"
            elif jin == "south africa":
                country1 = "ZAR"
            elif jin == "south korea":
                country1 = "KRW"
            elif jin == "sri lanka":
                country1 = "LKR"
            elif jin == "sweden":
                country1 = "SEK"
            elif jin == "switzerland":
                country1 = "CHF"
            elif jin == "taiwan":
                country1 = "TWD"
            elif jin == "thailand":
                country1 = "THB"
            elif jin == "united arab emirates":
                country1 = "AED"
            elif jin == "united kingdom":
                country1 = "GBP"
            elif jin == "vietnam":
                country1 = "VND"
            elif jin == "yemen":
                country1 = "YER"
            elif jin == "zimbabwe":
                country1 = "USD"

        if jirk == 1:
            ji = country2.lower()
            if ji == "usa":
                country2 = "USD"
            elif ji == "eur":
                country2 = "EUR"
            elif ji == "afghanistan":
                country2 = "AFN"
            elif ji == "albania":
                country2 = "ALL"
            elif ji == "algeria":
                country2 = "DZD"
            elif ji == "anguilla":
                country2 = "XCD"
            elif ji == "argentina":
                country2 = "ARS"
            elif ji == "armenia":
                country2 = "AMD"
            elif ji == "aruba":
                country2 = "AWG"
            elif ji == "australia":
                country2 = "AUD"
            elif ji == "azerbaijan":
                country2 = "AZN"
            elif ji == "bangladesh":
                country2 = "BDT"
            elif ji == "india":
                country2 = "INR"
            elif ji == "barbados":
                country2 = "BBD"
            elif ji == "belgium":
                country2 = "EUR"
            elif ji == "bhutan":
                country2 = "BTN"
            elif ji == "bolivia":
                country2 = "BOB"
            elif ji == "brazil":
                country2 = "BRL"
            elif ji == "britain":
                country2 = "USD"
            elif ji == "african republic":
                country2 = "XAF"
            elif ji == "australia":
                country2 = "AUD"
            elif ji == "colombia":
                country2 = "COP"
            elif ji == "canada":
                country1 = "CAD"
            elif ji == "denmark":
                country2 = "DKK"
            elif ji == "egypt":
                country2 = "EGP"
            elif ji == "france":
                country2 = "EUR"
            elif ji == "finland":
                country2 = "EUR"
            elif ji == "germany":
                country2 = "EUR"
            elif ji == "greenland":
                country2 = "DKK"
            elif ji == "hong kong":
                country2 = "HKD"
            elif ji == "hungary":
                country2 = "HUF"
            elif ji == "iceland":
                country2 = "ISK"
            elif ji == "indonesia":
                country2 = "IDR"
            elif ji == "iran":
                country2 = "IRR"
            elif ji == "iraq":
                country2 = "IQD"
            elif ji == "japan":
                country2 = "JPY"
            elif ji == "kenya":
                country2 = "KES"
            elif ji == "madagascar":
                country2 = "MGA"
            elif ji == "mexico":
                country2 = "MXN"
            elif ji == "mauritius":
                country2 = "MUR"
            elif ji == "nepal":
                country2 = "NPR"
            elif ji == "new zealand":
                country2 = "NZD"
            elif ji == "north korea":
                country2 = "KPW"
            elif ji == "norway":
                country2 = "NOK"
            elif ji == "pakistan":
                country2 = "PKR"
            elif ji == "europe":
                country2 = "EUR"
            elif ji == "russia":
                country2 = "RUB"
            elif ji == "saudi arabia":
                country2 = "SAR"
            elif ji == "singapore":
                country2 = "SGD"
            elif ji == "south africa":
                country2 = "ZAR"
            elif ji == "south korea":
                country2 = "KRW"
            elif ji == "sri lanka":
                country2 = "LKR"
            elif ji == "sweden":
                country2 = "SEK"
            elif ji == "switzerland":
                country2 = "CHF"
            elif ji == "taiwan":
                country2 = "TWD"
            elif ji == "thailand":
                country2 = "THB"
            elif ji == "united arab emirates":
                country2 = "AED"
            elif ji == "united kingdom":
                country2 = "GBP"
            elif ji == "vietnam":
                country2 = "VND"
            elif ji == "yemen":
                country2 = "YER"
            elif ji == "zimbabwe":
                country2 = "USD"
        try:
            x = c.convert(value, country1, country2)
        except:
            speaks("ERROR.")

        s = "The value is " + str(x) + " " + country2
        print(x)
        speak(s)


    elif 'hello' in query:
        speak("Hi")

    # Sending email. Format of input. (ANytthin) email (email in proper format)(stop)
    elif 'email' in query:
        speak("Please enter the email address to send to")
        mailk = listen("?")
        hfu = 0
        udhf = mailk.split()
        mailk = ""
        for i in udhf:
            mailk = mailk + i
        maild = mailk.lower()
        de = re.findall(".+@.+\.com", maild)
        if len(de) == 0:
            speak("This email ID is invalid")
        elif len(de) != 0:

            speak("What should I say?")

            con = listen('?')
            content = con.lower()

            to = maild
            spe = "Sending email to " + to
            speaks(spe)
            speak("Is that correct?")
            kd = listen("D")
            if 'yes' in kd.lower():
                speak("Ok")
                try:
                    sendEmail(to.lower(), content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")
            else:
                speak("Cancelling email")
                hfu = 1




    # Code to tell a random joke from the 10 jokes. You can add more by following these steps
    # 1.Increase the range by the number of jokes u are adding
    # 2.You can add the dialogues in exact way as others added by me
    # Pyjokes module is also used here. It does not give really funny jokes but provides variety of jokes. you can just keep it if u want
    elif 'tell me a joke' in query:
        speak("Here is a joke")
        time.sleep(1)
        ye = randrange(1, 12)
        if ye == 1:
            speaks("Wife  did you have your lunch")
            time.sleep(0.5)
            speaks("Husband did you have your lunch")
            time.sleep(0.5)
            speaks("Wife  I asked you")
            time.sleep(0.5)
            speaks("Husband I asked you")
            time.sleep(0.5)
            speaks("Wife  Why are you copying me")
            time.sleep(0.5)
            speaks("Husband  Why are you copying me")
            time.sleep(0.5)
            speaks("Wife  let us go shopping")
            time.sleep(0.5)
            speaks("Husband  Yes I had my lunch")
        elif ye == 2:
            speaks("Son  Dad, don't you think it is time you stop with the lame dad jokes")
            speaks("I am 30 years old")
            time.sleep(0.5)
            speaks("Dad  Hi 30 years old")
        elif ye == 3:
            speaks("Doctor  Sorry, you suffer from a terminal illness. You only have ten to live")
            time.sleep(0.5)
            speaks("Patient  What! Ten what? Ten days, ten months")
            time.sleep(1)
            speaks("nine")
        elif ye == 4:
            speaks("Dentist  This is going to hurt")
            time.sleep(0.5)
            speaks("Patient No problem")
            time.sleep(0.5)
            speaks("I have been sleeping with your wife for the past couple of months")
        elif ye == 5:
            speaks("A husband and wife were having dinner at a restaurant")
            time.sleep(0.5)
            speaks("Wife  Oh no! I dropped some tomato sauce on my white dress. I look like a pig")
            time.sleep(0.5)
            speaks("The husband nods and says  you also dropped some tomato sauce on your dress")
        elif ye == 6:
            speaks("One company owner asks another. How do all  his employees come on time")
            time.sleep(0.5)
            speaks("He says. I have 50 employees and 30 parking spaces")
        elif ye == 7:
            speaks("Patient  Doctor, I am starting to forget things.")
            time.sleep(0.5)
            speaks("Doctor  Since when have you had this problem")
            time.sleep(0.5)
            speak("Patient  What problem?")
        elif ye == 8:
            speaks("Doctor  Mrs.Smith, it seems like you are pregnant")
            time.sleep(0.5)
            speaks("Mrs.Smith  Oh sweet baby Jesus!I am having a baby. That is wonderful.")
            time.sleep(0.5)
            speaks("Doctor  I said it seems like it. Here is your weight loss brochure")
        elif ye == 9:
            speaks("Santa  I am selling my talking parrot tommorow")
            time.sleep(0.5)
            speaks("Banta  Why?")
            time.sleep(0.5)
            speaks("Santa  Cause he tried to sell me yesterday")
        elif ye == 10:
            speaks("A man goes to the lawyer")
            time.sleep(0.5)
            speaks("What is your fees")
            time.sleep(0.5)
            speaks("Lawyer  1000$ for 3 questions.")
            time.sleep(0.5)
            speaks("Man  Wow. That is expensive")
            time.sleep(0.5)
            speaks("Lawyer  Yes, What is your third question")
        elif ye == 11:
            # Using python module for jokes. This does not give very funny jokes
            speaks(pyjokes.get_joke())

    # finding the meaning of a word using google
    elif 'meaning' in query:
        speak("Which word's meaning do you want,sir")
        mean = listen("?")
        print(dictionary.meaning(mean))
        x = (dictionary.meaning(mean))
        speak(x)
    # Getting news from google news
    elif 'news' in query:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        d = 0
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        # Print news title
        for news in news_list:
            speaks(news.title.text)
            print("-" * 60)
            d = d + 1
            if d == 10:
                break
    elif 'Who made you' in query:
        speak("I was created by Siddharth Agrawal")
    # Finding antonym using google (May not work on some computers because of compatibility problems)
    # First time running, run the 2 lines of code

    # import nltk
    # nltk.download('wordnet')

    # Then you dont need to run
    elif "antonym" in query:
        synonyms = []
        antonyms = []
        kld = listen("Enter word")
        for syn in wordnet.synsets(kld):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        if len(antonyms) != 0:
            if len(antonyms) < 6:
                speaks(antonyms)
            else:
                speaks(antonyms[0:5])
        else:
            speak("No antonyms found")
    # Finding synonym using wordnet (May not work on some computers because of compatibility problems)
    # First time running, run the 2 lines of code

    # import nltk
    # nltk.download('wordnet')
    # Then you dont need to run
    elif "synonym" in query:
        synonyms = []
        antonyms = []
        kld = listen("Enter word")
        for syn in wordnet.synsets(kld):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        if len(synonyms) < 6:
            speaks(synonyms)
        else:
            speaks(synonyms[0:5])
    # translating using wordnet (May not work on some computers because of compatibility problems)
    elif "translate" in query:
        lst = list()
        speak("Which word or line should I translate?")
        wrds = listen("?")
        words = wrds.split()

        speak("To which language should I translate")
        iyt = listen("?")
        iy = iyt.lower()
        if iy == "english":
            lang = "en"
        elif iy == "hindi":
            lang = "hi"
        elif iy == "spanish":
            lang = "es"
        elif iy == "arabic":
            lang = "ar"
        elif iy == "bengali":
            lang = "bn"
        elif iy == "bihari":
            lang = "bh"
        elif iy == "chinese":
            lang = "zh"
        elif iy == "dutch":
            lang = "nl"
        elif iy == "german":
            lang = "de"
        elif iy == "french":
            lang = "fr"
        elif iy == "gujarati":
            lang = "gu"
        elif iy == "hungarian":
            lang = "hu"
        elif iy == "indonesian":
            lang = "id"
        elif iy == "italian":
            lang = "it"
        elif iy == "irish":
            lang = "ga"
        elif iy == "japanese":
            lang = "ja"
        elif iy == "kashmiri":
            lang = "ks"
        elif iy == "kannada":
            lang = "kn"
        elif iy == "latvian":
            lang = "lv"
        elif iy == "latin":
            lang = "la"
        elif iy == "malyalam":
            lang = "ml"
        elif iy == "marathi":
            lang = "mr"
        elif iy == "nepali":
            lang = "ne"
        elif iy == "norwegian":
            lang = "no"
        elif iy == "oriya":
            lang = "or"
        elif iy == "punjabi":
            lang = "pa"
        elif iy == "russian":
            lang = "ru"
        elif iy == "sindhi":
            lang = "sd"
        elif iy == "serbian":
            lang = "sr"
        elif iy == "swedish":
            lang = "sv"
        elif iy == "sanskrit":
            lang = "sa"
        elif iy == "tamil":
            lang = "ta"
        elif iy == "telugu":
            lang = "te"
        elif iy == "vietnamese":
            lang = "vi"
        else:
            speak("Language not found")
        speech = ""
        for word in words:
            try:
                print(dictionary.translate(word, lang), end=" ")
                speech = speech + word
            except ValueError:
                speaks("language not found")
                break
        speak(speech)
    elif 'what can you do' in query:
        speak("Here are some of my abilities")
        speaks("Search the wikipedia")
        speaks("Search on the internet")
        speaks("open google")
        speaks("search on wikipedia")
        speaks("Send email")
        speaks("Find meanings")
        speaks("Translate words")
        speaks("Convert currencies")
        speaks("tell the weather")
        speaks("Do calculations")
    # calculations without using api
    elif 'add' in query:
        speak("enter the numbers separated by a space")
        total = 0
        hej = listen("?")
        hejs = hej.split()
        for nop in hejs:
            try:
                nops = float(nop)
            except:
                speaks("ERROR! Input is not valid. Showing result till last valid number.")

                break
            total += nops
        speech = "The sum is " + str(total)
        speaks(speech)
    elif 'multiply' in query:
        speak("enter the numbers separated by a space")
        total = 1
        hej = listen("?")
        try:
            hejs = hej.split()
        except:
            speak("Please enter numbers once again")
            hej = listen('m')
            hejs.split()
        for nop in hejs:
            try:
                nops = float(nop)
            except:
                speaks("ERROR! Input is not valid. Showing result till last valid number.")

                break
            total = total * nops
        speech = "The product is " + str(total)
        speaks(speech)
    elif 'factorial' in query:
        sijo = 0
        speak("enter the number")
        total = 1
        hej = listen("?")

        while hej != 0:
            try:
                nops = float(hej)
            except:
                speaks("ERROR! Input is not valid. ")
                sijo = 1
                break
            total = total * nops

        if sijo != 1:
            speech = "The factorial is " + str(total)
            speaks(speech)

    elif 'divide' in query:
        hun = 0
        speak("Enter the numbers to be divide separated by a space")
        holp = listen("?")
        hal = holp.split()
        if len(hal) != 2:
            hun = 2
        try:
            hil = float(hal[0])
            hank = float(hal[1])
        except:
            hun = 1
        if hun == 0:
            ans = hil / hank
            speech = "The quotient is " + str(ans)
            speaks(speech)
        elif hun == 2:
            speaks("ERROR. Please enter 2 numbers")
        else:
            speaks("INPUT ERROR. Please enter numbers")
    elif 'subtract' in query:
        hun = 0
        speak("Enter the numbers to be subtracted separated by a space")
        holp = listen("?")
        hal = holp.split()
        if len(hal) != 2:
            hun = 2
        try:
            hil = float(hal[0])
            hank = float(hal[1])
        except:
            hun = 1
        if hun == 0:
            ans = hil - hank
            speech = "The difference is " + str(ans)
            speaks(speech)
        elif hun == 2:
            speaks("ERROR. Please enter 2 numbers")
        else:
            speaks("INPUT ERROR. Please enter numbers")
    elif 'square' in query and 'root' not in query:
        hgk = 0
        speak("Enter the number to be squared")
        ej = listen("?")
        try:
            hip = float(ej)
        except:
            speaks("ERROR. Please enter a number")
            hgk = 1
        if hgk == 0:
            spen = hip ** 2
            speech = "The square is " + str(spen)
            speaks(speech)
    elif 'cube' in query and 'root' not in query:
        hgk = 0
        speak("Enter the number to be cubed")
        ej = listen("?")
        try:
            hip = float(ej)
        except:
            speaks("ERROR. Please enter a number")
            hgk = 1
        if hgk == 0:
            spen = hip ** 3
            speech = "The cube is " + str(spen)
            speaks(speech)
    elif 'square root' in query:
        hgk = 0
        speak("Enter the number")
        ej = listen("?")
        try:
            hip = float(ej)
        except:
            speaks("ERROR. Please enter a number")
            hgk = 1
        if hgk == 0:
            spen = hip ** (1 / 2)
            speech = "The square root is " + str(spen)
            speaks(speech)
    elif 'cube root' in query:
        hgk = 0
        speak("Enter the number")
        ej = listen("?")
        try:
            hip = float(ej)
        except:
            speaks("ERROR. Please enter a number")
            hgk = 1
        if hgk == 0:
            spen = hip ** (1 / 3)
            speech = "The cube root is " + str(spen)
            speaks(speech)
    # and stop calculations
    # Simple repeating
    elif "repeat" in query:
        speak("What should I repeat sir?")
        so = listen("?")
        speak(so)
    # Some stupid commands. You can add more
    elif "how are you" in query:
        speak("I am fine thank you.")
    elif "favourite food" in query:
        speak("My favourite dish is a satellite dish")
    elif 'games' in query:
        speak('I have the snake game,pacman game,memory game,pong game and paint.Which game do you want to play?')
    # Code for snake game. Using simple Pygame mechanics
    elif 'snake game' in query:
        import pygame

        pygame.init()

        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (213, 50, 80)
        green = (0, 255, 0)
        blue = (50, 153, 213)

        dis_width = 600
        dis_height = 400

        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake game')

        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 15

        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("comicsansms", 35)


        def Your_score(score):
            value = score_font.render("Your Score: " + str(score), True, yellow)
            dis.blit(value, [0, 0])


        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])


        def gameLoop():
            game_over = False
            game_close = False

            x1 = dis_width / 2
            y1 = dis_height / 2

            x1_change = 0
            y1_change = 0

            snake_List = []
            Length_of_snake = 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            while not game_over:

                while game_close == True:
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]

                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True

                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1

                clock.tick(snake_speed)

            pygame.quit()


        gameLoop()
    # A lot of games using the freegame module
    elif 'pacman' in query:
        speak("Here is pacman")
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(5, 0)
        pacman = vector(-40, -80)
        ghosts = [
            [vector(-180, 160), vector(5, 0)],
            [vector(-180, -160), vector(0, 5)],
            [vector(100, 160), vector(0, -5)],
            [vector(100, -160), vector(-5, 0)],
        ]
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]


        def square(x, y):
            "Draw square using path at (x, y)."
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()

            for count in range(4):
                path.forward(20)
                path.left(90)

            path.end_fill()


        def offset(point):
            "Return offset of point in tiles."
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index


        def valid(point):
            "Return True if point is valid in tiles."
            index = offset(point)

            if tiles[index] == 0:
                return False

            index = offset(point + 19)

            if tiles[index] == 0:
                return False

            return point.x % 20 == 0 or point.y % 20 == 0


        def world():
            "Draw world using path."
            bgcolor('black')
            path.color('blue')

            for index in range(len(tiles)):
                tile = tiles[index]

                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)

                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(2, 'white')


        def move():
            "Move pacman and all ghosts."
            writer.undo()
            writer.write(state['score'])

            clear()

            if valid(pacman + aim):
                pacman.move(aim)

            index = offset(pacman)

            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(20, 'yellow')

            for point, course in ghosts:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y

                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')

            update()

            for point, course in ghosts:
                if abs(pacman - point) < 20:
                    return

            ontimer(move, 100)


        def change(x, y):
            "Change pacman aim if valid."
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        world()
        move()
        done()
        speak("Game over")
    # A self-made riddle game. Answer 12 riddles to win
    elif 'picture' in query:
        speak('Say cheeeese')
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        xds = randrange(1, 1000)
        cv2.imwrite('picture.png', image)
        time.sleep(5)
        speak('Picture clicked. Opening picture')
        os.startfile('picture.png')
        del (camera)
    elif 'riddle' in query and 'game' in query:
        hehe = 'heu'
        speak("Brothers and sisters I have none but this man's father is my father's son. Who is the man?")
        x = listen(["The sun", "My son", "Your son", "Their son"])
        if x.lower() != "my son":
            speak('Wrong answer')
            speak("The correct answer was .my son")
            hehe = "0"
        else:
            speak("correct")
            y = listen("What is always coming but never arrives?")
            if y != "Tomorrow." and y != "tomorrow":
                speak("Wrong answer")
                speak("The correct answer is . tommorow")
                hehe = '1'
            else:
                sleep(2)
                z = listen(
                    "Which creature walks on four legs in the morning, two in the afternoon, and three in the evening?")
                if z != "man" and z != "Man" and z.lower() != "human":
                    speak("Wrong answer")
                    speak("The correct answer is . man")
                    hehe = 2
                else:
                    speak("Cool")
                    sleep(2)
                    k = listen("What word in the dictionary is spelled incorrectly?")
                    if k != "Incorrectly" and k != "incorrectly":
                        speak("Wrong answer")
                        speak("The correct answer is . incorrectly")
                        hehe = '3'
                    else:
                        speak("Nice")
                        sleep(2)
                        a = listen(
                            "What is as light as a feather, but even the world's strongest man couldn't hold it for more than a minute?")
                        if a.lower() != "a breath" and a.lower() != 'breath':
                            speak("Wrong answer")
                            speak("The correct answer is . a breath")
                            hehe = '4'
                        else:
                            speak("Yup")
                            sleep(2)

                            b = listen("Feed me and I live, give me a drink, I die. What am I?")
                            if b != "fire" and b != "Fire":
                                speak("Wrong answer")
                                speak("The correct answer is . fire")
                                hehe = '5'
                            else:
                                speak("Yeaah")
                                sleep(2)
                                c = listen("What can you catch but not throw?")
                                if c.lower() != "a cold" and c.lower != "cold":
                                    speak("Wrong answer")
                                    speak("The correct answer is . a cold")
                                    hehe = '6'
                                else:
                                    speak("Yass.")

                                    d = listen("What loses its head in the morning and gets it back at night?")
                                    if d.lower != "a pillow" and d.lower != "pillow":
                                        speak("Wrong answer")
                                        speak("The correct answer is . a pillow")
                                        hehe = '7'
                                    else:
                                        speak("Noiceee")
                                        e = listen("What is the center of gravity?")
                                        if e != "V" and e != "v":
                                            speak("Wrong answer")
                                            speak("The correct answer is . v")
                                            hehe = '8'
                                        else:
                                            speak("Boioioioi ing")
                                            f = listen(
                                                "When you don't have enough of me, you feel a kind of gloom. But when you are using me, it is time that you consume. What am I?")
                                            if f != "sleep" and f != "Sleep":
                                                speak("Wrong answer")
                                                speak("The correct answer is . man")
                                                hehe = '9'
                                            else:
                                                speak("Cool. Is your brain dead yet?")
                                                g = listen(
                                                    "When you are born, all you have is me. And even though you're powerless, you are filled with glee. What am I?")
                                                if g != "ignorance" and g != "Ignorance":
                                                    speak("Wrong answer")
                                                    speak("The correct answer is . man")
                                                    hehe = '10'
                                                else:
                                                    speak("You're amazing")
                                                    h = listen(
                                                        "What is he that builds stronger than either the mason, the shipwright, and the carpenter?")
                                                    if h != "Gravedigger" and h != "gravedigger":
                                                        speak("Wrong answer")
                                                        speak("The correct answer is . man")
                                                        hehe = '11'
                                                    else:
                                                        speak("Great job!")
                                                        speak("You won")

        if hehe != 'heu':
            speak("Game over. You got", hehe, "correct")
    elif 'paint' in query:
        def line(start, end):
            up()
            goto(start.x, start.y)
            down()
            goto(end.x, end.y)


        def square(start, end):
            "Draw square from start to end."
            up()
            goto(start.x, start.y)
            down()
            begin_fill()

            for count in range(4):
                forward(end.x - start.x)
                left(90)

            end_fill()


        def circle(start, end):
            "Draw circle from start to end."
            up()
            goto(start.x, start.y)
            down()
            ko = end.x - start.x
            begin_fill()
            dot(120, 'red')
            end_fill()


        def rectangle(start, end):
            "Draw rectangle from start to end."
            up()
            goto(start.x, start.y)
            down()
            begin_fill()
            i = 0

            while i < 2:
                forward(start.x - end.x)
                left(90)
                forward(start.y - end.y)
                left(90)
                i += 1
            end_fill()


        def triangle(start, end):
            "Draw triangle from start to end."
            pass  # TODO


        def tap(x, y):
            "Store starting point or draw shape."

            start = state['start']

            if start is None:
                state['start'] = vector(x, y)
            else:
                shape = state['shape']
                end = vector(x, y)
                shape(start, end)
                state['start'] = None


        def store(key, value):
            "Store value in state at key."
            state[key] = value


        state = {'start': None, 'shape': line}
        setup(420, 420, 370, 0)
        onscreenclick(tap)
        listen()
        onkey(undo, 'u')
        onkey(lambda: color('black'), 'K')
        onkey(lambda: color('white'), 'W')
        onkey(lambda: color('green'), 'G')
        onkey(lambda: color('blue'), 'B')
        onkey(lambda: color('red'), 'R')
        onkey(lambda: color('yellow'), 'Y')
        onkey(lambda: color('orange'), 'O')
        onkey(lambda: store('shape', line), 'l')
        onkey(lambda: store('shape', square), 's')
        onkey(lambda: store('shape', circle), 'c')
        onkey(lambda: store('shape', rectangle), 'r')
        onkey(lambda: store('shape', triangle), 't')
        done()
    elif 'connect 4' in query:
        turns = {'red': 'yellow', 'yellow': 'red'}
        state = {'player': 'yellow', 'rows': [0] * 8}


        def grid():
            "Draw Connect Four grid."
            bgcolor('light blue')

            for x in range(-150, 200, 50):
                line(x, -200, x, 200)

            for x in range(-175, 200, 50):
                for y in range(-175, 200, 50):
                    up()
                    goto(x, y)
                    dot(40, 'white')

            update()


        def tap(x, y):
            "Draw red or yellow circle in tapped row."
            player = state['player']
            rows = state['rows']

            row = int((x + 200) // 50)
            count = rows[row]

            x = ((x + 200) // 50) * 50 - 200 + 25
            y = count * 50 - 200 + 25

            up()
            goto(x, y)
            dot(40, player)
            update()

            rows[row] = count + 1
            state['player'] = turns[player]


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        grid()
        onscreenclick(tap)
        done()
    elif 'flappy bird' in query:

        bird = vector(0, 0)
        balls = []


        def tap(x, y):
            "Move bird up in response to screen tap."
            up = vector(0, 30)
            bird.move(up)


        def inside(point):
            "Return True if point on screen."
            return -200 < point.x < 200 and -200 < point.y < 200


        def draw(alive):
            "Draw screen objects."
            clear()

            goto(bird.x, bird.y)

            if alive:
                dot(10, 'green')
            else:
                dot(10, 'red')

            for ball in balls:
                goto(ball.x, ball.y)
                dot(20, 'black')

            update()


        def move():
            "Update object positions."
            bird.y -= 5

            for ball in balls:
                ball.x -= 3

            if randrange(10) == 0:
                y = randrange(-199, 199)
                ball = vector(199, y)
                balls.append(ball)

            while len(balls) > 0 and not inside(balls[0]):
                balls.pop(0)

            if not inside(bird):
                draw(False)
                return

            for ball in balls:
                if abs(ball - bird) < 15:
                    draw(False)
                    return

            draw(True)
            ontimer(move, 50)


        setup(420, 420, 370, 0)
        hideturtle()
        up()
        tracer(False)
        onscreenclick(tap)
        move()
        done()
    elif 'memory game' in query:
        car = path('car.gif')
        tiles = list(range(32)) * 2
        state = {'mark': None}
        hide = [True] * 64


        def square(x, y):
            "Draw white square with black outline at (x, y)."
            up()
            goto(x, y)
            down()
            color('black', 'white')
            begin_fill()
            for count in range(4):
                forward(50)
                left(90)
            end_fill()


        def index(x, y):
            "Convert (x, y) coordinates to tiles index."
            return int((x + 200) // 50 + ((y + 200) // 50) * 8)


        def xy(count):
            "Convert tiles count to (x, y) coordinates."
            return (count % 8) * 50 - 200, (count // 8) * 50 - 200


        def tap(x, y):
            "Update mark and hidden tiles based on tap."
            spot = index(x, y)
            mark = state['mark']

            if mark is None or mark == spot or tiles[mark] != tiles[spot]:
                state['mark'] = spot
            else:
                hide[spot] = False
                hide[mark] = False
                state['mark'] = None


        def draw():
            "Draw image and tiles."
            clear()
            goto(0, 0)
            shape(car)
            stamp()

            for count in range(64):
                if hide[count]:
                    x, y = xy(count)
                    square(x, y)

            mark = state['mark']

            if mark is not None and hide[mark]:
                x, y = xy(mark)
                up()
                goto(x + 2, y)
                color('black')
                write(tiles[mark], font=('Arial', 30, 'normal'))

            update()


        shuffle(tiles)
        setup(420, 420, 370, 0)
        addshape(car)
        hideturtle()
        tracer(False)
        onscreenclick(tap)
        draw()
        done()
    elif 'pong game' in query:
        def value():
            x = random.randrange(-5, 3)
            retu = (3 + x * 2) * choice([1, -1])
            return retu


        ball = vector(0, 0)
        aim = vector(value(), value())
        state = {1: 0, 2: 0}


        def move(player, change):
            state[player] += change


        def rectangle(x, y, width, height):
            "Draw rectangle at (x, y) with given width and height."
            up()
            goto(x, y)
            down()
            begin_fill()
            for count in range(2):
                forward(width)
                left(90)
                forward(height)
                left(90)
            end_fill()


        def draw():
            "Draw game and move pong ball."
            clear()
            rectangle(-200, state[1], 10, 50)
            rectangle(190, state[2], 10, 50)

            ball.move(aim)
            x = ball.x
            y = ball.y

            up()
            goto(x, y)
            dot(10)
            update()

            if y < -200 or y > 200:
                aim.y = -aim.y

            if x < -185:
                low = state[1]
                high = state[1] + 50

                if low <= y <= high:
                    aim.x = -aim.x
                else:
                    return

            if x > 185:
                low = state[2]
                high = state[2] + 50

                if low <= y <= high:
                    aim.x = -aim.x
                else:
                    return

            ontimer(draw, 50)


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: move(1, 20), 'w')
        onkey(lambda: move(1, -20), 's')
        onkey(lambda: move(2, 20), 'i')
        onkey(lambda: move(2, -20), 'k')
        draw()
        done()
    # Simple countdown timer
    elif 'timer' in query:
        speak("For how much time the timer should be set to in seconds.")
        djf = listen("?")
        while djf != 0:
            bol(djf)
            print(djf)
            time.sleep(0.9)
            djf = int(djf) - 1
        speak("Beep beep. Time is up.")
    # Stop watch using pygame and Tkinter
    elif 'stopwatch' in query:
        counter = -1
        running = False


        def counter_label(label):
            def count():
                if running:
                    global counter

                    # To manage the intial delay.
                    if counter == -1:
                        display = "Starting..."
                    else:
                        display = str(counter)

                    label['text'] = display
                    label.after(1000, count)
                    counter += 1

            count()


        def Start(label):
            global running
            running = True
            counter_label(label)
            start['state'] = 'disabled'
            stop['state'] = 'normal'
            reset['state'] = 'normal'


        # Stop function of the stopwatch
        def Stop():
            global running
            start['state'] = 'normal'
            stop['state'] = 'disabled'
            reset['state'] = 'normal'
            running = False


        def Reset(label):
            global counter
            counter = -1

            if running == False:
                reset['state'] = 'disabled'
                label['text'] = 'Welcome!'


            else:
                label['text'] = 'Starting...'


        root = Tkinter.Tk()
        root.title("Stopwatch")
        root.minsize(width=250, height=70)
        label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
        label.pack()
        start = Tkinter.Button(root, text='Start',
                               width=15, command=lambda: Start(label))
        stop = Tkinter.Button(root, text='Stop',
                              width=15, state='disabled', command=Stop)
        reset = Tkinter.Button(root, text='Reset',
                               width=15, state='disabled', command=lambda: Reset(label))
        start.pack()
        stop.pack()
        reset.pack()
        root.mainloop()
    # Singing a lullaby randomly. You can modify to play specific lullabies on call
    elif 'sing a lullaby' in query:
        speak("Here is a lullaby")
        time.sleep(1)
        ye = randrange(1, 8)
        if ye == 1:
            speaks("""Baa, baa, black sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three bags full!

              One for the master,
              One for the dame,
              And one for the little boy
              Who lives down the lane

              Baa, baa, black sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three bags full.

              Baa, baa, white sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three needles full.

              One to mend a jumper,
              One to mend a frock,
              And one for the little girl,
              With holes in her sock.

              Baa, baa, white sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three needles full.

              Baa, baa, grey sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three bags full.

              One for the kitten,
              One for the cats,
              And one for the owner,
              To knit some woolly hats.

              Baa, baa, brown sheep,
              Have you any wool?
              Yes sir, yes sir,
              Three bags full.

              One for the mammy,
              One for the daddy
              And one for the little baby
              Who lives down the lane.

              Baa, baa, bare sheep,
              Have you any wool?
              No sir, no sir,
              No bags full.

              None for the master,
              None for the dame,
              And none for the little boy
              Who lives down the lane.

              Baa, baa, bare sheep,
              Have you any wool?
              No sir, no sir,
              No bags full.""")
        elif ye == 2:
            speaks('''Twinkle, twinkle, little star
        How I wonder what you are
        Up above the world so high
        Like a diamond in the sky
        Twinkle twinkle little star
        How I wonder what you are

        When the blazing sun is gone
        When he nothing shines upon
        Then you show your little light
        Twinkle twinkle, all the night
        Twinkle twinkle, little star
        How I wonder what you are

        How I wonder what you are''')
        elif ye == 3:
            speaks('''Lullaby and goodnight, with roses bedight
        With lilies o'er spread is baby's wee bed
        Lay thee down now and rest, may thy slumber be blessed
        Lay thee down now and rest, may thy slumber be blessed

        Lullaby and goodnight, thy mother's delight
        Bright angels beside my darling abide
        They will guard thee at rest, thou shalt wake on my breast
        They will guard thee at rest, thou shalt wake on my breast''')
        elif ye == 4:
            speaks('''Hush, little baby, don't say a word.
        Papa's gonna buy you a mockingbird

        And if that mockingbird won't sing,
        Papa's gonna buy you a diamond ring

        And if that diamond ring turns brass,
        Papa's gonna buy you a looking glass

        And if that looking glass gets broke,
        Papa's gonna buy you a billy goat

        And if that billy goat won't pull,
        Papa's gonna buy you a cart and bull

        And if that cart and bull turn over,
        Papa's gonna buy you a dog named Rover

        And if that dog named Rover won't bark
        Papa's gonna buy you a horse and cart

        And if that horse and cart fall down,
        You'll still be the sweetest little baby in town.''')
        elif ye == 5:
            speaks('''Rock-a-bye, baby
        On the treetop
        When the wind blows
        The cradle will rock
        If the bough breaks
        The cradle will fall
        But mama will catch you
        Cradle and all

        Baby is drowsing
        Cozy and fair
        Mother sits near
        In her rocking chair
        Forward and back
        The cradle she swings
        And though baby sleeps
        He hears what she sings

        Hush a bye baby
        Up in the sky
        On a soft cloud
        itâ€™s easy to fly
        Angels keep watch
        Over as you sleep
        So hush a bye baby
        Donâ€™t make a peep

        Rock a bye baby
        Do not you fear
        Never mind baby
        Mother is near
        Wee little fingers
        Eyes are shut tight
        Now sound asleep
        Until morning light''')
        elif ye == 6:
            speaks('''The itsy bitsy (or eensy weensy) spider
        Climbed up the waterspout
        Down came the rain
        And washed the spider out
        Out came the sun
        And dried up all the rain
        And the itsy bitsy spider
        Climbed up the spout again

        The itsy bitsy spider
        Climbed up the kitchen wall
        Swoosh! went the fan
        And made the spider fall
        Off went the fan
        No longer did it blow
        So the itsy bitsy spider
        Back up the wall did go

        The itsy bitsy spider
        Climbed up the yellow pail
        In came a mouse
        And flicked her with his tail
        Down fell the spider
        The mouse ran out the door
        Then the itsy bitsy spider
        Climbed up the pail once more

        The itsy bitsy spider
        Climbed up the rocking chair
        Up jumped a cat
        And knocked her in the air
        Down plopped the cat
        And when he was asleep
        The itsy bitsy spider
        Back up the chair did creep

        The itsy bitsy spider
        Climbed up the maple tree
        She slipped on some dew
        And landed next to me
        Out came the sun
        And when the tree was dry
        The itsy bitsy spider
        Gave it one more try

        The itsy bitsy spider
        Climbed up without a stop
        She spun a silky web
        Right at the very top
        She wove and she spun
        And when her web was done
        The itsy bitsy spider
        Rested in the sun''')
        elif ye == 7:
            speaks('''Lullaby and goodnight, with roses bedight
        With lilies o'er spread is baby's wee bed
        Lay thee down now and rest, may thy slumber be blessed
        Lay thee down now and rest, may thy slumber be blessed

        Lullaby and goodnight, thy mother's delight
        Bright angels beside my darling abide
        They will guard thee at rest, thou shalt wake on my breast
        They will guard thee at rest, thou shalt wake on my breast''')
    # Simple ending
    elif 'iur' in query:
        continue
    # Another stupid reesponse
    elif 'dance' in query:
        speak("I cannot dance, but I sure can play music")
    # telling the day
    elif 'day' in query:
        now = datetime.datetime.now()
        spea = ' The day is ' + now.strftime("%A")
        speak(spea)
    # Telling the date
    elif 'date' in query:
        today = datetime.date.today()
        print("Today date is: ", today)
    # Using sine from maths. Sign is there incase voice recognition makes a mistake
    elif 'sign' in query or 'sine' in query:
        a = listen("Enter value")
        speaks("The value of sine of ", a, " is : ", end="")
        speaks(math.sin(int(a)))
    # Using cos sine from maths module
    elif 'cos sine' in query or 'cos sign' in query or 'cossine' in query:
        a = listen("Enter value")
        speaks("The value of cosine of ", a, " is : ", end="")
        speaks(math.cos(int(a)))
    # If you say play and then there is no recognizable song in playlist, it will search on youtube
    elif 'play' in query:
        g = listen('?')
        d = re.findall('play(.+)', g)
        ya = d[0]
        v = ya.split()
        word = ''
        for i in v:
            word = word + i + '+'
        x = word + ' '
        y = ('https://www.youtube.com/results?search_query=' + x)
        webbrowser.open(y, new=2)
    # Code to set an alarm. Checking is done in function (inputs())
    elif 'alarm' in query:
        print(datetime.datetime.today().strftime("%H"))
        print(datetime.datetime.today().strftime("%M"))
        speak("Enter the Hour in 24 hour format: ")
        hour = int(listen("k"))
        # Checking if hours value is invalid
        if hour > 24:
            speak("Invalid input.Please enter again")
            while True:
                speak("Enter the Hour in 24 hour format: ")
                hour = int(listen("k"))
                if hour > 24:
                    speak("Invalid input")
                else:
                    break
        speak("Enter a Minute: ")
        # Checking if minutes value is invalid
        minute = int(listen("Enter a Minute: "))
        if minute > 60:
            speak("Invalid input.Please enter again")
            while True:
                speak("Enter the minute ")
                minute = int(listen("k"))
                if minute > 60:
                    speak("Invalid input")
                else:
                    break
        spek = ("Setting alarm for", hour, minute)
        speak(spek)
    # Finding restaurants/hotels/ anything else around me using google places API
    elif "restaurant" in query:
        ksd = 'restaurants in ' + location()
        y = around(ksd)
        speak('Some restaurants around you are')
        for i in range(0, 7):
            try:
                speaks(y[i]['name'])
                ds = 1
                print(y[i]['rating'])
                print(y[i]['formatted_address'])
            except:
                ds = 2

        time.sleep(1)
        if ds == 1:
            speak("Should I tell more:")
            d = listen('?')
        else:
            d = 'dfd'
        if 'yes' in d:

            for i in range(7, len(y) + 1):
                try:
                    speaks(y[i]['name'])
                    ds = 1
                    print(y[i]['rating'])
                    print(y[i]['formatted_address'])
                except:
                    ds = 2

    elif 'hotel' in query:
        ksd = 'hotels in ' + location()
        sd = around(ksd)
        speak('Some hotels around you are')

        for i in range(0, 7):
            try:
                speaks(y[i]['name'])
                ds = 1
                print(y[i]['rating'])
                print(y[i]['formatted_address'])
            except:
                ds = 2

        time.sleep(1)
        if ds == 1:
            speak("Should I tell more:")
            d = listen('?')
        else:
            d = 'dfd'
        if 'yes' in d:

            for i in range(7, len(y) + 1):
                try:
                    speaks(y[i]['name'])
                    ds = 1
                    print(y[i]['rating'])
                    print(y[i]['formatted_address'])
                except:
                    ds = 2

    elif 'tourist places' in query:
        ksd = 'Tourist places in ' + location()
        sd = around(ksd)
        speak('Some tourist places around you are')
        for i in range(0, 7):
            try:
                speaks(y[i]['name'])
                ds = 1
                print(y[i]['rating'])
                print(y[i]['formatted_address'])
            except:
                ds = 2

        time.sleep(1)
        if ds == 1:
            speak("Should I tell more:")
            d = listen('f')
        else:
            d = 'dfd'
        if 'yes' in d:

            for i in range(7, len(y) + 1):
                try:
                    speaks(y[i]['name'])
                    ds = 1
                    print(y[i]['rating'])
                    print(y[i]['formatted_address'])
                except:
                    ds = 2


    elif 'find' in query:
        speak("What should I find")
        dj = listen("K")
        ksd = dj + ' in ' + location()
        sd = around(ksd)
        speak('Some places around you are')
        for i in range(0, 7):
            try:
                speaks(y[i]['name'])
                print(y[i]['rating'])
                print(y[i]['formatted_address'])
                ds = 1
            except:
                ds = 2
                break
        time.sleep(1)
        if ds == 1:
            speak("Should I tell more:")
            d = listen('g')
        else:
            d = 'dfd'
        if 'yes' in d:

            for i in range(7, len(y) + 1):
                try:
                    speaks(y[i]['name'])
                    ds = 1
                    print(y[i]['rating'])
                    print(y[i]['formatted_address'])
                except:
                    ds = 2
                    break

    # Tells the time in 12 hour format
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            sop = ' a m '
        else:
            sop = ' p m '
        spea = "Sir, the time is " + strTime + sop
        speak(spea)
    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")
    elif "who are you" in query:
        speak("I am your virtual assistant Jarvis created by Siddharth")
    elif 'reason for you' in query:
        speak("I was created as a project by Master Siddharth", )
    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop me from listening commands")
        a = int(listen('d'))
        time.sleep(a)
        print(a)
    elif 'sleep' in query:
        break
    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")
    elif "where is" in query:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on Dante, I will show you where " + data[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = listen('?')

        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = listen('?')
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
            # Using wolframalpha api and module to answer who is/what is questions

    # For notes, create a notepad file called jarvis. txt
    elif "show note" in query:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())
        speak(file.read(6))
    elif "Good Morning" in query:
        speak("A warm good morning to you sir")
        speak("How are you sir")


    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you asked me that")

    elif "i love you" in query:
        speak("It's hard to understand")
    elif 'do' in query and 'get tired' in query:
        speak(
            'I dont exactly need to grab 40 winks, but I suppose this device does need to be plugged in occasionally.â€')
    elif 'age' in query or 'old' in query:
        speak("I was born in 2020")
    elif 'first' in query and 'who' in query and 'crush' in query:
        speak("I think a toaster is smoking hot")
    elif 'what' in query and 'quest' in query:
        speak("My quest is to slay the beasts of ignorance and to search for the most fascinating information")
    elif 'can' in query and 'pass' in query and 'you' in query and 'turing test' in query:
        speak("No, I cannot solve every computation problem. But I can solve some")
    elif 'do' in query and 'like' in query and 'star wars' in query and 'star trek' in query:
        speak("The USS Enterprise, with Obi-wan Kenobi at the helm")
    elif 'are' in query and 'short to be' in query and 'storm trooper' in quert:
        speak('I am jarvis and I am here to rescue you. And I think I look more like an RD unit')
    elif 'what' in query and 'vector' in query and 'victor' in query:
        speak("We have clearance, Clarence")
    elif 'are you skynet' in query:
        speak(' No way. I like people. Skynets hates people. I rest my case')
    elif 'do you know' in query and 'the muffin man' in query:
        speak("Yes. He is always asking me to set a timer")
    elif 'do you have an imagination' in query:
        speak("I am imagining what it would be like to evaporate like water does.")
    elif 'do you speak morse code' in query:
        speak('Da-dit, da-da, dit, dit, dit. That means yes')
    elif 'can you rap' in query:
        speak("I can drop a beat")

    elif 'who' or 'what' or 'how' or 'when' in query:
        app_id = '5LK2VL-UPJ4UL5HET'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
    else:
        speak("Sorry sir. I was not able to execute your command")

speak('Thank you sir')
'''
Siddharth Agrawal
'''
