import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'abc' in command:
                command = command.replace('abc', '')
                print(command)
    except:
        pass
    return command

def login(secretpass):
    flag= 0
    if 'caterpillars are flying' in secretpass:
        talk("Login successful")
        flag=1
    else:
        talk ('Sorry Incorrect Password')
    return flag


def bank_options():
    command = take_command()
    print(command)
    valLogin = login(command)
    if valLogin == 1:
        talk ('How may I help you, tell me option number ')
        talk ('1) check current balance')
        talk ('2) change password')
        talk ('3) send money')
        option = take_command()
        print (option)
    else:
        option = ''
    return option

def send_money():
    talk ('Welcome to money transfer')
    talk ('To whom you want to send money ')
    receiver = take_command()
    print (receiver)
    if 'thomas' in receiver:
        talk ('how much money you want to transfer to Thomas')
        money = take_command()
        print (money)
        talk ('Money to be transfer '+ money + ' Please confirmed')
        confirmation = take_command()
        print (confirmation)
        if 'confirm' in confirmation:
            talk ('Tell me you most secrete phrase to transfer money')
            tphrase = take_command()
            print (tphrase)
            if tphrase == 'transfer money':
                talk (''+money+'   sent to thomas')
                talk ('Transaction Completed thanks for banking with us')
            else :
                talk ('incorrect phrase please try again')
        else :
            talk ('Confirmation not given')
            talk ('Cancelling transaction')
    else:
        talk ('Receiver not found')

def bank_action(option):
    if option == '1':
        talk ('Current balance is 1056420 rupees')
    elif option == '3':
        smoney = send_money()
    elif option == '':
        talk ('Say correct option or Option not given')
    else:
        talk ('Say correct option')

    
    

while True:
    #talk('Hello Ankush, How may I help you')
    talk ('welocome to ABC bank, Tell me your secret phrase')
    option = bank_options()
    bank_action(option)