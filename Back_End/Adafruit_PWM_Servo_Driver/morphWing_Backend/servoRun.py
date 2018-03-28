#!/usr/bin/python
import sys
sys.path.append('../')
from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 205 # Min pulse length out of 4096	#0
servoMax = 307  # Max pulse length out of 4096	#45
pwm.setPWMFreq(50)                        # Set frequency to 60 Hz


def TestingServoConfiguration(servo):
	#testing each servo for simple angle test

while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(0, 0, servoFin)
  time.sleep(1)
  #pwm.setPWM(0, 0, servoMax)
  #time.sleep(2)
  #pwm.setPWM(0, 0, servoFin)
  #time.sleep(2)
  
