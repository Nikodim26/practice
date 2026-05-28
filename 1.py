import json
import random

first_names = ['Александр', 'Максим', 'Дмитрий', 'Иван', 'Михаил', 'Андрей', 'Сергей', 'Владимир', 'Николай', 'Тимофей']
last_names = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Фёдоров', 'Морозов', 'Волков']
cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород', 'Челябинск',
          'Самара']


def generate_users(first_names, last_names, cities):
    while True:
        yield {'first_name': random.choice(first_names), 'last_name': random.choice(last_names),
               'age': random.randint(18, 65), 'city': random.choice(cities)}


user = generate_users(first_names, last_names, cities)
print(json.dumps([next(user) for i in range(3)], ensure_ascii=False, indent=4))
