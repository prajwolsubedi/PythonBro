# CALCULATE EXECUTION TIME IN PYTHON

import time

start_time = time.perf_counter()



#Your code goes here
for i in range(100000000):
    pass


end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"The elapsed time is {elapsed_time:1f} seconds")