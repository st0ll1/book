from person_start import Person

bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)
people = [bob, sue]     #  Список базы данных

for person in people:
    print(person.name, person.pay)

# -> список кортежей
x = [(person.name, person.pay) for person in people]

[rec.name for rec in people if rec.age >= 45]  # Генератор с условием. SQL  подобное выражение
[(rec.age**2 if rec.age >= 45 else rec.age) for rec in people]  


