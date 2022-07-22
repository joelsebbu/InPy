#create a dictionary phonebook with keys as names and values as phone numbers
phoneBook = {"jane": "12345", "john": "67890", "anne": "12346"}

#create function to add a new entry to the phonebook
def addEntry(name, number):
    phoneBook[name] = number
    print("Entry added")
    print(phoneBook)

#function to search for a name in the phonebook
def searchName(name):
    if name in phoneBook:
        print("Found")
        print(phoneBook[name])
    else:
        print("Not found")

#function to list all the names and numbers in the phonebook
def listAll():
    for name in phoneBook:
        print(name)
        print(phoneBook[name])
        print("\n")
#function to delete a name from the phonebook
def deleteName(name):
    if name in phoneBook:
        del phoneBook[name]
        print("Entry deleted")
        print(phoneBook)
    else:
        print("Not found")

#function to search by number
def searchNumber(number):
    for name in phoneBook:
        if phoneBook[name] == number:
            print(name)
            print(phoneBook[name])
            print("\n")
            break
    else:
        print("Not found")

addEntry("joe", "12347")
searchName("joe")
listAll()
deleteName("joe")
searchNumber("12346")