import state as st
class Printer():

    def __init__(self):
        # self.state = StateLowerCase()
        self.w = st.writeNameLower

    def setState(self, newState):
        # self.state = newState
        self.w = newState

    def writeName(self, name):
        #self.state.writeName(self, name)
        self.w(self,name)





