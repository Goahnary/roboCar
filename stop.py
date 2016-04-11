import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1E = 22

Motor2E = 19
 
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2E,GPIO.OUT)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
