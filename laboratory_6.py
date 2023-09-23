# # Использовать библиотеку openpyxl
# # Создать документ Excel с одним рабочим листом. Назвать его ‘Python’. 
# # Столбец A заполнить числами от 3 до 15.
# # Столбец B заполнить следующим образом: каждое третье значение столбца А умножается на 2, остальные просто переносятся из А.
# # По данным столбца B построить BarChart и  PieChart.
# # Сохранить 

# from openpyxl import Workbook
# from openpyxl.chart import BarChart, PieChart, Reference
# from openpyxl.styles import Font


# font = Font(name='Calibri', size=20, italic=True, bold = True, strike = True, color='FF00AA')
# wb = Workbook()
# worksheet = wb.active

# worksheet['A6'].font = font
# worksheet['B6'].font = font
# worksheet['C6'].font = font
# worksheet.title = 'Python'


# for number in range(3, 16):
#     worksheet.cell(column=1, row=number-2, value=number)

# for row in range(1, 14):
#     if row % 3 == 0:
#         worksheet.cell(column=2, row=row, value=worksheet.cell(column=1, row=row).value*2)
#     else:
#         worksheet.cell(column=2, row=row, value=worksheet.cell(column=1, row=row).value)

# chart = BarChart()
# chart.title = 'Линейный График'
# chart.y_axis.title = 'Values'
# chart.x_axis.title = 'Index'
# data = Reference(worksheet, min_col=2, min_row=1, max_row=13)
# cats = Reference(worksheet, min_col=1, min_row=2, max_row=13)
# chart.add_data(data, titles_from_data=True)
# chart.set_categories(cats)
# worksheet.add_chart(chart, 'D1')

# pie = PieChart()
# pie.title = "Круговая Диаграмма"
# labels = Reference(worksheet, min_col=1, min_row=2, max_row=13)
# data = Reference(worksheet, min_col=2, min_row=1, max_row=13)
# pie.add_data(data, titles_from_data=True)
# pie.set_categories(labels)
# worksheet.add_chart(pie, "D16")

# wb.save('lab_6.xlsx')