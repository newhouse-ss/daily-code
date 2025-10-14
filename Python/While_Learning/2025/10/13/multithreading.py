import time
import threading

def walk_dog():
    time.sleep(5)
    print("You walked the dog.")

def take_out_trash():
    time.sleep(4)
    print("You took out the trash.")

def get_mail():
    time.sleep(2)
    print("You got the mail.")

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete.")