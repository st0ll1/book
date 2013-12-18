from person import Person
from manager import Manager
bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Doe', age=55, pay=30000)
db = [bob, sue, tom]

for obj in db:
    obj.giveRaise(.10) # метод по умолчанию или специализированный


for obj in db:
    print(obj.lastName(), '=>', obj.pay)


# Расширение методов класса

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)  # Вызываем непосредственно версию метода суперкласса и передаем аргументы

# Вызовы  ниже эквивалентны 
# instance.method(arg1, arg2)
# class.method(instance, arg1, arg2)

