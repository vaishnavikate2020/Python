def Number(n):
          for i in range(n):
                    j=1
                    while j<=n:
                              print(j,end=" ")
                              j+=1
                    print("\n")

def main():
	x=(int(input("Enter the  number")))
	Number(x)

if __name__ == "__main__":
	main()