import state as st

class Printer(): # THIS IS THE 'CONTEXT'

    def __init__(self):
        self.state = st.StateLowerCase()

    def setState(self, newState):
        self.state=newState

    def writeName(self, name):
        self.state.writeName(self, name)
