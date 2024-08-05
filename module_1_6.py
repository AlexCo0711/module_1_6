# Практическое задание по теме: "Словари и множества"

# tsak 2
my_dict = {'Alex': 2000, 'Olga': 2001, 'Yulia': 1999, 'Sergey': 2002}  # созание словаря
print('Task 2')
print('Dict: ', my_dict)  # вывод словаря
print('Existing value: ', my_dict['Olga'])  # вывод по существующему ключу или
# вариант 2
print('Existing value: ', my_dict.get('Olga'))  # вывод по существующему ключу
print('Not existing value: ', my_dict.get('helga'))  # вывод по отсутствующему ключу
my_dict.update({'Polina': 1998, 'Elena': 1990})  # добавление произвольных пар
print('Modifid dictionary:', my_dict)
print('Deleted value:', my_dict.pop('Sergey'))  # вывод значения пары и удаление ключа пары
print('Modifid dictionary:', my_dict)

# task 3
my_set = {False, 1, 2, 3, 4, 5, 4, 3, 2, 1, False}  # создание произвольного множества
print('Set: ', my_set)  # вывод множества
set_1 = {9, 8, 7, }  # новое множество
my_set.update(set_1)  # добавление во множество нового множесмтва (объединение)
my_set.add((11, 12)) # добавление кортежа
print('Modifed set: ', (my_set)) # вывод полученноггшо множества
my_set.discard(2) # удаление 3-го элемента из множества
my_set.remove(5) # удаление 6-го элемента множества из 22-й строки
print('Modifed set: ', (my_set)) # вывод полученноггшо множества
