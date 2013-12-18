class Person:
    ''' Метод __str__ возвращает отформатированную строку для печати объектов целиком
    '''
    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)      #__class__ является ссылкой на ближайший класс
        # экземпляром которого является объект self

tom = Manager('Tom Jones', 50)
print(tom)                                          # выведет: <Manager => Tom Jones>
