def Number(n):
                    j=0
                    while n>0:
                              j+=n%10
                              n=n//10
                    return j

def main():
    x=(int(input("Enter the number")))
    y=Number(x)
    print("Number of digit=",+y)

if __name__ == "__main__":
	main()