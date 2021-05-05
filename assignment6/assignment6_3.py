class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
        print("Enter first number")
        self.value1=int(input())
        print("Enter second number")
        self.value2 = int(input())
    def Addition(self):
        return self.value1+self.value2
    def Subtraction(self):
        return self.value1-self.value2
    def multiplication(self):
        return self.value1*self.value2
    def division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()
    obj1.Accept()
    ret=obj1.Addition()                      #ret=add(obj1)
    print("Addition is",ret)
    ret=obj1.Subtraction()                      #ret=sub(obj1)
    print("Subtraction is",ret)
    ret=obj1.multiplication()
    print("Multiplication is",ret)
    ret=obj1.division()
    print("Division is",ret)
    
    obj2.Accept()
    ret=obj2.Addition()                      #ret=add(obj2)
    print("Addition is",ret)
    ret=obj2.Subtraction()                      #ret=sub(obj2)
    print("Subtraction is",ret)
    ret=obj2.multiplication()
    print("Multiplication is",ret)
    ret=obj2.division()
    print("Division is",ret)
    
if __name__ == "__main__":
	main()