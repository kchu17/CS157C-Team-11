import speech_recognition as sr
import playsound
import os
from time import ctime
import random
import time
from speech_to_text import mia_speak
# from MIAPython import readEntry, existing_question, updateEntry, addNewEntry
import wolframalpha
from flask import Flask, request, url_for, session
from twilio.twiml.voice_response import VoiceResponse, Record, Gather

# client = wolframalpha.Client('2E922Y-48JVAHYP2H')


# while True:
#     query = str(input('Query: '))
#     res = client.query(query)
#     output = next(res.results).text
#     print(output)


# question = 'who is the 43rd President of the United States'
# question2 = 'what is the time'
# question3 = 'who are you'
# answer1 = 'George W. Bush (from January 20, 2001 to January 20, 2009)'
# answer2 = 'Barrack Obama'

# print(existing_question(question))
# x = ctime()
# print(type(x))
# print(x)
# arr=x.split()
# print(arr)

# def func(*args):
#     # *args means for however many arguments you take in, it will catch them all
#     print(args[0])
#     # for arg in args:
#     #     print(arg)
#     print(len(args))
# l = [11,3,4,5,"tuts"]
 
# print(func(*l))
def concatenate(**words):
    print(words.get('a'))
    print(words.keys())
    # print(words.values()[0])
    # result = ""
    # for arg in words.values():
    #     result += arg
    # return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))



# print(existing_question(question3))


# if existing_question(question) == True:
#     updateEntry(question, answer1)
#     readEntry(question)
# else:
#     addNewEntry(question, answer2)
#     readEntry(answer1)


# x = existing_question('what is the time')
# if(x == True):
#     print('success')
# else:
#     print('failure')
# app = Flask(__name__)

# r = sr.Recognizer()
# #Theories to test out
# # OS operates in call?
# # Microphone operates in call?

# @app.route("/", methods=['POST', 'GET'])
# # def hello_call():
# #     """Respond to incoming phone calls with a brief message."""
# #     # Start our TwiML response
# #     resp = VoiceResponse()

# #     string = 'Hello World Hello World'

# #     # Read a message aloud to the caller
# #     resp.say(string, voice='alice')
# #     resp.say("Therefore I like you", voice='alice')

# #     return str(resp)

# def reply():

#     # response = VoiceResponse()
#     # gather = Gather(input='speech', action='/completed')
#     # gather.say('Welcome to Twilio, please tell us why you\'re calling')
#     # x = response.append(gather)
#     # print(type(x))
#     # print(x)
#     # return (str(x))
#     response = VoiceResponse()
#     response.say("Hello, Please leave a message")
#     response.record()
#     print(str(response))
#     return str(response)

# if __name__ == "__main__":
#     app.run(debug=True)