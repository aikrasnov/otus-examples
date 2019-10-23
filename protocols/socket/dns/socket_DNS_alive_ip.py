import socket
import requests

# Чекаем живой IP
domain = "www.protesting.ru"
foo, bar, addresses = socket.gethostbyname_ex(domain)
print(foo, bar, addresses)
print(f"ip: {addresses}")

for address in addresses:
    print(f"current ip: {address}")
    response = requests.get(f"https://{address}", verify=False, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    })
    if response.status_code == 200:
        break
else:
    raise SystemExit(f"There no alive ip for {domain}")

print(f"{address} {domain}")