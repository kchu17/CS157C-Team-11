from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("685542ea-039d-4fbb-a0f3-58372ca5e9da-bluemix", "J_VIN6hP17Zu5r4rUUGesjutWnRPrbie9BT1Z4O-Unvj", connect=True)

databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
 print("'{0}' successfully created.\n".format(databaseName))

#CREATE
def addNewAnswer(question,answer):
    newEntry={
    'question': question,
    'answer': answer,
    }
    my_document = myDatabaseDemo.create_document(newEntry)
    if my_document.exists():
        print('SUCCESS!!')

addNewAnswer("How old is Roshan?","3")
addNewAnswer("How ugly is Roshan?","10")

#READ
