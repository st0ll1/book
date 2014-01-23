# Обновление записей в базе используя классы

import shelve

db = shelve.open('persondb')
for key in db:
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.25)
db['Sue Jones'] = sue

db.close()