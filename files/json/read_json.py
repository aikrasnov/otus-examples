import json

with open("foo.json", "r") as f:
    users = json.loads(f.read())

json.loads('{}')

users_list = users['users']

for user in users_list:
    print(user)


with open("bar.json") as f:
    print(json.load(f))
