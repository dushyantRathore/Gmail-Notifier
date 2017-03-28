import pickle

# Get details from the pickle file


def get_ID():
    fileobject = open('/home/dushyant/Desktop/Github/Gmail-Notifier/ID.txt', 'r')
    pickle_ID = pickle.load(fileobject)
    return pickle_ID

# Update the value in pickle file


def update_ID(val):
    fileobject = open("/home/dushyant/Desktop/Github/Gmail-Notifier/ID.txt", 'wb')
    pickle.dump(val, fileobject)
    fileobject.close()
