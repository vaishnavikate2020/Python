def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))

#print(factorial(n))
def main():
    n = int(input("Enter number:"))
    print("Factorial is:",factorial(n))


if __name__ == "__main__":
	main()