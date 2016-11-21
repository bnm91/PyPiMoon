from bs4 import BeautifulSoup
from gpiozero import LED
import lxml
import requests
import time



ledOne = LED(17)
ledTwo = LED(10)
ledThree = LED(5)
ledFour = LED(11)
ledFive = LED(19)
ledSix = LED(22)

#run this continuously while the moon is on
#TODO make this run continuously while the moon is on
while True:
#get BeautifulSoup for raleigh moon phase page
        r = requests.get('http://www.timeanddate.com/moon/phases/usa/raleigh') #permalink

        data = r.text

        soup = BeautifulSoup(data, 'lxml')


        #find moon percent
        phasePercentSpan = soup.find('span', {'id': 'cur-moon-percent'})

        phasePercent = phasePercentSpan.get_text()
        phasePercent = phasePercent[0:len(phasePercent) - 1]
        phasePercent = float(phasePercent)

        print phasePercent


        #find the phase name
        qlook = soup.find('div', {'id': 'qlook'})

        phaseName = soup.find('p').get_text()

        print phaseName

        lights = [0, 0, 0, 0, 0, 0]

        #determine how lit up the room moon should be
        #TODO implement Pi led.on/led.off instead of these variables
        lightOne = 'off' #pin 17
        lightTwo = 'off' #pin 10
        lightThree = 'off' #pin 5
        lightFour = 'off'  #pin 11
        lightFive = 'off'  #pin 19
        lightSix = 'off'   #pin 22


        ledOne.off()
        ledTwo.off()
        ledThree.off()
        ledFour.off()
        ledFive.off()
        ledSix.off()

        #TODO refactor this logic
        #TODO add waxing logic
        if 'New Moon' in phaseName or phasePercent < 3:
                print 'new'
                lightOne = 'off'
                lightTwo = 'off'
                lightThree = 'off'
                lightFour = 'off'
                lightFive = 'off'
                lightSix = 'off'
        elif 'Waning Crescent' in phaseName:
                if phasePercent >=3 and phasePercent < 22:
                        print 'waning crescent small'
                        lightOne = 'on'
                        lightTwo = 'off'
                        lightThree = 'off'
                        lightFour = 'off'
                        lightFive = 'off'
                        lightSix = 'off'
                elif phasePercent >= 22 and phasePercent < 45:
                        print 'waning crescent big'
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'off'
                        lightFour = 'off'
                        lightFive = 'off'
                        lightSix = 'off'
        elif 'Third Quarter' in phaseName:
                print 'third quarter'
                if phasePercent >= 45 and phasePercent < 55:
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'off'
                        lightFive = 'off'
                        lightSix = 'off'
        elif 'Waning Gibbous' in phaseName:
                if phasePercent >= 55 and phasePercent < 88:
                        print 'waning gibbous small'
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'off'
                        lightSix = 'off'
                elif phasePercent >= 88 and phasePercent < 97:
                        print 'waning gibbous big'
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'on'
                        lightSix = 'off'
                elif phasePercent >= 97:
                        print 'waning gibbous basically full'
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'on'
                        lightSix = 'on'
        elif 'Full' in phaseName or phasePercent >=97:
                print 'full'
                lightOne = 'on'
                lightTwo = 'on'
                lightThree = 'on'
                lightFour = 'on'
                lightFive = 'on'
                lightSix = 'on'
        elif 'Waxing Crescent' in phaseName:
                if phasePercent >=3 and phasePercent < 22:
                        print 'waxing crescent small'
                        lightOne = 'off'
                        lightTwo = 'off'
                        lightThree = 'off'
                        lightFour = 'off'
                        lightFive = 'off'
                        lightSix = 'on'
                elif phasePercent >= 22 and phasePercent < 45:
                        print 'waxing crescent big'
                        lightOne = 'off'
                        lightTwo = 'off'
                        lightThree = 'off'
                        lightFour = 'off'
                        lightFive = 'on'
                        lightSix = 'on'

                        ledOne.on()
                        ledTwo.on()
                        ledThree.off()
                        ledFour.off()
                        ledFive.off()
                        ledSix.off()
        elif 'Waxing Gibbous' in phaseName:
                if phasePercent >= 55 and phasePercent < 88:
                        print 'waxing gibbous small'
                        lightOne = 'off'
                        lightTwo = 'off'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'on'
                        lightSix = 'on'
                elif phasePercent >= 88 and phasePercent < 97:
                        print 'waxing gibbous big'
                        lightOne = 'off'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'on'
                        lightSix = 'on'
                elif phasePercent >= 97:
                        print 'waning gibbous basically full'
                        lightOne = 'on'
                        lightTwo = 'on'
                        lightThree = 'on'
                        lightFour = 'on'
                        lightFive = 'on'
                        lightSix = 'on'


                

        print 'lightOne: ' + lightOne
        print 'lightTwo: ' + lightTwo
        print 'lightThree: ' + lightThree
        print 'lightFour: ' + lightFour
        print 'lightFive: ' + lightFive
        print 'lightSix: ' + lightSix
                
                
        #only need to update phase once per day
        time.sleep(86400)


