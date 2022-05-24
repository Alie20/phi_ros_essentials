#!/usr/bin/env python

# This node is a subscriber used to get the postition of the robot from turtlesim
# Tips to Write a Subscriber 
# Identifiy the name for the topic
# Identify the type of the message to be recieived
# Define a callback function that will be automatically execute the meessage 
# Start Listening for the topic messages

import rospy
from turtlesim.msg import Pose

#create a fucntion
def pose_call_back(message):
    rospy.loginfo("The x position % .2f",message.x)
    rospy.loginfo("The y position % .2f",message.y)
    rospy.loginfo("The Theta % .2f",message.theta)

#initialize a node with name listener
rospy.init_node('listener',anonymous=True)

#define a subscriber(nameOfTopic,Typeofmsg,nameOfFunction)
rospy.Subscriber('/turtle1/pose',Pose,pose_call_back)

#keep awake untill the user end the program
rospy.spin()
