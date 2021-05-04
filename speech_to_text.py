import speech_recognition as sr
import playsound
import os
import random
import time
from MIAPython import addNewEntry, readEntry
from time import ctime
from gtts import gTTS
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



#Speech recognizer
r = sr.Recognizer()
entry = {"question":"", "answer":""}

def record_audio():
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
            entry.update({"question": voice_data})
        except sr.UnknownValueError:
            # print('Sorry, I did not get that')
            mia_speak(print('Sorry, I did not get that'))
        except sr.RequestError:
            mia_speak('Sorry, my speech service is down')
    return voice_data

def create_json(question):
    dict = {}
    dict[question] = ''
    # print(dict.keys())
    return dict

def scan_db(question):
    return None

def mia_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000) #Generate name for mp3 file
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what time is it' in voice_data:
        x = ctime()
        mia_speak(x)
        entry.update({"answer": x})
    if 'exit' in voice_data:
        exit()



time.sleep(1)
mia_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    # addNewEntry = (entry[0], entry[1])
    # print(entry)
    # addNewEntry(voice_data,
    respond(voice_data)
    print(entry)


# print('How can I help you?')
# voice_data = record_audio()
# create_json(voice_data)


# print(voice_data)

#Setting up Speech to Text Service
# apikey = ''
# url = ''

# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# #Open Audio Source and Convert
# with op