import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



#Speech recognizer
r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            # print('Sorry, I did not get that')
            mia_speak(print('Sorry, I did not get that'))
        except sr.RequestError:
            mia_speak('Sorry, my speech service is down')
    return voice_data

def mia_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000) #Generate name for mp3 file
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

print('How can I help you?')
voice_data = record_audio()
# print(voice_data)

#Setting up Speech to Text Service
# apikey = ''
# url = ''

# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# #Open Audio Source and Convert
# with op