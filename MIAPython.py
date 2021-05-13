from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


client = Cloudant.iam("dcc9e7a6-300c-48bc-a169-3b153750d14a-bluemix", "ok15p-S7RlG8WsXUDBKLVFyWPtzneRXP8kshX1eRjWUx", connect=True)

# databaseName = "databasedemo"
databaseName = 'hisdb'
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

keywords={"time","today","yesterday","now","temperature"}

#break question into words
def makeWordArray(question):
    arr=question.split()
    return arr

#CREATE
def addNewEntry(question,answer):
    wordArray=makeWordArray(question)
    containsKeywords=False
    for i in wordArray:
        if(i.lower() in keywords):
            containsKeywords=True
    newEntry={
    'question': question,
    'answer': answer,
    'needsUpdate':containsKeywords,
    'frequency': 1
    }
    my_document = myDatabaseDemo.create_document(newEntry)
    if my_document.exists():
        print('SUCCESS!!')


#UPDATE
def updateEntry(question, newAnswer):
    for document in myDatabaseDemo: #Searches the collection for the matching question
        if (document['question']==question): 
            mydoc=document
            mydoc['question']=question
            mydoc['answer']=newAnswer
            mydoc['needsUpdate']=document['needsUpdate'] #Can this be left out?
            mydoc['frequency']=document['frequency'] + 1
            mydoc.save()
            return 0
    print("Question not found in database")

# If it exists?

# def existing_question(question):
#     for document in myDatabaseDemo: 
#         print(document['question'])
#         if (document['question'] == question):
#             if(document['needsUpdate']):
#                 return True
#                 break
#             else:
#                 return False

# def needs_update(question):
#     for document in myDatabaseDemo: 
#         if (document['question'] == question):
#             if(document['needsUpdate']):
#                 return True
#                 break

def existing_question(question):
    for document in myDatabaseDemo:
        if (document['question'] == question):
            return True
    return False

# READ
def readEntry(question):
    for document in myDatabaseDemo:
        if (document['question'] == question):
            # if(document['needsUpdate']):
            #     mydoc=document
            #     mydoc['question']=question
            #     mydoc['answer']="6:00pm"
            #     mydoc['needsUpdate']=document['needsUpdate']
            #     mydoc['frequency']=document['frequency'] + 1
            #     mydoc.save()
            #     print(document['answer'])
            #     return 0
            print(document['answer'])
            mydoc=document
            mydoc['question']=question
            mydoc['answer']=document['answer']
            mydoc['needsUpdate']=document['needsUpdate']
            mydoc['frequency']=document['frequency']
            mydoc.save()
            return 0
    print("Answer not found in database")


# #READ
# def readEntry(question):
#     for document in myDatabaseDemo:
#         if (document['question'] == question):
#             if(document['needsUpdate']):
#                 mydoc=document
#                 mydoc['question']=question
#                 mydoc['answer']="6:00pm"
#                 mydoc['needsUpdate']=document['needsUpdate']
#                 mydoc['frequency']=document['frequency'] + 1
#                 mydoc.save()
#                 print(document['answer'])
#                 return 0
#             print(document['answer'])
#             mydoc=document
#             mydoc['question']=question
#             mydoc['answer']=document['answer']
#             mydoc['needsUpdate']=document['needsUpdate']
#             mydoc['frequency']=document['frequency'] + 1
#             mydoc.save()
#             return 0
#     print("Answer not found in database")

# addNewEntry("Is Pluto still a planet?","Yes, it is one one the nine planets")
# addNewEntry("What NBA team has the most championships?","The Boston Celtics are currently have the most championships with 17")
# addNewEntry("Whats the time right now in California?", "5:00pm")
# readEntry("Whats the time it")


# updateEntry("Is Pluto still a planet?","no")

#DELETE
def deleteEntry(question):
    for document in myDatabaseDemo:
        if (document['question']== question):
            document.delete()
            return 0
    print("Question not found in database")

#FREQUECY
def mostFrequent():
    mydoc=None
    max=0
    for document in myDatabaseDemo:
        if document['frequency'] > max:
            max=document['frequency']
            mydoc=document
    # print(mydoc['question'])
    # return mydoc
    return mydoc['question']

# mostFrequent()