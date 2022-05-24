#!/usr/bin/env python

import math
from click import command
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

x = 0
y = 0
theta = 0

def pose_call_back(message):
    global x ,y,theta 
    x     =  message.x
    y     =  message.y
    theta = message.theta
    #rospy.loginfo("%.2f\t%.2f\t%.2f\n",x,y,theta) 

def move(velocity,distance):
    '''
    global x,y
    x0 = x 
    y0 = y 
    rospy.loginfo("Hello %0.2f,%0.2f",x0,y0)
    current_distance = 0
    rate =rospy.Rate(100)
    velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    while(1):
        command_velocity = Twist()
        command_velocity.linear.x = velocity
        velocity_publisher.publish(command_velocity)
        rate.sleep()
        diff_x = (x-x0)**2
        diff_y = (y-y0)**2
        current_distance += math.sqrt(abs(diff_x)+abs(diff_y))
        rospy.loginfo("x0:%.2f\tx:%.2f\ty0:%.2f\ty:%.2f\tcurrent:%.2f\n",x0,x,y0,y,current_distance)
        if(distance <= current_distance):
            break
    command_velocity.linear.x = 0
    velocity_publisher.publish(command_velocity)

    '''
    command_velocity = Twist()
    distance_moved = 0
    t0 = time.time()
    while (1):

        velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        t1 = time.time()
        command_velocity.linear.x = velocity
        velocity_publisher.publish(command_velocity)
        distance_moved = (t1-t0)*velocity
        rate =rospy.Rate(1)
        #rospy.loginfo(f"")
        if (distance_moved >= distance):
            break     
    command_velocity.linear.x = 0
    velocity_publisher.publish(command_velocity)  

def rotate(angular_velocity,angle_required):
    
    global theta
    theta0= theta
    current_angle =0 
    rate =rospy.Rate(100)
    velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    while(1):
        command_velocity = Twist()
        angular_velocity_rad = math.radians(angular_velocity)
        command_velocity.angular.z = angular_velocity_rad
        velocity_publisher.publish(command_velocity)
        rate.sleep()
        current_angle = abs(theta - theta0) 
        rospy.loginfo (f"current_angle:%f\t angle_required:%f\t",current_angle,math.radians(angle_required))
        if(math.radians(angle_required) <= current_angle):
            break
    command_velocity.angular.z = 0
    velocity_publisher.publish(command_velocity)

    '''command_velocity = Twist()
    angle_moved = 0
    radian_speed = math.radians(angular_velocity)
    t0 = time.time()
    while (1):

        Angular_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        t1 = time.time()
        command_velocity.angular.z = radian_speed
        Angular_publisher.publish(command_velocity)
        angle_moved = (t1-t0)*angular_velocity
        rate =rospy.Rate(1)
        #rospy.loginfo(f"")
        if (angle_moved >= angle_required):
            break     
    command_velocity.angular.z = 0
    Angular_publisher.publish(command_velocity)  
'''

rospy.init_node('velocity',anonymous=True)
rospy.Subscriber('/turtle1/pose',Pose,pose_call_back)
time.sleep(1)
move(0.8,1)
rotate(30,90)



