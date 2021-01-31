import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def getInfo():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def sendEmail(receiver , subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('joshiyash436@gmail.com', 'Yash@12345')
    email = EmailMessage()
    email['From'] = 'joshiyash436@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Email sent Succesfully')
    talk('Do you want to send more emails')
    again = getInfo()
    if 'yes' in again:
        getEmailInfo()
    else:
        exit()

email_list = {
    'black':'joshiyash919@gmail.com'
}


def getEmailInfo():
    talk("To whom you want to send email ?")
    name = getInfo()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of your email ?")
    subject = getInfo()
    talk("Tell me the email")
    message = getInfo()

    sendEmail(receiver,subject,message)


getEmailInfo()
