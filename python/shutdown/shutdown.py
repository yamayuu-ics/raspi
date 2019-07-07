#!/usr/bin/python3
# config:utf-8

import time
import RPi.GPIO as GPIO
import os

pinnum=4

GPIO.setmode(GPIO.BCM)


GPIO.setup(pinnum,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#print('test')

while True:
    GPIO.wait_for_edge(pinnum,GPIO.FALLING)
    sw_cnt = 0
    #print('tese2')
    while True:
        sw_status = GPIO.input(pinnum)
        #print("in loop")
        if sw_status == 0:
            sw_cnt = sw_cnt + 1
            if sw_cnt >= 50:
                #print("Start Shutdown Sequence")
		#os.system("echo "Start_Shutdown_Sequence"")
                os.system("sudo shutdown -h now")
                break
            else:
                pass
                #print("Short push")
                #break

            time.sleep(0.01)

	



