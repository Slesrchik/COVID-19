import camelot
import requests #импортируем модуль
f=open(r'D:\LearnPython.pdf',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://www.coronavirus.kdheks.gov/DocumentCenter/View/1125/Historical---May-6?bidId=") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()
tables = camelot.read_pdf('D:\LearnPython.pdf', pages='1,2,3')
tables.export("D:\KANSAS2.csv", f = "csv", compress = True)
#here we have zip file that consists of 3 pages.
