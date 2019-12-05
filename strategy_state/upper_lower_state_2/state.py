from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def writeName(self,printer, name):
        pass


class StateLowerCase(State):
    def writeName(self, printer, name):
        print(name.lower())
        printer.setState(StateUpperCase1())


class StateUpperCase1(State):
    def writeName(self, printer, name):
        print(name.upper())
        printer.setState(StateUpperCase2())

class StateUpperCase2(State):
    def writeName(self, printer, name):
        print(name.upper())
        printer.setState(StateLowerCase())
