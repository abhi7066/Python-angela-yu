# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 1.Write a program to create two threads and execute them parallelly

import threading

# Function to be executed in Thread 1
def thread_one_func():
    print("Thread 1 started.")
    # Code for Thread 1
    print("Thread 1 finished.")

# Function to be executed in Thread 2
def thread_two_func():
    print("Thread 2 started.")
    # Code for Thread 2
    print("Thread 2 finished.")

# Create Thread 1 and Thread 2
thread1 = threading.Thread(target=thread_one_func)
thread2 = threading.Thread(target=thread_two_func)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# The main program continues execution after both threads finish
print("Program execution completed.")