import threading
def NUM (func, lock):
    func (lock)

def evenlist(lock):
    lock.acquire()
    num = [int(x) for x in input("enter numbers").split()]
    sum=0
    num=list(num)
    for i in range(len(num)):
        if  num[i]%2==0:
            print("Even number",num[i])
            sum=sum+num[i]
    print("even",sum)
    lock.release()
def oddlist(lock):
    lock.acquire()
    num = [int(x) for x in input("enter numbers").split()]
    num = list(num)
    sum=0
    for i in range(len(num)):
        if num[i] % 2 != 0:
            print("Odd number",num[i])
            sum = sum + num[i]
    print("odd",sum)
    lock.release()
if __name__ == "__main__":
    print ("Inside main")
    lock = threading.Lock ()
    
    thread1 = threading.Thread(target=NUM, args=(evenlist,lock,))
    thread2 = threading.Thread(target=NUM, args=(oddlist,lock,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(" exit fom main.")
