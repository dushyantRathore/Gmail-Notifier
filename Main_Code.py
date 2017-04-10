#!/usr/bin/python

import imaplib
import email
import notify2
from pickle_manipulations import get_EmailID,get_InboxID,get_Password,update_InboxID


def job():

    org_email = "@gmail.com"
    smtp_server = "imap.gmail.com"
    smtp_port = 993

    username = get_EmailID()
    password = get_Password()

    mail = imaplib.IMAP4_SSL(smtp_server)

    mail.login(username, password)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    pickle_ID = get_InboxID()
    first_id = int(id_list[0])
    last_id = int(id_list[-1])

    # print pickle_ID
    # print last_id

    diff = last_id - pickle_ID

    if diff == 0:
        message = "No new mails."

        print message

        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message)
        n.show()

    elif diff == 1:
        message = "You have 1 new mail "

        print message

        l = ""

        for i in range(last_id, pickle_ID, -1):
            typ, data = mail.fetch(i, '(RFC822)')

            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_string(response[1])
                    l += "-> " + msg['from'] + " - " + msg['subject'] + "\n"

        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message + "\n" + str(l))
        n.show()

        update_InboxID(last_id)

    else:
        message = "You have " + str(diff) + " new mails."

        print message

        l = ""

        for i in range(last_id, pickle_ID, -1):
            typ, data = mail.fetch(i, '(RFC822)')

            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_string(response[1])
                    l += "-> " + msg['from'] + " - " + msg['subject'] + "\n"

        notify2.init("Gmail Notifier")
        n = notify2.Notification("Gmail Inbox", message + "\n" + str(l))
        n.show()

        update_InboxID(last_id)

if __name__ == "__main__":
    job()


