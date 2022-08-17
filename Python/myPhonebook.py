from xml.etree.ElementInclude import include


import os

def init():
    try:
        os.mkdir("contactX")
    except FileExistsError:
        print("Directory already exists")

    try:
        contacts =open('contactX/contact.txt','w')
        contacts.write('Name\tPhone\n')
        contacts.close()
    except FileExistsError:
        print("File already exists")

def addContact(name,phone):
    contacts =open('contactX/contact.txt','a')
    contacts.write(name+'\t'+phone+'\n')
    contacts.close()

def searchByName(name):
    contacts =open('contactX/contact.txt','r')
    for line in contacts:
        if name in  line:
            print(line)
    contacts.close()

def searchByNumber(number):
    contacts =open('contactX/contact.txt','r')
    for line in contacts:
        if number in  line:
            print(line)
    contacts.close()

def listAll():
    contacts =open('contactX/contact.txt','r')
   


# init()

# addContact('Joel','12345')
# addContact('JJ','56465')
# addContact('John','79564')
# addContact('James','542321')

# searchByName('JJ')

# searchByNumber('12345')


