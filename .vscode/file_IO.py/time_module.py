import time
# print(time.time())

# for i in range(5):
#     time.sleep(1)
#     print(i)



t = time.localtime()
formatted_time=time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(formatted_time)