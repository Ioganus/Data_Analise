# # 1)	Осуществляется ввод данных списка с клавиатуры. Реализовать функцию, принимающую одно число и возвращающую его модуль. 
# # Вывести список абсолютных величин исходного списка. А также число – количество вызовов функции. Не забыть обработать 
# # возможные исключения.
# # Пример:
# # Ввод >>>  1 -3 8 -19 0 -88
# # Вывод >>> [1, 3, 8, 19, 0, 88], количество вызовов = 6


# # РЕШЕНИЕ
# try:
#     array = list(map(int, input("Введите целые числа через пробел: ").split()))
# except Exception:
#         print("!!!Ошибка ввода. Введите данные в соответствии с требованием!!!")

# def absolute ():
#     try:
#         my_abs =[abs(i) for i in array]
#         print (f'{my_abs}, количество вызовов = {len(my_abs)}' )
#         return my_abs
#     except Exception:
#         print ('!!!Error. Please enter numbers as required!!!')

# absolute ()


# # ------------------------------------------------------------------------------------
# # 2)	Вводятся с клавиатуры 2 списка. Реализовать поэлементное умножение элементов первого списка на элементы второго.
# # Пример:
# # Ввод >>>  1 2 3 4 5 6
# # 	      1 2 3 4 5 6
# # Вывод >>> [1, 4, 9, 25, 36]


# #РЕШЕНИЕ 
# List_1 = list(map(int,input().split()))
# List_2 = list(map(int,input().split()))

# print ([List_1[i]*List_2[i] for i in range(len(List_1))])


# # --------------------------------------------------------------------------------------------
# # 3)	Дана строка с пробелами (с несколькими словами). Вывести длину слов в строке, используя функцию map().
# # Пример:
# # Ввод >>>  “All the world is a stage”
# # Вывод >>> [3, 3, 5, 2, 1, 5]


# # РЕШЕНИЕ
# stroka = 'All the world is a stage'
# chars = [len(i) for i in stroka.split()]

# print (chars)

