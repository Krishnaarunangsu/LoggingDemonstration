import time
import calendar


time_duration:time = time.gmtime(0)
print(time_duration)
print(f'Time GM:{calendar.timegm(time.gmtime())}')
print(f'Time LGM:{time.localtime(time.time())}')


from time import time, ctime, struct_time
print(time())

t = time()
print(t)
print(ctime(t))

time_tuple = (2019, 4, 25, 17, 28, 12, 1, 57, 0)
time_obj = struct_time(time_tuple)
print(time_obj)


#  https://realpython.com/python-time-module/



