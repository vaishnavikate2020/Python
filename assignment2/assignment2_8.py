def Printpattern(n):
          for i in range(n):
                    j=1
                    while j<=i+1:
                              print(j,end=" ")
                              j+=1
                    print("\n")
def main():
	x=(int(input("Enter the  number")))
	Printpattern(x)

if __name__ == "__main__":
	main()