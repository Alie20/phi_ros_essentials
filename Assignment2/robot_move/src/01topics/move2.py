#!/usr/bin/env python

# Import the required libraries 
from cmath import sqrt
import queue
import rospy ,math 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time 

#define a global variabl to use it in all function.
x = 0 
y = 0
theta = 0
#define the call back function to get (x,y,theta).
def pose_call_back(message):
    global x,y,theta
    x = message.x
    y = message.y
    theta = message.theta
    #rospy.loginfo(f"X:{x}\tY:{y}\ttheta:{theta}\n")

def move(linear_velocity,distance):
    global x,y 
    x0 = x 
    y0 = y 
    moved_distance = 0
    linear_velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate =rospy.Rate(10)
    while(1):
        command_linear_velocity = Twist()
        command_linear_velocity.linear.x = linear_velocity  
        linear_velocity_publisher.publish(command_linear_velocity)
        rate.sleep()
        diff_x = (x-x0)**2
        diff_y = (y-y0)**2
        moved_distance = math.sqrt(abs(diff_x)+abs(diff_y))
        if(moved_distance >= distance):
            rospy.loginfo("############################################")
            rospy.loginfo("#                                          #")
            rospy.loginfo("#  Robot reached to the certain poisiton   #")
            rospy.loginfo("#                                          #")
            rospy.loginfo("############################################")
            break
def rotate(angular_velocity,angle):
    global theta 
    theta0 = theta
    angle_moved = 0
    angle = math.radians(angle)
    angular_velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate = rospy.Rate(50)
    while (1):
        command_angular_velocity = Twist()
        command_angular_velocity.angular.z = math.radians(angular_velocity)  
        angular_velocity_publisher.publish(command_angular_velocity)
        rate.sleep()
        angle_moved = abs(theta0-theta)
        rospy.loginfo(f"angle_moved:{angle_moved}\t angle_required:{angle}\n")
        if(angle_moved >= angle):
            rospy.loginfo("########################################")
            rospy.loginfo("#                                      #")
            rospy.loginfo("#  Robot reached to the certain Angle  #")
            rospy.loginfo("#                                      #")
            rospy.loginfo("########################################")
            break



        
    
    



rospy.init_node("move",anonymous=True)
rospy.Subscriber('/turtle1/pose',Pose,pose_call_back)
time.sleep(2)
move(1,2)
rotate(30,90)
