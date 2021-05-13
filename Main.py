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
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# def answer_call():
#     """Respond to incoming phone calls with a brief message."""
#     # Start our TwiML response
#     resp = VoiceResponse()

#     # Read a message aloud to the caller
#     resp.say("Thank you for calling! Have a great day. Have a great Day!! Have a great day!!!", voice='alice')

#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)


app = Flask(__name__)

r = sr.Recognizer()
entry = {"question":"", "answer":""}
resp = VoiceResponse()

@app.route("/", methods=['GET', 'POST'])

def record_audio():
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
            entry.update({"question": voice_data})
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
            resp.say('Sorry, I did not get that', voice='alice')
            # mia_speak(print('Sorry, I did not get that'))
        except sr.RequestError:
            resp.say('Sorry, my speech service is down', voice='alice')
            # mia_speak('Sorry, my speech service is down')
    return voice_data

def respond(voice_data):
    if 'what is the time' in voice_data:
        x = ctime()
        resp.say(x, voice='alice')
        # mia_speak(x)
        entry.update({"answer": x})
    if 'exit' in voice_data:
        exit()

# def mia_speak(audio_string):
#     tts = gTTS(text=audio_string, lang='en')
#     r = random.randint(1, 1000000) #Generate name for mp3 file
#     audio_file = 'audio-' + str(r) + '.mp3'
#     tts.save(audio_file)
#     playsound.playsound(audio_file)
#     print(audio_string)
#     os.remove(audio_file)

def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    time.sleep(1)
    resp.say('How can I help you?')
    # mia_speak('How can I help you?')
    while 1:
        voice_data = record_audio()
        # resp.say(voice_data, voice='alice')
        respond(voice_data)
        print(entry)

    # Read a message aloud to the caller
    # resp.say("Thank you for calling! Have a great day.", voice='alice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)


#Find someone to insert the uestio nand answer into the database
#thinking of using a list or needing to build a cusotm object in python to tho this shit
