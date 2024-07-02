thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# access items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])  # Ford

# duplicates are not allowed
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# The dict()
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)  # {'name': 'John', 'age': 36, 'country': 'Norway'}

tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)

tel2 = dict(sape=4139, guido=4127, jack=4098)
print(f'tel2 is : {tel2}')
