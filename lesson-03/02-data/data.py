from json import loads, dumps

with open('users.json', 'r') as file:
    users = loads(file.read())

with open('example.json', 'r') as file:
    example = loads(file.read())

readers = list()
for user in users:
    reader = dict()
    for key in user.keys():
        if key in example.keys():
            reader[key] = user[key]
    readers.append(reader)
# print(readers)