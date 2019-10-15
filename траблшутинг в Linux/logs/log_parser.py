import argparse
import re
import json


parser = argparse.ArgumentParser(description='Process access.log')
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/library/argparse.html#the-add-argument-method
parser.add_argument('-f', dest='file',  action='store', help='Path to logfile')
args = parser.parse_args()

dict_ip = {}

with open(args.file) as file:
    for index, line in enumerate(file.readlines()):
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
        method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
        if dict_ip.get(ip, None) is None:
            dict_ip[ip] = {
                "GET": 0,
                "POST": 0,
                "PUT": 0,
                "DELETE": 0,
                "HEAD": 0,
            }
        dict_ip[ip][method] += 1
        if index > 99:
            break

print(json.dumps(dict_ip, indent=4))
