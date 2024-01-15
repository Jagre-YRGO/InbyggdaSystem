#!/usr/bin/python3


import socket
import gpiozero
import time

HOST = "192.168.0.89" #Host to connect to
PORT = 65432 		#Listen port

def my_function():
	print('Button was pressed!')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(b'Button was pressed!')
	s.close()


button = gpiozero.Button(21)
button.when_pressed = my_function

while True:
	try:
		my_input = int(input('Tell me your age:'))
		print(f'---You will turn {my_input+1} next year')
	except KeyboardInterrupt:
		print('\nEnding')
		break
