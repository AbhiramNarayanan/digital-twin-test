import time
import random

def generate_data():
    while True:
        data = {"temperature": random.randint(20, 100), "pressure": random.randint(100, 200)}
        print(data)
        time.sleep(1)

if __name__ == "__main__":
    generate_data()
