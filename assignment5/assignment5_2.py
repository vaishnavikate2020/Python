def count(N, n=1):
    global N,n
    print(n)
    if n < N:
        count(N, n + 1)


def main():
    print("Enter the number of till you want to print numbers:")
    value = int(input())
    count(value)
if __name__ == "__main__":
	main()
