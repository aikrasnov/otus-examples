from multiprocessing import Pool
import time


foo = []


def millis():
    return int(round(time.time() * 1000))

# noinspection PyShadowingNames
def calculate(_):
    start_time = millis()
    for i in range(100_000):
        foo.append(i)
    print(f"Took {str(millis() - start_time)} ms")


bar = list(range(1000))

pool = Pool(processes=10)

start_time = millis()
results = pool.map(calculate, bar)

print(f"Total took {str(millis() - start_time)}ms in 10 processes")

# for result in results:
#     print(result.status_code)

print("\n#######\n")

start_time = millis()
for b in bar:
    calculate(b)
print(f"Total took {str(millis() - start_time)}ms in 1 processes")
