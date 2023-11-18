import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("you drank cofee")


def study():
    time.sleep(5)
    print("you finish study")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.activeCount())
print(threading.enumerate())
print(time.perf_counter())
