import smtplib
import imaplib
import email
import pickle


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Initialisation Function


def startup():

    org_email = "@gmail.com"
    smtp_server = "imap.gmail.com"
    smtp_port = 993

    username = raw_input(color.BOLD + color.CYAN + "Enter username : " + color.END)
    password = raw_input(color.BOLD + color.CYAN + "Enter password : " + color.END)

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
    startup()
