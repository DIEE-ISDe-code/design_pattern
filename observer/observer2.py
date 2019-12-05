
# observer2.py  

# The Observer
class SubscriberOne:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print( self.name,' received the message ', message)

# The Observer
class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print( self.name,' received the message ', message)



# The Observable
class Publisher:
    def __init__(self):
        self.subscribers = dict() # set()
        # subscribers is a dictionary.
        #  key: anObserver
        #  value: the 'update' method or others.
    def register(self, anObserver, callback=None):
        if callback==None:
            # call the 'default' method
            callback=getattr(anObserver,'update')
        self.subscribers[anObserver]=callback


    def unregister(self, anObserver):
        del self.subscribers[anObserver]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            # returns all "key, value" couples
            callback(message)



# driver

publisher=Publisher()

bob=SubscriberOne('Bob') #has update() method
alice=SubscriberOne('Alice') #has update() method
john=SubscriberTwo('John') #has **receive()** method

publisher.register(bob, bob.update)     # explicitly uses the 'update()' method
publisher.register(alice)               # implicitly uses the 'update()' method
publisher.register(john, john.receive)  # explicitly uses the 'receive()' method


# send a message
publisher.dispatch('Lunchtime!')
publisher.unregister(john)
publisher.dispatch('Happy hour!')
