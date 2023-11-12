import time
from datetime import datetime


time_1 = datetime.now()
time.sleep(1)
time_2 = datetime.now()

print(time_1 == time_2)

print(time_1)
print(time_2)