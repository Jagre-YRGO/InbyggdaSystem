#!/usr/bin/python3
import time
import gpiozero

button = gpiozero.Button(21)

dta_file = open('temp_log.csv',mode='w')

while True:
    f = open('/sys/bus/w1/devices/28-012063f42433/temperature')
    temp = int(f.readline())
    f.close()
    print(f'Current temperature is:{temp/1000}', end='\r')
    dta_file.write(str(temp/1000) + '\n')
    if button.is_pressed:
        break

dta_file.close()




