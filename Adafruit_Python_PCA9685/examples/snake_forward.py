from __future__ import division
import time
import math
import Adafruit_PCA9685
pwm=Adafruit_PCA9685.PCA9685()

def set_servo_pulse(channel,pulse):
	pulse_length=1000000
	pulse_length //= 60
	print('{0}us per period'.format(pulse_length))
	pulse_length //= 4096
	print('{0}us per bit'.format(pulse_length))
	pulse *= 1000
	pulse //= pulse_length
	pwm.set_pwm(channel,0,pulse)
	pwm.set_pwm(channel,1,pulse)
	pwm.set_pwm(channel,2,pulse)
	pwm.set_pwm(channel,3,pulse)

pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')

def angle_calc(ang):
	angle=(8.0/3)*float(ang)+400
	return int(angle)

for j in range(1,30):
	for i in range(0,100):
		theta=70*(i/100.0)
		phi=-theta-(math.asin((166.26/188.23)*math.sin(theta*(math.pi/180.0))))*(180.0/math.pi)
		pwm.set_pwm(3,0,angle_calc(-theta))
		pwm.set_pwm(2,0,angle_calc(0))
		pwm.set_pwm(1,0,angle_calc(phi))
		pwm.set_pwm(0,0,angle_calc(0))
		time.sleep(0.0001)
	time.sleep(0.001)
	pwm.set_pwm(3,0,angle_calc(0))
	pwm.set_pwm(2,0,angle_calc(0))
	pwm.set_pwm(1,0,angle_calc(0))
	pwm.set_pwm(0,0,angle_calc(0))
	time.sleep(1)
'''	for i in range(0,100):
		theta=75*((100-i)/100.0)
		phi=-theta-(math.asin((166.26/188.23)*math.sin(theta*(math.pi/180))))*(180.0/math.pi)
		pwm.set_pwm(3,0,angle_calc(-theta))
		pwm.set_pwm(2,0,angle_calc(0))
		pwm.set_pwm(1,0,angle_calc(phi))
		pwm.set_pwm(0,0,angle_calc(0))
		time.sleep(0.01)'''
time.sleep(5)

pwm.set_pwm(2,0,angle_calc(0))
pwm.set_pwm(3,0,angle_calc(0))
pwm.set_pwm(0,0,angle_calc(0))
pwm.set_pwm(1,0,angle_calc(0))
