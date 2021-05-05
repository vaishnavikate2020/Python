def cheknum(num):
	if num > 0:
		print("{0} is positive".format(num))
	elif num < 0:
		print("{0} is negative".format(num))
	elif num ==0:
		print("ZERO you entered...")

def main():
	num=(int(input("Enter any number")))
	cheknum(num)

if __name__ == "__main__":
	main()