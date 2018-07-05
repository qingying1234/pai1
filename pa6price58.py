import re
import requests
res=requests.get('http://cd.58.com/chuzu/?PGTID=0d100000-0006-6123-9a44-348c1b86d1f0&ClickID=2')
# print(res.text)
prices=re.findall('<div class="money">(.*?) </div>',res.text,re.S)
print(prices)
for price in prices:
    p = re.findall('<b>(.*?)</b>元/月',price)
    print(p)

