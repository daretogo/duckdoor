import time as time
from time import sleep      # Import sleep from time
import RPi.GPIO as GPIO     # Import Standard GPIO Module

GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM
GPIO.setwarnings(False);

# PWM Frequency
pwmFreq = 100

# Setup Pins for motor controller
GPIO.setup(12, GPIO.OUT)    # PWMA
GPIO.setup(18, GPIO.OUT)    # AIN2
GPIO.setup(16, GPIO.OUT)    # AIN1
GPIO.setup(22, GPIO.OUT)    # STBY
GPIO.setup(15, GPIO.OUT)    # BIN1
GPIO.setup(13, GPIO.OUT)    # BIN2
GPIO.setup(11, GPIO.OUT)    # PWMB

pwma = GPIO.PWM(12, pwmFreq)    # pin 18 to PWM  
pwma.start(100)

# Setup pins for limit switch
openingls = 38
GPIO.setup(openingls, GPIO.IN)

# Setup variables for stopping movement when limit switch triggered
pollinterval = 0.001
roomToGo = GPIO.input(openingls)


## Functions
###############################################################################
def counterclockwise(spd):
    runMotor(0, spd, 0)

def clockwise(spd):
    runMotor(0, spd, 1)

def runMotor(motor, spd, direction):
    GPIO.output(22, GPIO.HIGH);
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if(motor == 0):
        GPIO.output(16, in1)
        GPIO.output(18, in2)
        pwma.ChangeDutyCycle(spd)

def motorStop():
    GPIO.output(22, GPIO.LOW)

clockwise(99)
runduration = 11
currentduration = 0

while roomToGo == 0 and currentduration <= runduration:
  sleep(pollinterval)
  currentduration = currentduration + pollinterval
  roomToGo = GPIO.input(openingls)

clockwise(50)
runduration = 9
currentduration = 0

while roomToGo == 0 and currentduration <= runduration:
  sleep(pollinterval)
  currentduration = currentduration + pollinterval
  roomToGo = GPIO.input(openingls)

motorStop()
sleep(.25)
