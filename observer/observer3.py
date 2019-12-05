
# observer3.py  (Python 3)

# The Observer
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print( self.name,' received the message ', message)

# The Observable
class Publisher:
    def __init__(self, events):
        # The constructor accepts in input a list of events
        # __init__ uses this list to initialize a dictionary
        self.subscribers = { event: dict() for event in events}

    def get_subscribers(self, event): #helper method
        return self.subscribers[event]

    def register(self, event, anObserver, callback=None):
        if callback==None:
            # set the callback to the update method
            callback=getattr(anObserver,'update')
        self.get_subscribers(event)[anObserver]=callback

    def unregister(self, event, anObserver):
        del self.get_subscribers(event)[anObserver]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            # returns all "key, value" couples FOR THE DICTIONARY RELATED TO THIS EVENT
            callback(message)


# driver

# possible events are ('lunch', 'happyhour')
publisher=Publisher(['lunch', 'happyhour'])

bob=Subscriber('Bob')
alice=Subscriber('Alice')
john=Subscriber('John')

# bob and john are intrested in the event 'lunch'
publisher.register('lunch', bob )
publisher.register('lunch', john )

# alice and john are intrested in the event 'happyhour'
publisher.register('happyhour', alice )
publisher.register('happyhour', john )


# send a message
print ('\nLUNCHTIME!')
publisher.dispatch('lunch','Lunchtime!') #event, message
print ('\nHAPPYHOUR!')
publisher.dispatch('happyhour','HAPPY HOUR!') #event, message


print("\nNow  john is no longer interested in event 'happyhour'")
print("but he remains interested in event 'lunch'\n")

publisher.unregister('happyhour',john)


# send a message
print ('\nLUNCHTIME!')
publisher.dispatch('lunch','Lunchtime!') #event, message
print ('\nHAPPYHOUR!')
publisher.dispatch('happyhour','HAPPY HOUR!') #event, message
