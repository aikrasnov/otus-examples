import argparse
import re
import json
from collections import defaultdict
# from collections import Counter, deque TODO: не забыть упомянуть


parser = argparse.ArgumentParser(description='Process access.log')
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/library/argparse.html#the-add-argument-method
parser.add_argument('-f', dest='file',  action='store', help='Path to logfile')
args = parser.parse_args()

dict_ip = defaultdict(lambda: {"GET": 0,"POST": 0,"PUT": 0,"DELETE": 0,"HEAD": 0})

with open(args.file) as file:
    for _, line in enumerate(file.readlines()):
        # 109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
        method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]

        dict_ip[ip][method] += 1

print(json.dumps(dict_ip, indent=4))
