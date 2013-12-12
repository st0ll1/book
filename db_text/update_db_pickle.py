'''
Обновляем данные в базе
'''
import pickle

# Открываем базу
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

# Работаем с базой
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

#  Сохраняем изменения в базе
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
