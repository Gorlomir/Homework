my_dict = {'Огурцы': 7, 'Помидоры': 3, 'Апельсины': 8}
print(my_dict)
print(my_dict.get('Огурцы'))
print(my_dict.get('Мандарины', 'Такой покупки нет в списке'))
my_dict.update({'Мандарины' : 5,
               'Хурма': 6})
a = my_dict.pop('Огурцы')
print('Удаленная покупака', ':', a)
print(my_dict)

my_set = {1, 9, 8, 7, 5, 6, 7, 8, 9,}
print(my_set)
my_set.update({4, 2})
print(my_set)
my_set.remove(8)
print(my_set)