# # Квадратная матрица должна иметь следующий вид:

# # 0  2  3  4  5 …
# # 2  0  3  4  5 …
# # 3  3  0  4  5 …
# # 4  4  4  0  5 …
# # 5  5  5  5  0 …
# # ……………….

# # Считать число с клавиатуры, сформировать и вывести такую матрицу, имеющую заданную размерность. Данную матрицу вывести в файл matrix.txt


# # РЕШЕНИЕ:

# import numpy as np

# n = int(input("Введите количество строк:"))
# m = int(input("Введите количество столбов"))

# mat = [[0]*m for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         if i==j:
#             mat [i][j] = 0
#         else:
#             mat[i][j] = max(i,j)

# np.savetxt('matrix1.txt', mat, '%3d')
# # ----------------------------------------------------------------


# # Считать с клавиатуры 2 числа: N и M, где N - количество строк матрицы, M - 
# # количество столбцов матрицы. 
# # Сформировать матрицу заданной размерности, состоящую из случайных чисел типа 
# # float с точностью до одного знака после точки. 
# # Данную матрицу вывести в документ Word с именем matrix.docx и документ Excel с именем matrix.xlsx


# # РЕШЕНИЕ:

# import random
# import openpyxl
# from docx import Document
# '''Для сохранения документа в формате docx использовал библиотеку python-docx'''

# n = int(input("Введите количество строк: "))
# m = int(input("Введите количество столбцов: "))

# matrix = [[round(random.uniform(0.0, 1.0), 1) for j in range(m)] for i in range(n)]

# '''Для сохранения документа в формате docx использовал библиотеку python-docx'''
# doc = Document()
# table = doc.add_table(rows=n, cols=m)
# for i in range(n):
#     row_cells = table.rows[i].cells
#     for j in range(m):
#         row_cells[j].text = str(matrix[i][j])
# doc.save('matrix.docx')

# wb = openpyxl.Workbook()
# ws = wb.active
# for i in range(n):
#     for j in range(m):
#         ws.cell(row=i+1, column=j+1, value=matrix[i][j])
# wb.save('matrix.xlsx')
