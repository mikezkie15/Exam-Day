class Calculate:
    def __init__(self):
        self.num1 = None
        self.num2 = None
    def getInput(self):
        self.num1 = int(input("Enter your first number: "))
        self.num2 = int(input("Enter the second number: "))
    def add(self):
        add = self.num1 + self.num2
        print(add)
class Arthemitic(Calculate):
    def __init__(self):
        super().__init__(self)
add = Arthemitic()
add.getInput()
add.add()