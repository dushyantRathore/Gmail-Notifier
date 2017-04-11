import smtplib
import imaplib
import email
import pickle
from Tkinter import *


# Initialisation Function


class initialise():

    def __init__(self):
        self.root = Tk()
        self.root.title("Gmail Notifier")
        self.mainframe = Frame(self.root, padx=10, pady=10)
        self.label1 = Label(self.mainframe, text="Enter your username : ")
        self.label1.config(font=("Arial", 18))
        self.entry1 = Entry(self.mainframe, width=25)
        self.entry1.config(font=("Arial", 18))
        self.label2 = Label(self.mainframe, text="Enter your password : ")
        self.label2.config(font=("Arial", 18))
        self.entry2 = Entry(self.mainframe, width=25)
        self.entry2.config(font=("Arial", 18))

        self.button1 = Button(self.mainframe, text="Register", command=self.register)
        self.button1.config(font=("Arial", 18))

        # Grid Packing

        self.label1.grid(row=0, sticky=E)
        self.entry1.grid(row=0, column=1)
        self.label2.grid(row=1, sticky=E)
        self.entry2.grid(row=1,column=1)
        self.button1.grid(row=2,column=0,columnspan=2)

        self.mainframe.pack()

        self.root.mainloop()

    def register(self):

        username = self.entry1.get()
        password = self.entry2.get()

        # print username
        # print password

        org_email = "@gmail.com"
        smtp_server = "imap.gmail.com"
        smtp_port = 993

        mail = imaplib.IMAP4_SSL(smtp_server)

        mail.login(username, password)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        first_id = int(id_list[0])
        last_id = int(id_list[-1])

        fileobject1 = open('EmailID.txt', 'w')
        pickle.dump(username, fileobject1)

        fileobject2 = open('Password.txt', 'w')
        pickle.dump(password, fileobject2)

        fileobject3 = open('InboxID.txt', 'w')
        pickle.dump(last_id, fileobject3)

if __name__ == "__main__":
    initialise()
