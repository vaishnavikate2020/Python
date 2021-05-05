def displayr(no):
    if no !=0:          #recursive call
        print("",no)
        no= no -1
        displayr(no)

def main():
    print("Enter the number of times you want to print *")
    value = int(input())
    displayr(value)
if __name__ == "__main__":
	main()
