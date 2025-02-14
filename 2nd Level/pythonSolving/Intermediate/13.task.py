class Greet:
    def __init__(self,name,name2):
        self.name = name
        self.name2 = name2
        print(name)
        print(name2)
    def __del__(self):
        print("Destructor called, HUHU ")


names = Greet("Mike","Debie")
del names
