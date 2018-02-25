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

print('Moving servo on channel 0, press Ctrl+c tp quit...')

def angle_calc(ang):
	angle=(8.0/3)*float(ang)+400
	return int(angle)

Ax = 30
Ay = 30
Wx = math.pi*5/6
Wy = math.pi*5/6
dx = math.pi*2/3
dy = math.pi*2/3
phi = 0


pwm.set_pwm(2,0,angle_calc(0))
pwm.set_pwm(3,0,angle_calc(0))
pwm.set_pwm(0,0,angle_calc(0))
pwm.set_pwm(1,0,angle_calc(0))
time.sleep(2)


k = 1
Ax = 30
Ay = k*30

for t in range(0,60):
	t = t*math.pi/100
	theta2 = Ax*(math.sin((Wx*t)+(2*dx)))
 	theta4 = Ax*(math.sin((Wx*t)+(4*dx)))
	theta1 = Ax*(math.sin((Wx*t)+(1*dx)+phi))
	theta3 = Ax*(math.sin((Wx*t)+(3*dx)+phi))
	
	pwm.set_pwm(2,0,angle_calc(theta1))
	pwm.set_pwm(3,0,angle_calc(theta2))
	pwm.set_pwm(0,0,angle_calc(theta3))
	pwm.set_pwm(1,0,angle_calc(theta4))
		
	time.sleep(0.05)

pwm.set_pwm(2,0,angle_calc(0))
pwm.set_pwm(3,0,angle_calc(0))
pwm.set_pwm(0,0,angle_calc(0))	
pwm.set_pwm(1,0,angle_calc(0))

time.sleep(2)

for j in range(1,30):
	for i in range(0,100):
		theta=70*(i/100.0)
		phi = -theta-(math.asin((166.26/188.23)*math.sin(theta*(math.pi/180.0))))*(180.0/math.pi)
		pwm.set_pwm(1,0,angle_calc(-theta))
		pwm.set_pwm(0,0,angle_calc(0))
		pwm.set_pwm(3,0,angle_calc(phi))
		pwm.set_pwm(2,0,angle_calc(0))
		time.sleep(0.0001)

	time.sleep(0.001)
	pwm.set_pwm(1,0,angle_calc(0))
	pwm.set_pwm(0,0,angle_calc(0))
	pwm.set_pwm(3,0,angle_calc(0))
	pwm.set_pwm(2,0,angle_calc(0))

time.sleep(5)

pwm.set_pwm(2,0,angle_calc(0))
pwm.set_pwm(3,0,angle_calc(0))
pwm.set_pwm(0,0,angle_calc(0))
pwm.set_pwm(1,0,angle_calc(0))
