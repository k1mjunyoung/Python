class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def avg(self):
        result = (self.first + self.second)/2
        return result

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number1: "))

cal1 = Calculator(num1, num2)

print(cal1.sum())
print(cal1.mul())
print(cal1.sub())
print(cal1.div())
print(cal1.avg())
