#Подключение библиотек
from matplotlib import pyplot
from openpyxl import load_workbook

#Служебная функция
def getvalue(x):
    return  x.value

# Извлекаем таблицу Exel в переменную
wb = load_workbook('data_analysis_lab.xlsx')
