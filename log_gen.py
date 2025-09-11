import random
import time

niveles = ["INFO", "WARN", "ERROR", "DEBUG"]

with open("sample.log", "w") as f:
    for i in range(1000):
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {random.choice(niveles)} Test Log_{i}\n")

