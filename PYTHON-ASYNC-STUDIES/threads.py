import threading
import time

# def new():
#     while True():
#         time.sleep(1)
#         print("THIS IS A NEW FUNCTION")


# def second():
#     while True:
#         time.sleep(0.8)
#         print("HELLO THIS IS THE SECOND")

# threading.Thread(target=new).start()
# threading.Thread(target=second).start()


# -------------

counter = 0

def function1():
    global counter

    while True:
        counter += 1
        counter -= 1


def function2():
    global counter
    
    while True:
        counter += 1
        counter -= 1


threading.Thread(target=function1).start()
threading.Thread(target=function2).start()