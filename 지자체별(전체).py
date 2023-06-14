import requests
import matplotlib.pyplot as plt 
import matplotlib as mpl 
from matplotlib import font_manager, rc
from xml.etree.ElementTree import fromstring

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

key = 'Vw7ZO84ToP%2FEBj5kKE%2BJ4%2Fzifi8aQ43NHaMYsA9jyFYlirKMW7381MPxhakOaai6tSqciZ61RpuWdFa8Z5wU0A%3D%3D'

years = [2016, 2017, 2018, 2019]
siDos = [1100,1200,1300,1400]
guGun = ''

data={1100:[], 1200:[], 1300:[], 1400:[]}


for i in siDos:
    for j in years:
       murl = f'http://apis.data.go.kr/B552061/lgStats/getRestLgStats?ServiceKey={key}&searchYearCd={j}&siDo={i}&guGun=&numOfRows=1&pageNo=1'
       res = requests.get(murl)
       trafficData = res.text
       tree = fromstring(trafficData)
       acc_cnt = int(tree.find("body").find("items").find("item").findtext("acc_cnt"))
       data[i].append(acc_cnt)

print(data)

plt.plot(data[1100], marker='o')
plt.plot(data[1200], marker='s')
plt.plot(data[1300], marker='^')
plt.plot(data[1400], marker='D')

plt.legend(['서울', '부산', '경기도', '강원도'])
plt.grid(True)
plt.xticks(range(4), ['2016','2017', '2018','2019'], color='black')
plt.yticks(range(7500, 60001, 2500), ["{:d}".format(x) for x in range(7500, 60001, 2500)])
plt.title("지역별 교통사고건수")
plt.xlabel('연도')
plt.ylabel('사고건수')
plt.show() 
