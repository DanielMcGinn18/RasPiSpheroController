# Sphero Remote Control for Raspberry Pi
## Designed by researchers at the Tufts CEEO in Summer 2018

Python Files:
* BB8_driver.py - <a href="https://github.com/jjinking/SpheroBB8-python/blob/master/BB8_driver.py">Library used to implement high-level controls</a>
* sphero_keycommands.py - Control Sphero with keyboard
* sphero_remote.py - Control Sphero with Custom Raspberry Pi hat

Board Files:
* EAGLE schematic and board files for simple controller (sphero_remote.py is written for this board)
* EAGLE schematic for board version 2 with added functionality:
* Can be stacked on top of the <a href="https://www.adafruit.com/product/3196">Pimoroni LiPo SHIM</a>
* Single RGB LED
* Potentiometer and 10-bit ADC to allow user to change Sphero speed
* Through hole connection to Raspberry Pi

CAD Files:
* Raspberry Pi case for simple controller

To install bluepy run:
```sudo apt-get install python-pip libglib2.0-dev```
```sudo pip install bluepy```

Add the MAC address of your sphero to line 10 of BB8_driver.py

To run the program on your raspberry pi at startup enter the command: sudo nano /home/pi/.bashrc
go to the last line of the script and add:
echo Running at boot
sudo python <complete sphero_remote.py file path>