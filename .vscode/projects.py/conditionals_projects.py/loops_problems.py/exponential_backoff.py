# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
wait_time=1
max_retries=5
attempts=1
while attempts<=max_retries:
    print("Attempts",attempts,"-wait time", wait_time)
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2