from bs4 import BeautifulSoup

import lxml

import requests



r = requests.get('https://www.timeanddate.com/moon/phases/')

data = r.text

soup = BeautifulSoup(data, 'lxml')

phasePercentSpan = soup.find('span', {'id': 'cur-moon-percent'})

phasePercent = phasePercentSpan.get_text()

print phasePercent

