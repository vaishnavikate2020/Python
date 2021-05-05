def Factorial_Add(x):
          i=1
          sum=0
          while x>i:
                    if x%i==0:
                              sum=sum+i
                    i=i+1
          return sum
		  
def main():
	x=(int(input("Enter the  number")))
	print("Sum is",+Factorial_Add(x))               

if __name__ =="__main__":
	main()
