from multiprocessing.pool import ThreadPool
import time
import requests


def millis():
    return int(round(time.time() * 1000))


# noinspection PyShadowingNames
def http_get(url):
    start_time = millis()
    result = requests.get(url)
    print(url + " took " + str(millis() - start_time) + " ms")
    return result


urls = ['http://www.google.com/', 'https://foursquare.com/', 'http://www.yahoo.com/', 'http://www.bing.com/',
        "https://www.yelp.com/"]

pool = ThreadPool(processes=5)

start_time = millis()
results = pool.map(http_get, urls)

print(f"Total took {str(millis() - start_time)}ms in 5 threads")

# for result in results:
#     print(result.status_code)

print("\n#######\n")

start_time = millis()
for url in urls:
    http_get(url)
print(f"Total took {str(millis() - start_time)}ms in 1 threads")
