from multiprocessing.pool import ThreadPool
import time

foo = []


def millis():
    return int(round(time.time() * 1000))


# noinspection PyShadowingNames
def calculate(_):
    start_time = millis()
    for i in range(100_000):
        foo.append(i)
    print(f"Took {str(millis() - start_time)}ms")


bar = [0, 1, 2, 3, 4, 5]

pool = ThreadPool(processes=5)

start_time = millis()
results = pool.map(calculate, bar)

print(f"Total took {str(millis() - start_time)}ms in 5 threads")

# for result in results:
#     print(result.status_code)

print("\n#######\n")

start_time = millis()
for b in bar:
    calculate(b)
print(f"Total took {str(millis() - start_time)}ms in 1 threads")
