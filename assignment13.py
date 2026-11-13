import threading
import time

# Task 1: Display numbers
def display_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Task 2: Display squares
def display_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

# Task 3: Display message
def display_message():
    for i in range(1, 6):
        print("Hello from Thread 3!")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=display_squares)
t3 = threading.Thread(target=display_message)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
