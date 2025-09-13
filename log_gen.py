# This script generates a sample log file named "sample.log" with 1000 entries.
import random
import time

levels = ["INFO", "WARN", "ERROR", "DEBUG"]

with open("sample.log", "w") as f:
    for i in range(1000):
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {random.choice(levels)} Test Log {i}\n")

