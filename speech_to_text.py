import speech_recognition as sr
import playsound
import os
import random
import time
import wolframalpha
from MIAPython import addNewEntry, readEntry, mostFrequent, existing_question, updateEntry, deleteEntry
from time import ctime
from gtts import gTTS
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Speech recognizer
r = sr.Recognizer()
client = wolframalpha.Client('2E922Y-48JVAHYP2H')
entry = {"question":"", "answer":"","needsUpdate":"","frequency":""}

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

def mia_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000) #Generate name for mp3 file
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    # print(audio_string)
    os.remove(audio_file)

def ask_wolfram(voice_data):
    question = client.query(voice_data)
    output = next(question.results).text
    return output

#Extracts a subset dictionary of time
def extract_time_info(time):
    time_info = {'Day':'', 'Month':'', 'Day of Month':'','Time':'','Year':''}
    time_info['Day'] = time[0]
    time_info['Month'] = time[1]
    time_info['Day of Month'] = time[2]
    time_info['Time'] = time[3]
    time_info['Year'] = time[4]
    return time_info

def respond(voice_data):
    if 'what is your name' in voice_data:
        name = 'My name is MIA'
        mia_speak(name)
        entry.update({"answer": name})
        if existing_question(voice_data) == True:
            updateEntry(entry['question'], entry['answer'])
            readEntry(entry['question'])
        else:
            addNewEntry(entry['question'], entry['answer'])
            readEntry(entry['question'])
    elif 'what is the most common question' in voice_data:
        x = mostFrequent()
        mia_speak(x)
        entry.update({"answer": x})
        if existing_question(voice_data) == True:
            updateEntry(entry['question'], entry['answer'])
            readEntry(entry['question'])
        else:
            addNewEntry(entry['question'], entry['answer'])
            readEntry(entry['question'])
        #entry updatE?
    elif 'what is the time' in voice_data:
        x = ctime()
        split_time = x.split()
        mia_speak(x)
        broken_time = extract_time_info(split_time)
        entry.update({"answer": x, "details": broken_time})
        print(entry)
        if existing_question(voice_data) == True:
            updateEntry(entry['question'], entry['answer'], entry['details'])
            readEntry(entry['question'])
        else:
            addNewEntry(entry['question'], entry['answer'], entry['details'])
            readEntry(entry['question'])
    elif 'exit' in voice_data:
        exit()
    else: #General Question
        # answer = ask_wolfram(voice_data)
        # mia_speak(answer)
        # entry.update({"answer": answer})
        # if existing_question(voice_data) == True:
        #     updateEntry(entry['question'], entry['answer'])
        #     readEntry(entry['question'])
        # else:
        #     addNewEntry(entry['question'], entry['answer'])
        #     readEntry(entry['question'])
        # updateEntry(entry['question'], entry['answer'])
        if existing_question(voice_data) ==  True:
            old_answer = readEntry(entry['question'])
            entry.update({"answer": old_answer})
            mia_speak(old_answer)
            updateEntry(entry['question'], entry['answer'])
        else:
            answer = ask_wolfram(voice_data)
            mia_speak(answer)
            entry.update({"answer": answer})
            addNewEntry(entry['question'], entry['answer'])
            readEntry(entry['question'])

if __name__ == "__main__":
    time.sleep(1)
    mia_speak('How can I help you?')
    while 1:
        voice_data = record_audio()
        respond(voice_data)





# print(voice_data)

#Setting up Speech to Text Service
# apikey = ''
# url = ''

# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# #Open Audio Source and Convert
# with op