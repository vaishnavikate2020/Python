from arithmatic import * 
def main():
    
    print("Enter first number:")
    value1=int(input())
    
    print("Enter second number:")
    value2=int(input())
    
    ret1=addition(value1,value2)
    ret2=subtraction(value1,value2)
    ret3=multiplication(value1,value2)
    ret4=division(value1,value2)
    
    print("Addition is",ret1)
    print("Subtraction is",ret2)
    print("Multiplication is",ret3)
    print("Division is",ret4)
    
if __name__ = "__main__":
    main()

