# Добавим поведение (методы)

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

    def __str__(self):
      return '[Person: %s, %s ]' % (self.name, self.pay) 

    # -> Фамилию
    def lastName(self):
      return self.name.split()[-1]

    # Изменяет оклад
    def giveRaise(self, percent):
      self.pay *= (1.0 + percent)

  
#----------------------------------------------------------------------------------------------------------------------------
class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus)   # Правильно дополняет оригинал


if __name__ =='__main__':
       bob = Person('Bob Smith', 42, 30000, 'software')
       sue = Person('Sue Jones', 45, 40000, 'hardware')
       print(bob)
       print(sue)
       print(bob.name, sue.pay)
       print(bob.lastName())
       sue.giveRaise(.10)
       print(sue)
       #-------------------------------------------------------------------------------------------------------------------------
       # class Manager
       tom = Manager(name='Tom Doe',  age =50, pay=50000)
       print(tom.lastName())
       tom.giveRaise(.20)
       print(tom.pay)

    
