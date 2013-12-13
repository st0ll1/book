'''
    Сценарий возьмет словарь словарей из файла initdata.py 
    и сохранит данные в бинарном формате в файле  people-pickle
'''
from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')        # В версии 3 использовать
pickle.dump(db, dbfile)                            # двоичный режим работы c файлами
dbfile.close()                                            # т.к данные имеют тип bytes а не string  
