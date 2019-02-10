# Tufts CEEO 2018
# BB8_driver Library: https://github.com/jjinking/SpheroBB8-python/blob/master/BB8_driver.py

#Import Libraries for Project
from bluepy import btle
import RPi.GPIO as GPIO
import struct,time,BB8_driver,sys

#GPIO Pin Designations
CW = 26; CCW = 21
GRN_LED = 15; RED_LED = 14;
RIGHT = 22; BWD = 27; FWD = 17; LEFT = 4;
QUIT = 26;

#Initiate GPIO Connection
GPIO.setmode(GPIO.BCM); GPIO.setwarnings(False)
GPIO.setup(CW, GPIO.IN, pull_up_down=GPIO.PUD_UP) #CW Button
GPIO.setup(CCW, GPIO.IN, pull_up_down=GPIO.PUD_UP) #CCW Button
GPIO.setup(GRN_LED, GPIO.OUT); GPIO.output(GRN_LED,GPIO.LOW) #Green LED
GPIO.setup(RED_LED, GPIO.OUT); GPIO.output(RED_LED,GPIO.LOW) #Red LED
GPIO.setup(RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Right Button
GPIO.setup(BWD, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Backward Button
GPIO.setup(FWD, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Forward Button
GPIO.setup(LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left Button
GPIO.setup(QUIT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Disconnect Button

#Connect to sphero
bb8 = BB8_driver.Sphero()
bb8.connect()
bb8.start()
time.sleep(1)
bb8.set_rgb_led(0,100,0,0,False) #Turn on sphero green light
GPIO.output(GRN_LED,GPIO.HIGH) #Turn on remote green LED
print("Connection Initiated")

#Initialize spin variables
heading=0
degree_change=10

#Initialize drive variables
speed=123 #Half Speed

#Define spin function
def sphero_spin (heading):
        bb8.roll(0,heading,0,False)
	bb8.set_rgb_led(0,0,0,0,False) #Turn off sphero LED
	bb8.set_back_led(255,False) #Turn on back LED

#Define drive function
def sphero_drive(heading):
	bb8.set_back_led(0,False) #Turn off back LED
	bb8.set_rgb_led(0,100,0,0,False) #Turn on sphero green LED
	bb8.roll(speed, heading, 1, False)
        time.sleep(0.2)
        bb8.roll(speed, heading, 0, False)

#Control sphero
while True:
    input_CCW = GPIO.input(CCW)
    input_CW = GPIO.input(CW)
    input_RIGHT = GPIO.input(RIGHT)
    input_BWD = GPIO.input(BWD)
    input_FWD = GPIO.input(FWD)
    input_LEFT = GPIO.input(LEFT)
    input_DISCONNECT = GPIO.input(QUIT)
#    heading = input("Enter Sphero Heading:") #Manual Heading Input
    if input_CCW == False: #CCW Spin
        if heading<(360-degree_change):
           heading+=degree_change
	else:
	   heading=heading-(360-degree_change)
	sphero_spin(heading)
        #print('Counterclockwise')
	print(heading)
    if input_CW == False: #CW Spin
	if heading>(degree_change):
	   heading-=degree_change
	else:
	   heading=heading+(360-degree_change)
	sphero_spin(heading)
        #print('Clockwise')
	print(heading)
    if input_LEFT== False: #LEFT Drive
        if heading<90:
	   left_heading=heading+270
	else:
	   left_heading=heading-90
	sphero_drive(left_heading)
	print("Left")
    if input_RIGHT == False: #RIGHT Drive
        if heading<270:
	   right_heading=heading+90
	else:
	   right_heading=heading-270
	sphero_drive(right_heading)
	print("Right")
    if input_FWD == False: #FWD Drive
	fwd_heading=heading
	sphero_drive(fwd_heading)
        print("Forward")
    if input_BWD == False: #BWD Drive
	if heading<180:
	   bwd_heading=heading+180
	else:
	   bwd_heading=heading-180
	sphero_drive(bwd_heading)
        print("Backward")
    if (input_CW==False and input_CCW==False): #Disconnect
	bb8.set_back_led(0,False) #Turn off back LED
	bb8.set_rgb_led(255,0,0,0,False) #Falsh red ligh
	GPIO.output(GRN_LED,GPIO.LOW) #Turn of Remote Green LED
	GPIO.output(RED_LED,GPIO.HIGH) #Flash Remote Red LED
	time.sleep(2)
	GPIO.output(RED_LED,GPIO.LOW)
	bb8.join()
	bb8.disconnect()
	print("Sphero Disconnected")
	sys.exit(1)
	exit(0)
