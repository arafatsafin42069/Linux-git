import threading
import time

def print_cube(num):
    print(f"Cube: {num * num * num}")
    time.sleep(1)  # Simulate some work

def print_square(num):
    print(f"Square: {num * num}")
    time.sleep(1)  # Simulate some work

# Create and start threads
t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))

t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Both threads have completed.")

