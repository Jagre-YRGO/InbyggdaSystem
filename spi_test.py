#!/usr/bin/python3.9

import time
import spidev
from subprocess import check_output

f = open('log_spi.txt', mode='w')

f.write('spi_test running \n')

segments = (126,
48,
int('0b1101101',2),
int('0b1111001',2),
int('0b0110011',2),
int('0b1011011',2),
int('0b1011111',2),
int('0b1110000',2),
int('0b1111111',2),
int('0b1110011',2))

def write_disp(pos, num):
    spi.xfer2([pos+1,segments[num]])

def write_num_short(pos, num):
    string = str(num)

    if pos == 0:
        i = 0
    else:
        i = 4

    k=-1
    for char in string:
        write_disp(i,int(string[k]))
        k -= 1
        i += 1

def write_num(num):
    string = str(num)
    i=0
    k=-1
    for char in string:
        write_disp(i,int(string[k]))
        k -= 1
        i += 1

def clear_disp():
    for i in range(1,9):
        spi.xfer2([i,0])

bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Test display
spi.xfer2([0x0F,0x01])
time.sleep(1)
spi.xfer2([0x0F,0x00])



spi.xfer2([0x0A,0x01]) #full intensity
spi.xfer2([0x0C,0x01]) #normal operation
spi.xfer2([0x0B,0x0F]) #scan limit

clear_disp()

retval = str(check_output(['hostname', '-I'])).split(' ')
ip_nums = retval[0].split('.')
#my ip  is: b'192.168.0.122 \n'

if False:
    print(ip_nums[0][2:])
    print(int(ip_nums[1]))
    print(int(ip_nums[2]))
    print(ip_nums[3][0:-4])
    print(f"my ip  is: {str(retval)}")

    write_num_short(0,ip_nums[3][0:-4])
    write_num_short(1,ip_nums[2])

print(ip_nums)
print(ip_nums[0][2:])
print(int(ip_nums[1]))
print(int(ip_nums[2]))
print(ip_nums[3])


write_num_short(0,ip_nums[3])
write_num_short(1,ip_nums[2])

f.write('spi_script done \n')
f.close()
