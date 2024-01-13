#!/usr/bin/python3


import socket
import gpiozero
import time

HOST = "192.168.78.219" #Host to connect to
PORT = 65432 		#Listen port

def my_function():
	print('Button was pressed!')

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'Button was pressed!')
		s.close()

button = gpiozero.Button(21)
button.when_pressed = my_function


while True:
	my_input = int(input('Tell me your age:'))
	print(f'---You will turn {my_input+1} next year')
