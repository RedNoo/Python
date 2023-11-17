import time
from time import time_ns

print(time.ctime(0))

print(time.time())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
print(time_object.tm_year)
print(time.strftime("%B %d.%m.%Y %H:%M:%S", time_object))

time_string = "20 April, 2020"
t_object = time.strptime(time_string, "%d %B, %Y")

print(t_object.tm_year)

time_tuple = (2023, 11, 17, 22, 1, 0, 0, 0, 0)
print(time.asctime(time_tuple))
