#Подключение библиотек
from matplotlib import pyplot
from openpyxl import load_workbook

#Служебная функция
def getvalue(x):
    return  x.value

# Извлекаем таблицу Exel в переменную
wb = load_workbook('data_analysis_lab.xlsx')

# Извлекаем лист из таблицы
sheet = wb['Data']

#Извлекаем содержимое столбцов А, С, D
years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

#Отображение списков на графике
pyplot.plot(years, temperature, label='относительная температура')
pyplot.plot(years, activity, label='активность солнца' )

#Отображаем график
pyplot.show()




