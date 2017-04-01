import smtplib
import imaplib
import email
import pickle

# Initialisation Function


def startup():

    org_email = "@gmail.com"
    smtp_server = "imap.gmail.com"
    smtp_port = 993

    username = raw_input("Enter username : ")
    password = raw_input("Enter password : ")

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


startup()
