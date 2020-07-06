#!/usr/bin/env python
from Easy_Turtle import Easy_Turtle
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
import threading



def import_test():
    rospy.init_node('EZ_Turtle_control',anonymous=True)
    Easy_Turtle.remove_turtle("turtle1")

    t1=Easy_Turtle(5,9,0)
    
    t2=Easy_Turtle(5,1,0)
    
    t2.control()

if __name__ == '__main__':
    try:
        import_test()
    except rospy.ROSInterruptException:
        pass
