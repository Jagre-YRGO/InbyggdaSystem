import serial
ser = serial.Serial('COM14')  # open serial port
print(ser.name, ser.baudrate)         # check which port was really used
line = ser.readline()
print(line)
ser.write(b'hello123\n')     # write a string
ser.close()             # close port