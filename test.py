#!/usr/bin/env python3

from gpiozero import Button
import time

up = Button(22)
right = Button(23)
down = Button(24)
left = Button(25)
    
start = Button(5)
select = Button(6)
    
btn_A = Button(27)
btn_B = Button(26)
    
    


while True:
    #waits a moment for the code to catch up with itself
    time.sleep(0.1)
    #these are just a series of if statements - if the button is pressed, call the function!
    if up.is_pressed:
        print("Up!")
    if down.is_pressed:
        print("Down!")
    if left.is_pressed:
        print("Left!")
    if right.is_pressed:
        print("Right!")
    if start.is_pressed:
        print("Start!")
    if select.is_pressed:
        print("Select!")
    if btn_A.is_pressed:
        print("A!")
    if btn_B.is_pressed:
        print("B!")
    

    