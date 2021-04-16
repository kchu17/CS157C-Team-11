from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("685542ea-039d-4fbb-a0f3-58372ca5e9da-bluemix", "J_VIN6hP17Zu5r4rUUGesjutWnRPrbie9BT1Z4O-Unvj", connect=True)

databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
 print("'{0}' successfully created.\n".format(databaseName))

#CREATE
def addNewEntry(question,answer):
    newEntry={
    'question': question,
    'answer': answer,
    }
    my_document = myDatabaseDemo.create_document(newEntry)
    if my_document.exists():
        print('SUCCESS!!')

addNewEntry("How old is Roshan?","3")
addNewEntry("How ugly is Roshan?","10")

#READ
def readEntry(question):
    for document in myDatabaseDemo:
        if (document['question']==question):
            print(document['answer'])
            return 0

    print("Answer not found in database")

readEntry("How old is Roshan?")
readEntry("How smart is Roshan?")
