from bs4 import BeautifulSoup
import lxml
import requests
import time

#run this continuously while the moon is on
#TODO make this run continuously while the moon is on
#while true:
#get BeautifulSoup for raleigh moon phase page
r = requests.get('http://www.timeanddate.com/moon/phases/usa/raleigh') #permalink

data = r.text

soup = BeautifulSoup(data, 'lxml')


#find moon percent
phasePercentSpan = soup.find('span', {'id': 'cur-moon-percent'})

phasePercent = phasePercentSpan.get_text()

print phasePercent


#find the phase name
qlook = soup.find('div', {'id': 'qlook'})

phaseName = soup.find('p').get_text()

print phaseName


#determine how lit up the room moon should be
#TODO: use both phase name and illumination percentage to determine which lights should be on
lightNumber = 0

if phaseName = 'Waning Crescent':
	lightNumber = 1
elif phaseName = 'Third Quarter':
	lightNumber = 3
elif phaseName = 'Waning Gibbous':
	lightNumber = 5
elif phaseName = 'Full':
	lightNumber = 7
	
	
	
	
#only need to update phase once per day
#time.sleep(86400)

