import json

data = {
    "users": [
        {"Name": "Dominator", "skill": 100, "gold": 99999, "weapons": ['Sword', 'Atomic Laser']},
        {"Name": "Looser", "skill": 1, "gold": -100000, "weapons": [None, None, None]},
    ]
}

with open("foo.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)


with open("bar.json", "w") as f:
    s = json.dumps({"Имя": "Бар"}, indent=4, ensure_ascii=False)
    f.write(s)
