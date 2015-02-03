__author__ = 'jonathan'

#Working release
import requests
from bs4 import BeautifulSoup
import html2text

soup = BeautifulSoup(requests.get("http://www.blackaby.org/devarchive.asp").text)

page = soup.find('div', id='content-right')

title = page.find('span', class_="titleHome")
print title.text + '\n'

date = page.find('div', class_='sidetitle')
print date.text + '\n'

devotional = page.find("div", class_='content-body')
print html2text.html2text(devotional.prettify())