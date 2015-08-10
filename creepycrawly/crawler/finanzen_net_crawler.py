from bs4 import BeautifulSoup
import requests
import re


# http://www.finanzen.at/suchergebnisse?_search=AT0000831706







class FinanzenNetCrawler:
    def _pe_ratio(self, html):
        volStr = html.select('div.pricebox.content_box > div.content '
                             '> table:nth-of-type(2) > tr:nth-of-type(4) '
                             '> td:nth-of-type(4)')[0].text
        return int(re.sub('\.', '', volStr))

    def _volume(self, html):
        volStr = html.select('div.pricebox.content_box > div.content '
                             '> table:nth-of-type(2) > tr:nth-of-type(4) '
                             '> td:nth-of-type(4)')[0].text
        return int(re.sub('\.', '', volStr))

    def crawl(self, isin):
        '''
        starts the actual crawling of the page and extracts its data
        :param isin: the international securities identification number
        :return:
        '''
        resp = requests.get("http://www.finanzen.at/suchergebnisse?_search=" + isin,
                            headers={"content-type": "text",
                                     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"})

        # print(resp.text)
        html = BeautifulSoup(resp.text, 'html.parser')
        vol = self._volume(html)
        return vol






resp = requests.get("http://www.finanzen.at/suchergebnisse?_search=AT0000831706",
                    headers={"content-type": "text",
                             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 "
                                           "(KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"})
# print(resp.text)
html = BeautifulSoup(resp.text, 'html.parser')

crawler = FinanzenNetCrawler()
print(crawler.crawl("AT0000831706"))
print(crawler.crawl("DE0005190003"))
print(crawler.crawl("DE0008430026"))