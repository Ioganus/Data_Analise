# # Создать список из 6 случайных целых чисел в диапазоне от 2 до 10 (включительно). 
# # По ним построить Pie chart. 
# # Поменять базовые цвета на какие-нибудь монохромные. 
# # Добавить подписи относительных пропорций каждой величины относительно общего (чтобы внутри каждого кусочка pie было написано количество процентов от общего) с точностью до 2 знака после запятой. 
# # Отделить один кусочек от остальных.


# from random import randint
# import matplotlib.pyplot as plt


# list = [randint(2, 10) for i in range(6)]

# total = sum(list)
# percents = [(x / total) * 100 for x in list]
# formated_percents = ["{:.2f}%".format(x) for x in percents]
# labels = [x for x in list]

# colors = ['#217074', '#37745B', '#8B9D77', '#EDC5AB', 'gray', '#E7EAEF']
# explode = (0.2, 0, 0, 0, 0, 0)

# plt.figure(figsize=(7, 7))
# plt.pie(list, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140, explode=explode)
# plt.title(f'Диаграмма случайных чисел от 2 до 10\n По списку: {list}\n{formated_percents}')

# plt.show()

