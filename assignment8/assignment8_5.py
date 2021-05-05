import threading
def NUM(func, lock):
    func (lock)

def ANUM(lock):
    lock.acquire()
    for i in range(51):
        print(i)
    lock.release()
def RNUM(lock):
    print("Reverse Order:")
    lock.acquire()
    for i in range(50,-1,-1):
        
        print(i)
    lock.release()
    
if __name__ == "__main__":
    lock = threading.Lock ()
    thread1 = threading.Thread(target=NUM, args=(ANUM,lock,))
    thread2 = threading.Thread(target=NUM, args=(RNUM,lock,))
    thread1.start()
    thread1.join()
    thread2.start()