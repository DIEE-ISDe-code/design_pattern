#class StateLowerCase(State):
def writeNameLower(printer, name):
    print(name.lower())
    printer.setState(writeNameUpper)


# class StateUpperCase(State):
def writeNameUpper(printer, name):
    print(name.upper())
    printer.setState(writeNameLower)



