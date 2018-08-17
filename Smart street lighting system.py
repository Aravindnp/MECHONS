import time
import RPi.GPIO as GPIO
GPIO.cleanup()
TRIG =3 
ECHO =5
While(1):
	print "Distance measurement in progress“
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT) 
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.output(TRIG,False)
	print "Waiting for sensor to settle down"
	time.sleep(2)
	GPIO.output(TRIG,True) 
	time.sleep(0.00001) 
	GPIO.output(TRIG,False) 
	while GPIO.input(ECHO)==0:
	Pulse_start=time.time()
while GPIO.input(ECHO)==1:
	Pulse_end=time.time()
Pulse_duration= Pulse_end - Pulse_start 
distance = Pulse_duration*17150
distance=round(distance,2)
print "Distance : " ,distance ,"Cm“
if Distance<10
	GPIO.output(7,True) 	#making the street light on
time.sleep(5)
GPIO.output(7,false)	#making the street light off
GPIO.cleanup()

