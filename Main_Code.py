#!/usr/bin/python2.7

import time
import schedule
import smtplib
import imaplib
import email
import pickle
import notify2
import pandas
from pickle_manipulations import get_ID, update_ID

def job():

    org_email = "@gmail.com"
    smtp_server = "imap.gmail.com"
    smtp_port = 993

    # username = raw_input("Enter username : ")
    # password = raw_input("Enter password : ")

    username = "username"
    password = "password"

    mail = imaplib.IMAP4_SSL(smtp_server)

    mail.login(username, password)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    pickle_ID = get_ID()
    first_id = int(id_list[0])
    last_id = int(id_list[-1])

    # print pickle_ID
    # print last_id

    diff = last_id - pickle_ID

    if diff == 0:
        message = "No new mails."
        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message)
        n.show()

        print message

    elif diff == 1:
        message = "You have 1 new mail "

        l = []

        for i in range(last_id, pickle_ID, -1):
            typ, data = mail.fetch(i, '(RFC822)')

            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_string(response[1])
                    l.append(msg['from'] + " - " + msg['subject'])

        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message + "\n" + str(l))
        n.show()

        update_ID(last_id)

        print str(l)

    else:
        message = "You have " + str(diff) + " new mails."

        l = []

        for i in range(last_id, pickle_ID, -1):
            typ, data = mail.fetch(i, '(RFC822)')

            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_string(response[1])
                    l.append(msg['from'] + " - " + msg['subject'])

        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message + "\n" + str(l))
        n.show()

        print str(l)

        update_ID(last_id)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

