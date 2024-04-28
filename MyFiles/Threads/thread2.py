# see the IDs and thread's name
import threading
import os


def task1():
    print(f"Task1 assigned to thread: {threading.current_thread().name}")
    print(f"ID of Process running task1: {os.getpid()}")


def task2():
    print(f"Task 2 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task2: {os.getpid()}")


if __name__ == "__main__":
    print(f"ID of Process running in main Program: {os.getpid()}")
    print(f"Main thread's name: {threading.current_thread().name}")

    t1 = threading.Thread(target=task1, name="thread1")
    t2 = threading.Thread(target=task2, name="thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("End")
