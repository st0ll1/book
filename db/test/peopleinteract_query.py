# интерактивные запросы
import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)      # Извлекаем самое длинное поле
db = shelve.open('class-shelve')

while True: 
    key = input('\nKey? => ')   # ключ или пустая строка, возбуждает исключение
                                                 # при вводе EOF
    if not key: break
    try:
            record = db[key]         # извлечь запись по ключу и вывести
    except:
            print('No such key “%s”!' % key)
    else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=>', getattr(record, field))  # Извлекает атрибут объекта record по полю fie
