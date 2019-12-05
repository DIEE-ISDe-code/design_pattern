from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def writeChar(self,printer, name):
        pass


class StateLowerCase_0(State):
    def writeChar(self, printer, name):
        print(name.lower())
        if name.lower()=='a':
            print('CHANGE 0->1')
            printer.setState(StateLowerCase_1())
            
class StateLowerCase_1(State):
    def writeChar(self, printer, name):
        print(name.lower())
        if name.lower()=='b':
            print('CHANGE 1->2')
            printer.setState(StateLowerCase_2())
        elif name.lower()=='a':
            print('remain in state 1')
            print('STAY 1->1')
            printer.setState(StateLowerCase_1())
        else:            
            print('CHANGE 1->0')
            printer.setState(StateLowerCase_0())
            
class StateLowerCase_2(State):
    def writeChar(self, printer, name):
        print(name.lower())
        if name.lower()=='c':
            print('CHANGE 1->UPPER')
            printer.setState(StateUpperCase())
        else:
            print('CHANGE 1->0')
            printer.setState(StateLowerCase_0())
            
            
class StateUpperCase(State):

    def writeChar(self, printer, name):
        print(name.upper())
        if name.lower()=='x':
            printer.setState(StateLowerCase_0())
