from __future__ import division
import rospy
import time
import math
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
offset = 15

def angle_calc(ang):
    angle = (8.0/3)*float(ang)+400
    return int(angle)

def snake_home():
    pwm.set_pwm(0,0,angle_calc(-offset))
    pwm.set_pwm(1,0,angle_calc(offset))
    pwm.set_pwm(2,0,angle_calc(offset))
    pwm.set_pwm(3,0,angle_calc(offset))

def snake_forward(loops):
    for j in range(loops):
        for i in range(0,100):
            theta = 70*(i/100.0)
            phi = -theta-(math.asin((166.26/188.23)*math.sin(theta*(math.pi/180.0))))*(180.0/math.pi)
            pwm.set_pwm(0,0,angle_calc(theta-offset))
            pwm.set_pwm(1,0,angle_calc(0+offset))
            pwm.set_pwm(3,0,angle_calc(-phi+offset))
            pwm.set_pwm(2,0,angle_calc(0+offset))
            time.sleep(0.0001)
        time.sleep(0.001)
        snake_home()
        time.sleep(1)

def snake_roll(k,loops):
    Ax = 30
    Ay = 30
    Wx = math.pi*5/6
    Wy = math.pi*5/6
    dx = math.pi*2/3
    dy = math.pi*2/3
    phi = 0
    snake_home()
    for m in range(loops):
        Ax = 30
        Ay = k*30
        for t in range(0,100):
            t = t*math.pi/100
            theta2 = Ax*(math.sin((Wx*t)+(2*dx)))
            theta4 = Ax*(math.sin((Wx*t)+(4*dx)))
            theta1 = Ay*(math.sin((Wy*t)+(1*dy)+phi))
            theta3 = Ay*(math.sin((Wy*t)+(3*dy)+phi))

            pwm.set_pwm(0,0,angle_calc(theta1))
            pwm.set_pwm(1,0,angle_calc(theta2))
            pwm.set_pwm(3,0,angle_calc(theta3))
            pwm.set_pwm(2,0,angle_calc(theta4))
            time.sleep(0.005)

dec = True
while dec:
    print('Forward: 8, Roll Right: 6, Roll Left: 4, Home: 2, Stop: 5')
    act = input('Enter Action: ')
    if act == 8:
        snake_forward(2)
    elif act == 4:
        snake_roll(-1,2)
    elif act == 6:
        snake_roll(1,2)
    elif act == 2:
        snake_home()
    elif act == 5:
        dec = False
