#Для работы с табличками
import pandas as pd 
#Для построения графика
import matplotlib.pyplot as plt  
#Загружаем данные из файла
df_raw = pd.read_parquet('titanic.parquet')  
#Сохраняем таблицу в формат csv без инлексов
df_raw.to_csv('titanic.csv', index=False) 
#Выводим что наша табличка готова
print("titanic.csv готов.")  
#Читаем наш csv 
df = pd.read_csv('titanic.csv')  
#Считаем количество пассажиров по классам и статусу выживания
stats = df.groupby(['Pclass', 'Survived']).size().unstack()  
#Строим диограмму
stats.plot(kind='bar', color=['salmon', 'seagreen'])  
#Подптсь для оси х
plt.xlabel('Класс каюты') 
#Подпись для у
plt.ylabel('Число пассажиров')  
#Заголовок
plt.title('Статистика выживших и погибших по классам Титаника')  
#Добавляем легенду с подписями
plt.legend(['Погибли', 'Выжили']) 
#Распологаем цифры классов горизантольно 
plt.xticks(rotation=0)  
#Горизонтальная сетка (для вайба)
plt.grid(axis='y', linestyle='--', alpha=0.5)  
#Открываем бурду
plt.show() 
