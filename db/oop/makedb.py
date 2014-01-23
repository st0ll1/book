# Создает базу данных на базе классов
import shelve
from person import Person, Manager
#from manager import Manager

bob = Person('Bob Smith', job = 'software', pay = 100000)
sue = Person('Sue Jones',  job = 'dev', pay = 100000)
tom = Manager('Tom Doe', 50000)

db = shelve.open('persondb')            # Имя файла хранилища
for object in (bob, sue, tom):              # В качестве ключа используем атрибут name
    db[object.name] = object               # Сохранить объект в хранилище
db.close()                                             # Закрыть после изменений


#----------------------------------------------------------------------------------------------------------------
# Тест
# if __name__ == '__main__':
#     db['bob'] = bob
#     db['sue'] = sue
#     db['tom'] = tom
#     db.close()
