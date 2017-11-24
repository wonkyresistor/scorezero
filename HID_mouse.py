#!/usr/bin/env python3

'''
Welcome to the Score:Zero HID Mouse code!

This is essentially the same as the Keyboard code with a few teensy little mods :)

This code lets your Score:Zero (or any other set of GPIO buttons) act as a GPIO mouse.

By default, the U/D/L/R buttons move the mouse, A&B issue left & right clicks, start is
a space and select the letter 's'. You can mod these to anything you want - just change any
lines that mention that key from uinput.OLD_KEY to uinput.NEW_KEY.

If you find there are too many clicks when you press the button, increase the value for
time.sleep() in the while True loop. 

It requires the uinput, gpiozero and time libraries, but the installer script should look
after that. For more info visit wonkyresistor.com/scorezero. Have fun :)
'''

#makes sure that the system uinput module is running
from os import system
system("modprobe uinput")


#imports uinput (does all the keyboard emulation stuff), time (does timing), and the Button
#part of the gpiozero library to make it super easy to interface with buttons.
import uinput
import time
from gpiozero import Button
 

#defines each button depending on what GPIO it's hooked up to
up = Button(22)
right = Button(23)
down = Button(24)
left = Button(25)
    
start = Button(5)
select = Button(6)
    
btn_A = Button(27)
btn_B = Button(26)
    
    
#creates a list of keys used
keys = [uinput.REL_X, uinput.REL_Y, uinput.KEY_SPACE, uinput.KEY_S, uinput.BTN_LEFT, uinput.BTN_RIGHT]


#creates a keyboard called 'key'
key = uinput.Device(keys)

#the following are functions which trigger the desired key
#these don't need to be functions but it makes things a little neater
#and lets you easily trigger other funcitons on keypresses

#as standard they emit a single keypress/mouse move per trigger
def uppress():
    key.emit(uinput.REL_Y, -5)

def downpress():
    key.emit(uinput.REL_Y, 5)

def leftpress():
    key.emit(uinput.REL_X, -5)

def rightpress():
    key.emit(uinput.REL_X, 5)

def startpress():
    key.emit_click(uinput.KEY_SPACE)
        
def selectpress():
    key.emit_click(uinput.KEY_S)

def apress():
    key.emit_click(uinput.BTN_LEFT)

def bpress():
    key.emit_click(uinput.BTN_RIGHT)

#loops forever
while True:
    #waits a moment for the code to catch up with itself
    time.sleep(0.01)
    #these are just a series of if statements - if the button is pressed, call the function!
    if up.is_pressed:
        uppress()
    if down.is_pressed:
        downpress()
    if left.is_pressed:
        leftpress()
    if right.is_pressed:
        rightpress()
    if start.is_pressed:
        startpress()
    if select.is_pressed:
        selectpress()
    if btn_A.is_pressed:
        apress()
    if btn_B.is_pressed:
        bpress()
