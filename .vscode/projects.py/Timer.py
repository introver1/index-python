# Creating an Alarm Clock
import time
my_time = int(input("Enter the time in seconds: "))
# for l in range (0, my_time):
#     print(l)
#     time.sleep(1)

#  for reversed count
for l in range (my_time, 0, -1):
    seconds = l % 60
    minutes = int(l/60)%60
    hours = int(l/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("TIME'S UP")