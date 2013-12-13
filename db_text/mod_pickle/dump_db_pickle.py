'''
Востановит объект из  бинарного представления
  in: binary file
  out: object
  
'''
import pickle
dbfile = open('people-pickle', 'rb') 
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key] )        # Печатаем ключ и его значение (т.е словарь словарей)

print(db['sue']['name'])                  # Выводим конкретное значение ключа