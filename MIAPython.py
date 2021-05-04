from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


client = Cloudant.iam("dcc9e7a6-300c-48bc-a169-3b153750d14a-bluemix", "ok15p-S7RlG8WsXUDBKLVFyWPtzneRXP8kshX1eRjWUx", connect=True)

databaseName = "mia-db"
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

# addNewEntry("How old is Joe Biden?","78")
# addNewEntry("Whats the mascot for SJSU?","Sammy the Spartan")
# addNewEntry("Who is the CEO of Apple?","Tim Cook")
# addNewEntry("How many cups are in a gallon?","16")
# addNewEntry("What is the unit conversion from pounds to kilograms?","One pound is 2.2 kilograms")
# addNewEntry("How much sugar is in a can of coke?","39 grams of sugar")
# addNewEntry("Is the United States more populated than Russia?","Yes, the United States has approximately 330 million people while Russia has approximately 145 million.")
# addNewEntry("Whats Standford University's Acceptance Rate?","4.3%")
# addNewEntry("Is Pluto still a planet?","No, it was deemed a dwarf planet in 2006")
# addNewEntry("What NBA team has the most championships?","The LA Lakers and the Boston Celtics are currently tied for the most championships with 17 each. ")

#READ
def readEntry(question):
    for document in myDatabaseDemo:
        if (document['question']==question):
            print(document['answer'])
            return 0

    print("Answer not found in database")

# readEntry("How old is Joe Biden?")
# readEntry("Whats the mascot for SJSU?")
# readEntry("Who is the CEO of Apple?")
# readEntry("How many cups are in a gallon?")
# readEntry("What is the unit conversion from pounds to kilograms?")
# readEntry("How much sugar is in a can of coke?")
# readEntry("Is the United States more populated than Russia?")
# readEntry("Whats Standford University's Acceptance Rate?")
# readEntry("Is Pluto still a planet?")
# readEntry("What NBA team has the most championships?")
