#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    print("write your logic here")
    GPIO.setmode(GPIO.BOARD)
    chan_list = [11,13,15] #GPIO 17,22 and 27 selected for LED's 
    GPIO.setup(chan_list, GPIO.OUT)
    # Toggle one LED high
    # GPIO.output(11, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(11, GPIO.LOW)
    chano_list = [16,18] #set GPIO 23 and 24 to inputs for buttons
    GPIO.setup(chano_list, GPIO.IN)
    GPIO.setup(chano_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(chano_list, GPIO.RISING, method_on_interrupt)
    GPIO.add_event_detect(chano_list, GPIO.FALLING, callback=callback_method(),bouncetime=300)
    '''
    # Button LED toggle
    if GPIO.event_detected(16):
        if count==0:
            GPIO.output(11, GPIO.HIGH)
            count=1
        else:
            GPIO.output(11, GPIO.LOW)
            count=0
    '''
    #Increase Count
    if GPIO.event_detected(16):
        if count==0:
            GPIO.output(11, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(15, GPIO.HIGH)
            count=1
        elif count==1
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)
	     count=2
        elif count==2
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.HIGH)
	     count=3
        elif count==3
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.LOW)
	     count=4
        elif count==4
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.HIGH)
	     count=5
        elif count==5
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)
	     count=6
        elif count==6
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.HIGH)
	     count=7
        elif count==7
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.LOW)
	     count=0
    #Decrease count
    if GPIO.event_detected(18):
        if count==0:
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            count=7
        elif count==1
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.LOW)
	     count=0
        elif count==2
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.HIGH)
	     count=1
        elif count==3
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)
	     count=2
        elif count==4
             GPIO.output(11, GPIO.LOW)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.HIGH)
	     count=3
        elif count==5
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.LOW)
	     count=4
        elif count==6
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(15, GPIO.HIGH)
	     count=5
        elif count==7
             GPIO.output(11, GPIO.HIGH)
             GPIO.output(13, GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)
	     count=6
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        count=0
        while True:
	   main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")
