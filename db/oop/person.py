from classtools import AttrDisplay

# Добавим поведение (методы)
class Person(AttrDisplay):
    '''
       Суперкласс с базовыми данными. 
       Создает и обрабатывает информацию о людях
    '''
    def __init__(self, name, job=None, pay=0):
        self.name=name
        self.job=job
        self.pay=pay

    def __str__(self):
      return '[Person: %s, %s ]' % (self.name, self.pay) 

    # -> Фамилию
    def lastName(self):
      return self.name.split()[-1]

    # Изменяет оклад
    def giveRaise(self, percent):
      self.pay *= (1.0 + percent)

  
#----------------------------------------------------------------------------------------------------------------------------
# Класс Manager наследует и адаптирует поведение Person
class Manager(Person):
    ''' Класс адаптирует родительский класс Person '''  
    def __init__(self, name, pay):                              # Переопределение конструктора
      Person.__init__(self, name, 'mgr', pay)             # Вызов оригинального конструктора
                                                                                  # со значением 'mgr' в аргументе job
    def giveRaise(self, percent, bonus=0.1):
       Person.giveRaise(self, percent+bonus)            # Правильно дополняет оригинал


#-----------------------------------------------------------------------------------------------------------------------------
# Класс Department объединяет объекты в составной объект
class Department:
    ''' Класс объединяет объекты в составной объект '''
    def __init__(self, *args):
      self.members = list(args)

    def addMember(self, person):
      self.members.append(person)

    def giveRaise(self, percent):
      for person in self.members:
        person.giveRaise(percent)

    def showAll(self):
      for person in self.members:
        print(person)


#------------------------------------------------------------------------------------------------------------------------------
# Самотестирование
if __name__ =='__main__':
       bob = Person('Bob Smith', 'software', 30000)
       sue = Person('Sue Jones', 'hardware', 40000)
       print(bob)
       print(sue)
       print(bob.name, sue.pay)
       print(bob.lastName())
       sue.giveRaise(.10)
       print(sue)
       
       #-------------------------------------------------------------------------------------------------------------------------
       # # instance  of the class Manager
       tom = Manager(name='Tom Doe',  pay=50000)
       print(tom.lastName())
       tom.giveRaise(.20)
       print(tom.pay)
       print(tom)
       #--------------------------------------------------------------------------------------------------------------------------
       # processing all objects
       # print('-- All three -- ')
       # for object in (bob, sue, tom):
       #    object.giveRaise(.10)
       #    print(object)
      
       # development = Department(bob, sue)      # Встраивание объектов в составной объект
       # development.addMember(tom)
       # development.giveRaise(.10)                      #  Вызов метода giveRaise вложенных объектов
       # development.showAll()                              #  Вызов метода  __str__ вложенных объектов    
