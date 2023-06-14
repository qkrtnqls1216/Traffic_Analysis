import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


data=pd.read_csv('C:/Users/PC/documents/경찰청_교통단속현황_20190618.csv', encoding='CP949')

traffic_df = data.loc[:, ['신호', '과속','음주', '무면허']]

print(traffic_df)
      
years = list(data['구분'])
print(years)

traffData1 = list(traffic_df['신호'])
print(traffData1)

traffData2 = list(traffic_df['과속'])
print(traffData2)

traffData3 = list(traffic_df['음주'])
print(traffData3)

traffData4 = list(traffic_df['무면허'])
print(traffData4)


plt.plot(
    years,
    traffData1,
    color='blue',
    marker='o',
    linestyle='solid'
)
plt.plot(
    years,
    traffData2,
    color='red',
    marker='^',
    linestyle='solid'
)
plt.plot(
    years,
    traffData3,
    color='orange',
    marker='s',
    linestyle='solid'
)
plt.plot(
    years,
    traffData4,
    color='green',
    marker='D',
    linestyle='solid'
)

plt.grid(True)
plt.legend(['신호', '과속', '음주', '무면허'])
plt.xticks(np.arange(2014, 2019), ["{:4d}".format(x) for x in np.arange(2014, 2019)])
plt.title("서울시 교통단속현황")
plt.xlabel('연도')
plt.ylabel('단속적발수') 
plt.show()
