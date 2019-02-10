# Written by Dan McGinn
# Keyboard inputs adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
# BB8_driver commands used: https://github.com/jjinking/SpheroBB8-python/blob/master/BB8_driver.py

#!/usr/bin/python
from bluepy import btle
import struct,time,BB8_driver,sys #Required for sphero driver
import sys, termios, tty, os, time #Required for keyboard inputs

# Initiate keybaord inputs
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
#Connect to sphero
bb8 = BB8_driver.Sphero()
bb8.connect()
bb8.start()
time.sleep(1)
bb8.set_rgb_led(0,100,0,0,False) #Turn on green light
print("Connection Initiated")

#Initialize speed, heading, state, button delay
speed = 123 #Half speed
heading=0
state=0
button_delay = 0.01

#Change sphero heading based on key commands
while True:
    char = getch()
    bb8.roll(speed, heading, state, False)
    time.sleep(.2)
    bb8.roll(0,heading,0,False)
 
    if (char == "p"):
	bb8.set_rgb_led(255,0,0,0,False) #Falsh red light
	time.sleep(1)
	bb8.join()
	bb8.disconnect()
	print("Sphero Disconnected")
	sys.exit(1)
        exit(0)
 
    if (char == "a"):
        print("Left")
	heading=90
	state=1
 
    elif (char == "d"):
        print("Right")
	heading=270
	state=1
 
    elif (char == "w"):
        print("Forward")
	heading=180
	state=1
 
    elif (char == "s"):
        print("Backward")
	heading=0
	state=1
 
    elif (char == " "):
        print("Break")
	state=0
        time.sleep(button_delay)
