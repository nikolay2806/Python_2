# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4
import copy
my_list_1 = []
count_1 = int(input('Введите количество элементов в 1-ом списке: '))
for i in range(count_1):
    result1 = int(input('Введите число №' + str(i+1) + ': '))
    my_list_1.append(result1)
print(my_list_1)
my_list_2 = []
count_2 = int(input('Введите количество элементов в 2-ом списке: '))
for i in range(count_2):
    result2 = int(input('Введите число №' + str(i+1) + ': '))
    my_list_2.append(result2)
print(my_list_2)
# Копия списка
# my_list_1[:]
# my_list_1.copy()
# copy.deepcopy(my_list_1)
for i in my_list_1[:]:
    if i in my_list_2:
        my_list_1.remove(i)
print(my_list_1)
