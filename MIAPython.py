from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("685542ea-039d-4fbb-a0f3-58372ca5e9da-bluemix", "i2yZ76A-jB0eXT0SGcvsfpjS3GH_-u_z2jAu_LtDZngP", connect=True)

databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

keywords={"time","today","yesterday","now","temperature"}

#break question into words
def makeWordArray(question):
    arr=question.split();
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
    'needsUpdate':containsKeywords
    }
    my_document = myDatabaseDemo.create_document(newEntry)
    if my_document.exists():
        print('SUCCESS!!')

def updateEntry(question, newAnswer):
    for document in myDatabaseDemo:
        if (document['question']==question):
            mydoc=document
            mydoc['question']=question
            mydoc['answer']=newAnswer
            mydoc['needsUpdate']=document['needsUpdate']
            mydoc.save()
            return 0
    print("Question not found in database")


def readEntry(question):
    for document in myDatabaseDemo:
        if (document['question'] == question):
            if(document['needsUpdate']):
                mydoc=document
                mydoc['question']=question
                mydoc['answer']="6:00pm"
                mydoc['needsUpdate']=document['needsUpdate']
                mydoc.save()
            print(document['answer'])
            return 0
    print("Answer not found in database")

addNewEntry("Is Pluto still a planet?","Yes, it is one one the nine planets")
addNewEntry("What NBA team has the most championships?","The Boston Celtics are currently have the most championships with 17")
addNewEntry("Whats the time right now in California?", "5:00pm")
readEntry("Whats the time right now in California?")

#UPDATE
updateEntry("Is Pluto still a planet?","no")

#DELETE
def deleteEntry(question):
    for document in myDatabaseDemo:
        if (document['question']== question):
            document.delete()
            return 0
    print("Question not found in database")

deleteEntry("Whats the time right now in California?")
