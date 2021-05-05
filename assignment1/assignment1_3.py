def Add(value1,value2):
	sum= value1 + value2
	return sum
    
def main():
	num1=(int(input("Enter first number")))
	num2=(int(input("Enter second number")))
	sum=Add(num1,num2)
	print("Addition of {0} and {1} is {2}".format(num1,num2,sum))


if __name__ == "__main__":
	main()