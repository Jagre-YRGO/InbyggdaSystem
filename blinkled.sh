#!/bin/bash

echo "blinking LED"

echo 24 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio24/direction
echo 1 > /sys/class/gpio/gpio24/value
sleep 0.5
echo 0 > /sys/class/gpio/gpio24/value
sleep 0.5
echo 1 > /sys/class/gpio/gpio24/value
sleep 0.5
echo 0 > /sys/class/gpio/gpio24/value
echo 24 > /sys/class/gpio/unexport

echo "ending LED-script"



