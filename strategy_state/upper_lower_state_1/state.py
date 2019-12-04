from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def writeName(self,context, name):
        pass


class StateLowerCase(State):
    def writeName(self, context, name):
        print(name.lower())
        context.setState(StateUpperCase())


class StateUpperCase(State):

    def writeName(self, context, name):
        print(name.upper())
        context.setState(StateLowerCase())
