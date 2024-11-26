import random
import time

def generate_random_number(last_num):
    if random.random() < 0.9:
        return random.randint(10, last_num)
    return random.randint(last_num, 10000)

while True:
    with open("output.txt", "a") as file:
        last_num = generate_random_number(10000)
        file.write("power: " + str(last_num) + "\n")
    time.sleep(3)