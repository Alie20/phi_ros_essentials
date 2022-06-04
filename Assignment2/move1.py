#!/usr/bin/env python

# Import the required libraries 
import rospy ,math 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time 


#define move function that make robot to certain distance with fixed velocity     
def move(velocity,distance):
    # initialize Twist 
    command_velocity =Twist()
    distance_moved = 0
    rate = rospy.Rate(10)
    #initalize time 
    t0 = time.time()
    while(1):
        #define a publisher (topic_name,typeofmsg,message_size)
        velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 10)
        #intialize time at publishing time 
        t1 = time.time()
        #Save the given velocity to Twist
        command_velocity.linear.x = velocity
        #publish message
        velocity_publisher.publish(command_velocity)
        #calculate the distance by formula (distance = change in time * velocity)
        distance_moved=(velocity)*(t1-t0)
        rate.sleep()
        #print the distance moved and compare with required 
        rospy.loginfo(f"Distance_moved:{distance_moved}\tDistance_required:{distance}\n")
        #when the distance moved reached to distanc required stop
        if(distance_moved>=distance):
            rospy.loginfo("############################################")
            rospy.loginfo("#                                          #")
            rospy.loginfo("#  Robot reached to the certain poisiton   #")
            rospy.loginfo("#                                          #")
            rospy.loginfo("############################################")
            break
    command_velocity.linear.x = 0
    velocity_publisher.publish(command_velocity)

#define rotate function reach to angle with certain angular velocity
def rotate(angular_velocity,angle_required):
    # define the angle_moved at first 
    angle_moved = 0
    #define frequency
    rate = rospy.Rate(100)
    #intialize time at the first 
    t0 = time.time()
    #convert degree to radian
    angle_required_rad = math.radians(angle_required)
    
    while(1):
        #initlize Twist 
        command_angular_velocity = Twist()
        #define a publisher (topic_name,type of message, max no of message)
        angular_velocity_publisher= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        #convert the angular velocity from degree/s to rad/s 
        command_angular_velocity.angular.z = math.radians(angular_velocity)
        # publish the message
        angular_velocity_publisher.publish(command_angular_velocity)
        rate.sleep()
        # set the time at publish 
        t1 = time.time()
        # calculate the angle moved 
        angle_moved=(t1-t0)*(math.radians(angular_velocity))
        # print the result of angle moved and comapred with required angle 
        rospy.loginfo(f"Angle_moved in rad:{angle_moved}\tAngle Required in rad :{angle_required_rad}\n")
        # if the robot reach to certain angle stop
        if(angle_moved >= angle_required_rad):
            command_angular_velocity.angular.z = 0
            angular_velocity_publisher.publish(command_angular_velocity)
            rospy.loginfo("########################################")
            rospy.loginfo("#                                      #")
            rospy.loginfo("#  Robot reached to the certain Angle  #")
            rospy.loginfo("#                                      #")
            rospy.loginfo("########################################")
            break

rospy.init_node("move",anonymous=True)
move(1,4)
rotate(30,90)


