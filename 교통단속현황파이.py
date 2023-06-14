import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

data=pd.read_csv('C:/Users/PC/documents/경찰청_교통단속현황_20190618.csv', encoding='CP949')

traffic_df = data.loc[:, ['신호', '과속','음주', '무면허']]

years = list(data['구분'])
print(years)

print(traffic_df)


my_labels = ['신호', '과속','음주', '무면허']

for i in range(0,5):
    plt.pie(traffic_df.loc[i], labels=my_labels, autopct='%1.1f%%')
    plt.title(str(years[i])+'년 교통단속현황')
    plt.axis('equal')
    plt.show()
