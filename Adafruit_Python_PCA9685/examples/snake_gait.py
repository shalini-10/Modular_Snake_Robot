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

'''#Forward Parameters
Aver=70
Ahor=0
w_ver=(5.0/6)*math.pi
w_ver=4*math.pi
w_hor=0
d_ver=(2.0/3)*math.pi
d_ver=2*math.pi
d_hor=0
delta0=0.0
Over=0
Ohor=0'''

#Roll Parameters
Aver=20
Ahor=20
w_ver=4*math.pi
w_hor=4*math.pi
d_ver=2*math.pi
d_hor=-2*math.pi
delta0=(30.0/180)*math.pi
Over=0
Ohor=0

def forward_motion_ver(i,t):
	ang=float(w_ver*t+(i-1)*d_ver)
	ang=float(ang*(math.pi/180))
	theta_ver=Aver*math.sin(ang)+Over
	return theta_ver

def forward_motion_hor(i,t):
	ang=float(w_hor*t+(i-1)*d_hor+delta0)
	ang=float(ang*(math.pi/180))
	theta_hor=Ahor*math.sin(ang)+Ohor
	return theta_hor
loops=50
for x in range(0,loops*30):
	pwm.set_pwm(3,0,angle_calc(forward_motion_hor(1,x)))
#	pwm.set_pwm(2,0,angle_calc(forward_motion_ver(1,x)))
	pwm.set_pwm(1,0,angle_calc(forward_motion_hor(2,x)))
	pwm.set_pwm(0,0,angle_calc(forward_motion_ver(2,x)))
	pwm.set_pwm(2,0,angle_calc(0))
	print(x)
	print(angle_calc(forward_motion_hor(1,x)))
	print(angle_calc(forward_motion_ver(1,x)))
	print(angle_calc(forward_motion_hor(2,x)))
	print(angle_calc(forward_motion_ver(2,x)))
	time.sleep(0.001)
