import my_object

class MyDerivedObject(my_object.MyObject):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return self.greeting

    def set_greeting(self, newGreeting):
        self.greeting = newGreeting
