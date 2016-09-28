from bs4 import BeautifulSoup

import lxml

import requests



r = requests.get('https://www.timeanddate.com/moon/phases/')

data = r.text

soup = BeautifulSoup(data, 'lxml')

phasePercentSpan = soup.find('span', {'id': 'cur-moon-percent'})

phasePercent = phasePercentSpan.get_text()

print phasePercent

qlook = soup.find('div', {'id': 'qlook'})

phaseName = soup.find('p').get_text()

print phaseName

lightNumber = 0

if phaseName = 'Waning Crescent':
	lightNumber = 1
elif phaseName = 'Third Quarter':
	lightNumber = 3
elif phaseName = 'Waning Gibbous':
	lightNumber = 5
elif phaseName = 'Full':
	lightNumber = 7

