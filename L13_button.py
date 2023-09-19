#!/usr/bin/python3

import gpiozero
import time

def my_function():
	print('Button was presses!')
	time.sleep(10)
	print('awake')

button = gpiozero.Button(21)

button.when_pressed = my_function

while True:
	my_input = int(input('Tell me your age:'))
	print(f'---You will turn {my_input+1} next year')
