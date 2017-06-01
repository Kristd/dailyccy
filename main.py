#-*-coding:utf-8-*-
# URL: http://www.boc.cn/sourcedb/whpj/

#test pull request

import urllib2
import re

response = urllib2.urlopen('http://www.boc.cn/sourcedb/whpj/')
html = response.read()
f = file('c:\http.html', 'w')
reg = '<td[^>]*>港币<\/td>[\W\w]+?<\/tr>'
match = re.search(reg, html).group(0)

#add currency

regArea = '港币'
regDate = '\d{4}-\d{2}-\d{2}'
regTime = '\d{2}:\d{2}:\d{2}'
regPrice = '\d+\.\d+'

area = re.search(regArea, match).group(0)
date = re.search(regDate, match).group(0)
time = re.search(regTime, match).group(0)

prices = re.findall(regPrice, match)
#print prices

f.write('Area: ' + area)
f.write(' Datetime: ' + date+' '+time)
f.write(' Prices: ')
for p in prices:
	f.write(p + ' ')

f.close()
