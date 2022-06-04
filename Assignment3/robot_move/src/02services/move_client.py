#!/usr/bin/env python 

import rospy
from robot_move.srv import robot_move, robot_moveResponse , robot_moveRequest
from geometry_msgs.msg import Twist 


def robot_move_client(twist,duration):
    print(f"Sending data: {twist}\n duration: {duration}\n ")
    try:
        robot_move_proxy = rospy.ServiceProxy("robot_move_server",robot_move)
        move = robot_move_proxy(twist,duration)
        return move
    except rospy.ServiceException as e:
        print(f"Something wrong happed {e}")

rospy.init_node("robot_move_client1")
twist = Twist()
twist.linear.x = 0.5
twist.angular.z = 0.3
duration = 10

data = robot_move_client(twist,duration)
print("Status is {}".format(data.status))
print("{}".format(data.command))
print("Distance moved :{:0.2f}".format(data.distance))
#print("status is %b\t%s\nrobot moved %0.2f meter\n",data.status,data.command,data.distance)

