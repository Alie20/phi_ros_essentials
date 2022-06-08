#!/usr/bin/env python

import rospy
from turtlesim.srv import *

rospy.wait_for_service('/spawn')
spawner = rospy.ServiceProxy('/spawn', Spawn)
spawner(4, 2, 0, 'turtle3')
