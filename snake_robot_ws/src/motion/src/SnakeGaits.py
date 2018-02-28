#! /usr/bin/python3
from __future__ import division
import math
import time
import Adafruit_PCA9685

class SnakeGaits:

	m1=0
	m2=1
	m3=2
	m4=3

	#This function will transform angles to pulse length.
	def angle_calc(self,ang):
		angle=(8.0/3)*float(ang)+400
		return int(angle)



	#This function will actually implement the angles using pwm pulse.
	def set_configuration(self,h1,v1,h2,v2,pause):
		pwm=Adafruit_PCA9685.PCA9685()
		pwm.set_pwm_freq(60)
		pwm.set_pwm(0,0,self.angle_calc(h1))
		pwm.set_pwm(1,0,self.angle_calc(v1))
		pwm.set_pwm(2,0,self.angle_calc(h2))
		pwm.set_pwm(3,0,self.angle_calc(v2))
		angle=[h1,v1,h2,v2]
		print(angle)
		time.sleep(pause)




	#Foward gait
	def forward_gait(self,Amp,loops,loop_pause):
		#Amp: amplitude
		#loop_pause = 0.001
		for j in range(0,loops+1):
			for i in range(0,100):
				#v: vertical h: horizontal & integer denotes the motor number.
				v1=Amp*(i/100.0)
				v2=-v1-(math.asin((166.26/188.23)*math.sin(v1*(math.pi/180.0))))*(180.0/math.pi)
				h1=0
				h2=0
				#self_configuration is called to give angles to motors.
				self.set_configuration(h1,v1,h2,v2,0.0001)
			time.sleep(loop_pause)




	def rolling_gait(self,Amp,side,loops,loop_pause):
		if side == -1:
			Ax=Amp
			Ay=-Amp
		else:
			Ax=Amp
			Ay=Amp

		W = math.pi*5/6
		d = math.pi*2/3
		phi = 0
		for i in range(0,loops+1):
			for t in range(0,100):
				t=t*math.pi/100
				v1 = Ax*(math.sin((W*t)+(2*d)))		#theta2
				v2 = Ax*(math.sin((W*t)+(4*d))) 	#theta4
				h1 = Ay*(math.sin((W*t)+(1*d)+phi))	#theta1
				h2 = Ay*(math.sin((W*t)+(3*d)+phi))	#theta3
				self.set_configuration(h1,v1,h2,v2,0.005)
			time.sleep(loop_pause)




	def backward_gait(self,Amp,loops,loop_pause):
		#This is to take one roll and change the orientation.
		self.rolling_gait(30,1,1,0.05)

		#This is code for backward gait.
		for i in range(0,loops+1):
			for j in range(0,100):
				v2=Amp*(j/100.0)
				v1=-v1-(math.asin((166.26/188.23)*math.sin(v1*(math.pi/180.0))))*(180.0/math.pi)
				h1=0
				h2=0
				self.set_configuration(h1,v1,h2,v2,0.0001)
			time.sleep(0.001)

		#This is to take one roll in opposite direction to get back to original orientation.
		self.rolling_gait(30,-1,1,0.05)





	def rotating_gait(self,side,loops,loop_pause):
		if side == 1:
			Ax=60
			Ay=10
		else:
			Ax=-60
			Ay=10

		for i in range(0,loops+1):
			for t in range(0,100):
				t=t*math.pi/100
				v1 = Ax*(math.sin((W*t)+(2*d)))	#theta2
				v2 = Ax*(math.sin((W*t)+(4*d)))
				h1 = Ay*(math.sin((W*t)+(1*d)+phi))
				h2 = Ay*(math.sin((W*t)+(3*d)+phi))
				self.set_configuration(h1,v1,h2,v2,0.005)
			time.sleep(loop_pause)
