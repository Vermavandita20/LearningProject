class Hello:
    def __init__(self, name):
        self.name=name

    def say_hello(self):
        """this function will say hello"""
        return f"Hello,{self.name}!"
value= input('Enter name')
greeting = Hello(value)

print(greeting.say_hello())
print(len(greeting.say_hello()))
