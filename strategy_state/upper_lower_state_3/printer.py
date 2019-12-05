import state as st

class Printer(): # THIS IS THE 'CONTEXT'

    def __init__(self):
        self.state = st.StateLowerCase_0()

    def setState(self, newState):
        self.state=newState

    def writeChar(self, name):
        self.state.writeChar(self, name)
