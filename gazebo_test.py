#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import numpy
import math
import sys
import cv2
from matplotlib import pyplot
from cv_bridge import CvBridge, CvBridgeError
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
position_x = 0
position_y = 0
ang_vel=0


def walk():

    velocity.linear.x =.5
    velocity.angular.z=0
    bot1.publish(velocity)
    rospy.sleep(1)
    while not rospy.is_shutdown():
        velocity.linear.x =.5
        velocity.angular.z=0
        bot1.publish(velocity)
        if scanner_data.ranges[0]<=1.4:
            print "OBJECT DETECTED AT DISTANCE", scanner_data.ranges[0]
            velocity.linear.x =0
            velocity.angular.z=0
            bot1.publish(velocity)
            rospy.sleep(1)
            collision_avoid()


def collision_avoid():
    print "Avoiding Collision..."
    while 1:
        velocity.linear.x =0
        velocity.angular.z=.3
        bot1.publish(velocity)
        rospy.sleep(3)
        print "Returning to normal operation..."
        walk()




def scan_callback(scan):
    global scanner_data
    scanner_data=scan


def pose_callback(pos):
        global position_x, position_y

        position_x = pos.pose.pose.position.x
        position_y = pos.pose.pose.position.y
        ang_vel=pos.pose.pose.orientation.w

def gazebo_test():
    global velocity, bot1
    rospy.init_node('turtle_control', anonymous=True)
    bot1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom',Odometry, pose_callback)
    rospy.Subscriber('/scan',LaserScan, scan_callback )
    velocity=Twist()
    rate=rospy.Rate(10)

    key=raw_input("ready?")

    walk()

    velocity.linear.x =0
    velocity.angular.z=0
    bot1.publish(velocity)
    rospy.sleep(1)




try:
    gazebo_test()
except rospy.ROSInterruptException:
    pass
