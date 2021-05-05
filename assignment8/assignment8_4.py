import threading
def STR (func, lock):
    func (lock)

def small(lock):
    lock.acquire()
    str=input("enter values")
    low=[c for c in str if c.islower()]
    print("Count of small letters",len(low))
    lock.release()
    
def capital(lock):
    lock.acquire()
    str=input("enter values")
    cap=[c for c in str if c.isupper()]
    print("Count of capital letters",len(cap))
    lock.release()
    
def digit(lock):
    lock.acquire()
    str=input("enter values")
    cnt=0
    for i in range(0,len(str)):
        if str[i].isdigit():
            cnt+=1

    print("Count of digit:",cnt)
    lock.release()
if __name__ == "__main__":
    lock = threading.Lock ()

    thread1 = threading.Thread(target=STR, args=(small,lock,))
    thread2 = threading.Thread(target=STR, args=(capital,lock,))
    thread3 = threading.Thread(target=STR, args=(digit,lock,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
