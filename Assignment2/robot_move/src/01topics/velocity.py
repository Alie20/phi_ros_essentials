#!/usr/bin/env python

#Writing a publisher 
# Determine the name of the topic
# Determine the type of the messages 
# Determine the frequence of topic publication
# create publisher object
# keep Publishing the topic message at selected frequency

import rospy
from geometry_msgs.msg import Twist

#initialize the node with name velocity
rospy.init_node('velocity',anonymous=True)

#define a publisher(nameOfTopic,TypeOfMsg,SizeOfData)
velocity_publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

#define a frequency for publishing velocity
rate = rospy.Rate(5)

while not rospy.is_shutdown():
    command_velocity = Twist()
    command_velocity.linear.x = 0.0
    command_velocity.linear.y = 0.0
    command_velocity.linear.z = 0.0

    command_velocity.angular.x = 0.0
    command_velocity.angular.y = 0.0
    command_velocity.angular.z = 1.0

    #print on the screen the velocity
    rospy.loginfo(command_velocity)
    #publish to the topic
    velocity_publisher.publish(command_velocity)
    #wait 
    rate.sleep()
