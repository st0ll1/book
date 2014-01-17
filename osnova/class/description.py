# Класс содержит словарь!!! атрибутов в атрибуте __dict__
class rec: pass

x = rec()
y = rec()

x.name = 'bob'
y.name = 'sue'

x.__dict__.keys()
y.__dict__

#-----------------------------------------------------------
#Каждый экземпляр имеет ссылку на родительский класс __class__

x.__class__

#Так же классы имеют атрибут __bases__ которы представляет собой
#кортеж суперклассов

rec.__bases__

#------------------------------------------------------------

# Методы
def upperName(self):
    return self.name.upper()

rec.method = upperName
x.method() # -> BOB
y.method() # -> SUE
rec.method(x) # а можно и так
rec.method(y) # или так


#-------------------------------------------------------------
#-------------------------------------------------------------
# Полноценный класс

class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def info(self):
        return (self.name, self.age, self.job)

rec1 = Person('Bob', 40, 'menagerie')
rec2 = Person('Sue', 30, 'trainer')

rec1.job, rec.info()
















