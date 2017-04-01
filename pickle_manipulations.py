import pickle

# Get details from the pickle file


def get_EmailID():
    fileobject = open('EmailID.txt', 'r')
    EmailID = pickle.load(fileobject)
    return EmailID


def get_Password():
    fileobject = open('Password.txt', 'r')
    Password = pickle.load(fileobject)
    return Password


def get_InboxID():
    fileobject = open('InboxID.txt', 'r')
    pickle_ID = pickle.load(fileobject)
    return pickle_ID

# Update the value in pickle file


def update_InboxID(val):
    fileobject = open("InboxID.txt", 'wb')
    pickle.dump(val, fileobject)
    fileobject.close()
