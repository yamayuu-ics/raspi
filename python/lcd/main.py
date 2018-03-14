#!/usr/bin/python3
# config:utf-8




from lcd import i2cLcd
import time


#print("test")

lcd = i2cLcd(1,0x3e)

lcd.setCursor(0,0)
lcd.write("Write simple text to LCD")

time.sleep(2)

lcd.clear_display()
lcd.setCursor(0,0)
lcd.write_scroll("display scroll text")

time.sleep(2)

lcd.write_smart("if the text over max LCD,display with scroll")

time.sleep(2)

lcd.write_smart("Thanks!")

time.sleep(2)
