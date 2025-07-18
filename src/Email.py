# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Import the email modules we'll need
from email.message import EmailMessage
class Email:
    def __init__(self, Sender, Receiver, password, Message=None, Subject=None):
        self.sender = Sender
        self.receiver = Receiver
        self.password = password
        self.subject = Subject
        self.message = Message
    def get_password(self):
        return self.password
    def get_sender(self):
        return self.sender
    def get_receiver(self):
        return self.receiver
    def get_subject(self):
        return self.subject
    def get_message(self):
        return self.message
    def set_sender(self, sender):
        self.sender = sender
    def set_receiver(self, receiver):
        self.receiver = receiver
    def set_subject(self, subject):
        self.subject = subject
    def set_message(self, message):
        self.message = message
    def write_email(self):
        msg = MIMEMultipart()
        if self.subject == None:
            self.set_subject("Notification for website diff")
        
        msg['Subject'] = self.get_subject()
        msg['From'] = self.get_sender()
        msg['To'] = self.get_receiver()
        msg.attach(MIMEText(self.get_message(), "plain"))
        self.send_email(msg)
    def send_email(self, msg):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.get_sender(), self.get_password())
                text = msg.as_string()
                server.sendmail(self.get_sender(), self.get_receiver(), text)
                print("Email sent successfully")
        except:
            print("Error: Unable to send email")