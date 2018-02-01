import time

print(time.gmtime(0))

time_here = time.localtime()
print(time_here)
print("Year: ", time_here.tm_year)
print("Day of Month", time_here.tm_mday)
current_time = print(time.time())
print ("time is - " + time.strftime("%X",time.localtime(current_time)))


time1 = time.perf_counter()
time.sleep(2)
print("Slept for 2 sec")
time2 = time.perf_counter()
print(time2-time1)

print ("The current timezone is {0} with offset of {1}".format(time.tzname[0],time.timezone))
print ("daylight - {0}".format(time.daylight!=0) )
