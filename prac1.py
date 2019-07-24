#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Mohamed Zahier Parker
Student Number: PRKMOH054
Prac: 1
Date: 21/07/2019
"""
count=0 #variable used to hold the current value of the LEDs 
# import Relevant Librares
import RPi.GPIO as GPIO
import time
#Set up the GPIO output and input pins
GPIO.setmode(GPIO.BOARD)
chan_list = [11,13,15]
GPIO.setup(chan_list, GPIO.OUT) #set GPIO 17,22 and 27 to output mode for LEDs
chano_list = [16,18]
GPIO.setup(chano_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set GPIO 23 and 24 to inputs for buttons and pull down configuration
def callback_method(channel):
    
    global count
    print("Button 1") # Used to indicate that the method is run when button is pressed
    #One LED toggle by switch
    if count==0:
        GPIO.output(11, GPIO.HIGH)
        count=1
    else:
        GPIO.output(11, GPIO.LOW)
        count=0
    

    '''
    #Increase count variable and display count value on LEDs
    if  count==0:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        count=1
    elif  count==1:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        count=2
    elif  count==2:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        count=3
    elif  count==3:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        count=4
    elif  count==4:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        count=5
    elif  count==5:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        count=6
    elif  count==6:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        count=7
    elif  count==7:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        count=0 #loops the count varible around
    '''
def callback_method2(channel):
    global count
    print("Button 2") # Used to indicate that the method is run when button is pressed 
    #Decrease count variable and display count on LEDs
    if  count==0:
        GPIO.output(11, GPIO.HIGH) 
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        count=7 #loops the count variable around
    elif  count==1:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        count=0
    elif  count==2:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        count=1
    elif  count==3:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        count=2
    elif  count==4:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        count=3
    elif  count==5:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        count=4
    elif  count==6:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        count=5
    elif  count==7:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        count=6
# Logic that you write
GPIO.add_event_detect(16, GPIO.RISING, callback=callback_method, bouncetime=300) #Sets GPIO pin 16 to detect a rising edge in the signal at this pin and run callback_method function when it picks up this interrupt. It also only allows the function to be called again after 300ms to ensure that the switch is not read multiple times for one press.
GPIO.add_event_detect(18, GPIO.RISING, callback=callback_method2, bouncetime=300) #Sets GPIO pin 18 to detect a rising edge in the signal at this pin and run callback_method2 function when it picks up this interrupt. It also only allows the function to be called again after 300ms to ensure that the switch is not read multiple times for one press. 
def main():
    print("Code is running") #Used to check if code is cycling
    time.sleep(1) #One second time delay ensuring that the LED is off for one second
    '''
    # Toggle one LED high
    GPIO.output(11, GPIO.HIGH) #Sets the GPIO11 high so that the LED goes on
    time.sleep(1) #One second time delay to ensure that the LED is on for one second
    GPIO.output(11, GPIO.LOW) #Sets GPIO11 low so the LED goes off
    '''
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
	   main()
    except KeyboardInterrupt: #exits the program when ctrl and c is pressed at the same time
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")
