import ibm_watson
import speech_recognition as sr
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
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
    return voice_data

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