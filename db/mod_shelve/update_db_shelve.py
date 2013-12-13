from initdata import tom 
import shelve
db = shelve.open('people-shelve')

''' Извлекается объект sue, затем он изменяется в памяти,
а затем  снова сохраняется в хранилище
'''
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue                 # Изменяет объект съю
db.close() 