#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import numpy
import random
import math
import sys
from matplotlib import pyplot

turtle_count=1

def is_close_to(a,b):
#    if a<b and a+.05>=b:
#        return True
    if a>b and a-.5<b:
        return True
    else:
        return False

def is_close_to_hazard(a,b):
    if a<b and a+.05>=b:
        return True
    if a>b and a-.5<b:
        return True
    else:
        return False

def callback1(pos):
    global pos1, recent_x,recent_y
    pos1=pos
    recent_x=pos.x
    recent_y=pos.y
def callback2(pos):
    global pos2, recent_x, recent_y
    pos2=pos
    recent_x=pos.x
    recent_y=pos.y
def callback3(pos):
    global pos3, recent_x, recent_y
    pos3=pos
    recent_x=pos.x
    recent_y=pos.y
def callback4(pos):
    global pos4, recent_x, recent_y
    pos4=pos
    recent_x=pos.x
    recent_y=pos.y
def callback5(pos):
    global pos5, recent_x, recent_y
    pos5=pos
    recent_x=pos.x
    recent_y=pos.y

def add_a_turtle():
    global turtle_count
    if turtle_count==1:
        add_turtle(pos1.x,pos1.y,pos1.theta, 'turtle2')
        rospy.Subscriber('/turtle2/pose',Pose, callback2)
        turtle_count+=1

    elif turtle_count==2:
        add_turtle(pos2.x,pos2.y, pos2.theta, 'turtle3')
        rospy.Subscriber('/turtle3/pose',Pose, callback3)
        turtle_count+=1

    elif turtle_count==3:
        add_turtle(pos3.x,pos3.y, pos3.theta, 'turtle4')
        rospy.Subscriber('/turtle4/pose',Pose, callback4)
        turtle_count+=1

    elif turtle_count==4:
        add_turtle(pos4.x,pos4.y, pos4.theta, 'turtle5')
        rospy.Subscriber('/turtle5/pose',Pose, callback5)
        turtle_count+=1



def remove_a_turtle():
    pass


def turtle_circle():
    global turtle1,turtle2,turtle3,turtle4,turtle5, pi, turtle_count
    global velocity,velocity2, velocity3, velocity4, velocity5, recent_x, recent_y
    global add_turtle,pos1,pos2,pos3,pos4,pos5

    pi=math.pi
    rospy.init_node('turtle_circle_control',anonymous=True)
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    rospy.wait_for_service('kill')
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    remove_turtle("turtle1")
    add_turtle(5.544445,.5, 0, 'turtle1')
    turtle1=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    turtle2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
    turtle3=rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
    turtle4=rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=10)
    turtle5=rospy.Publisher('turtle5/cmd_vel', Twist, queue_size=10)

    rospy.Subscriber('/turtle1/pose',Pose, callback1)
    rate = rospy.Rate(.2)
    velocity=Twist()
    rospy.sleep(1)

    #set initial velocity based on circle radius
    r=input("Input circle radius: ")
    velocity.angular.z=2
    velocity.linear.x=velocity.angular.z*r

#    print "Press a to add a turtle and o to add an obstacle"
    amount=input("How many turtles do you want?")
    while not rospy.is_shutdown():

        turtle1.publish(velocity)
        turtle2.publish(velocity)
        turtle3.publish(velocity)
        turtle4.publish(velocity)
        turtle5.publish(velocity)

        if turtle_count<amount and is_close_to(recent_x, 5.544445) and recent_y>1:
            add_a_turtle()
            rospy.sleep(.25)





if __name__ == '__main__':
    try:
        turtle_circle()
    except rospy.ROSInterruptException:
        pass
