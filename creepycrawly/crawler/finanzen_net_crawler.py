from bs4 import BeautifulSoup
import requests
import re


#http://www.finanzen.at/suchergebnisse?_search=AT0000831706

resp = requests.get("http://www.finanzen.at/suchergebnisse?_search=AT0000831706", headers={"content-type":"text", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"})
#print(resp.text)
html = BeautifulSoup(resp.text, 'html.parser')
volStr = html.select('div.pricebox.content_box > div.content '
                       '> table:nth-of-type(2) > tr:nth-of-type(4) '
                       '> td:nth-of-type(4)')[0].text
volume = int(re.sub('\.', '', volStr))
print(volume)


