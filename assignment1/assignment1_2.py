def chknum(v):
    if(v%2)==0:
        print("{} number is even".format(v))
    else:
        print("{} number is odd".format(v))
def main():
    num=(int(input("Enter any number")))
    chknum(num)

if __name__ == "__main__":
    main()