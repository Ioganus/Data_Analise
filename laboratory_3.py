# # 1)	Даны 2 списка, содержащие одинаковое количество числовых элементов. 
# # l1 = [1,3,2,5,7,4]
# # l2 = [0,4,6,3,7,4]
# # Вывести элементы первого списка, которые больше элементов второго, стоящие на одинаковых позициях (сравнивать первый с первым, второй со вторым и тд)
# # Пример:
# # Вывод >>>  1, 5

# # РЕШЕНИЕ

# l1 = [1,3,2,5,7,4]
# l2 = [0,4,6,3,7,4]
# for i in range(len(l1)):
#     if l1[i] > l2[i]:
#         print (l1[i], end =' ')



# # 2)	Даны 2 списка, содержащие одинаковое количество числовых элементов. 
# # l1 = [1,3,2,5,7,4]
# # l2 = [0,4,6,3,7,4]
# # Для каждой позиции вывести наибольший элемент из соответствующего списка.
# # Пример:
# # Вывод >>>  1, 4, 6, 5, 7, 4

# # РЕШЕНИЕ

# l1 = [1,3,2,5,7,4]
# l2 = [0,4,6,3,7,4]
# a = list(map(max, l1, l2))
# print (*a)

# # --------------------------------------------------------------------------------------------------------------------
# # 3)	names = [‘Sam’, ‘John’, ‘Lindsay’, ‘Anna’]
# # last_names = [‘Smith’, ‘Black’, ‘Johnson’,’Davis’]
# # В первом списке хранятся имена людей. Во втором хранятся их фамилии. Напечатать список данных людей в формате:
# # Имя_1 Фамилия_1
# # Имя_2 Фамилия_2
# # ...
# # Пример:
# # Вывод >>>  Sam Smith
# #  John Black
# #  Lindsay Johnson
# #  Anna Davis

# # РЕШЕНИЕ

# names = ['Sam', 'John', 'Lindsay', 'Anna']
# last_names = ['Smith', 'Black', 'Johnson','Davis']

# for i,j in zip(names, last_names):
#     print (i,j)