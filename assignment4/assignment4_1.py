power= lambda no1 : no1**2


def main():
    value1=int(input("Please enter number:"))
    ret = power(value1)
    print("{} raised to 2 is {}".format(value1,ret))

if __name__=='__main__':
    main();