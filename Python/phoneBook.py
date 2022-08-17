import os
def init():
    curDir = os.getcwd()
    #create a directory called contacts
    try:
        os.mkdir("contacts")
    except FileExistsError:
        print("Directory already exists")

    #create a file called contacts.txt inside the contacts directory
    try:
        contacts = open("contacts/contacts.txt","w")
        contacts.write("Name\tPhone\n")
    except:
        print("File already exists")
        contacts.close()

def addContact(name,phone):
    contacts = open("contacts/contacts.txt","a")
    contacts.write(name+"\t"+phone+"\n")
    contacts.close()

def searchByName(name):
    print("\nSearch by name")
    contacts = open("contacts/contacts.txt","r")
    for line in contacts:
        if name in line:
            print(line)
    contacts.close()

def searchByNumber(phone):
    print("\nSearch by phone number")
    contacts = open("contacts/contacts.txt","r")
    for line in contacts:
        if phone in line:
            print(line)
    contacts.close()

def deleteContactByName(name):
    print("\nDelete contact by name")
    contacts = open("contacts/contacts.txt","r")
    lines = contacts.readlines()
    contacts.close()
    contacts = open("contacts/contacts.txt","w")
    for line in lines:
        if name not in line:
            contacts.write(line)
    contacts.close()

def deleteContactByNumber(phone):
    print("\nDelete contact by phone number")
    contacts = open("contacts/contacts.txt","r")
    lines = contacts.readlines()
    contacts.close()
    contacts = open("contacts/contacts.txt","w")
    for line in lines:
        if phone not in line:
            contacts.write(line)
    contacts.close()

def listContacts():
    print("\nList all contacts")
    contacts = open("contacts/contacts.txt","r")
    print(contacts.readline())
    lines = contacts.readlines()
    lines.sort()
    for line in lines:
        print(line)
    contacts.close()



# qn1: create a directory called contacts
# init()

# qn2: add contacts
# addContact("John","12345")
# addContact("Mary","54321")
# addContact("Bob","98765")

# qn3: list all contacts
# listContacts()

# qn4: search by name
searchByName("John")

# qn5: search by phone number
searchByNumber("98765")

# qn6: delete contact by name
# deleteContactByName("John")
# listContacts()

# qn7: delete contact by phone number
# deleteContactByNumber("98765")
# listContacts()


