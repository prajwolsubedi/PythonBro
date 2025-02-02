# multithreading = Used to perform multiple tasks concurrently (multitasking)
#  Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(name):
    time.sleep(8)
    print(f"You finish walking the {name}.")

def take_out_trash():
   time.sleep(2)
   print("You take out the trash")

def get_mail():
   time.sleep(4)
   print("You get the mail")

thread1 = threading.Thread(target=walk_dog, args=("Entertainment",))
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

thread1.join()
thread2.join()
chore3.join()
print("All chores are complete.")
