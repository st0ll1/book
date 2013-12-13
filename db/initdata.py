#Модуль для инициализации данных для передачи в файл

# Записи
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# База данных
db = {}                                                                         # Инициализация словаря
db['bob'] = bob                                                             # Ссылка на словари в словаре
db['sue'] = sue
db['tom'] = tom


if __name__ == '__main__' :                                           # Если запускается как script
    for key in db :
        print(key, ' => ', db[key])




