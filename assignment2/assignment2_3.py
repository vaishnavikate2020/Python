def Factorial(n):
          i=1
          while n>0:
                    i=i*n
                    n=n-1
          return i

def main():
    x=(int(input("Enter the number")))
    print("Factorial of ",x,"is",Factorial(x))
         
if __name__ == "__main__":
    main()

