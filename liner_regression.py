from pandas_datareader import data
from matplotlib import pyplot as plt
import pandas as pd
from selenium import webdriver

oecd = pandasdmx.Request('OECD')
data_response = oecd.data(resource_id='MEI_CLI', key='all?startTime=2018')
df = data_response.write(data_response.data.series, parse_time=False)
df.to_csv('c:\\Temp\\test_lei.txt', sep='\t')

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome('/Users/jjune/Downloads/chromedriver', options=options)
browser.get('https://www.wsj.com/market-data/bonds')

path = '//*[@id="root"]/div/div/div/div[2]/div[3]/div/div[3]/div[1]/div/table/tbody/tr[1]/td[1]'
table = browser.find_element_by_xpath(path)

rows = table.text.split('\n')
elements = []
for r in rows:
    elements.append([i for i in r.split(' ')])
df = pd.DataFrame(elements)

print (df)

snp = data.DataReader('^GSPC', 'yahoo', start='1992-01-02')
treas = data.DataReader('VFITX', 'yahoo', start='1992-01-02')

#print(treas)
#print(treas.shape)
#print(treas.describe())

print(snp)
print(snp.shape)
print(snp.describe())

snp.plot(y='Close', style='o')
plt.title('Close value by date')
plt.xlabel('Date')
plt.ylabel('Close')
plt.show()