from json import loads, dumps
from csv import DictReader
from collections import OrderedDict

with open('users.json', 'r') as file:
    users = loads(file.read())

with open('example.json', 'r') as file:
    example = loads(file.read())

bookreaders = list()

for user in users:
    bookreader = OrderedDict()
    for key in user.keys():
        if key in example.keys():
            bookreader[key] = user[key]
    bookreader['books'] = list()
    bookreaders.append(bookreader)

with open('books.csv', 'r') as file:
    booklist = DictReader(file)

    for bookreader in bookreaders:
        book = next(booklist, {})
        if len(book):
            prettybook = OrderedDict()
            for key in book.keys():
                lowkey = key.lower()
                if lowkey in example['books'][0].keys():
                    prettybook[lowkey] = book[key]
            bookreader['books'].append(prettybook)

with open('result.json', 'w') as file:
    result = dumps(bookreaders, indent=4, sort_keys=True)
    print(result)
    file.write(result)