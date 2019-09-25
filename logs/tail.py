import time
import sys

count = 0
while True:
    count += 1
    print(f"time: {time.time()}, count {count}")
    # Выталкиваем данные из буфера
    sys.stdout.flush()
    time.sleep(0.5)
