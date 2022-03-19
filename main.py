import app as app
while True:
    #talk('Hello Ankush, How may I help you')
    app.talk ('welocome to ABC bank, Tell me your secret phrase')
    option = app.bank_options()
    app.bank_action(option)