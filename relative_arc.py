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
global goal_num
goal_num=0

def is_close_to(a,b):
    if a<b and a+.1>=b:
        return True
    if a>b and a-.1<b:
        return True
    else:
        return False

def goal_hit():
    global goal_x, goal_y, goal_num
    goal_num+=1

    if goal_num==1:
        remove_turtle("goal")
        print "GOAL 1 REACHED"
        goal_x=1.08889
        goal_y=9.5
        add_turtle(goal_x, goal_y, pi/2,"goal1")
    elif goal_num==2:
        remove_turtle("goal1")
        print "GOAL 2 REACHED"
        goal_x=1.2
        goal_y=1.08889
        add_turtle(goal_x, goal_y, pi/2,"goal2")
    elif goal_num==3:
        remove_turtle("goal2")
        print "GOAL 3 REACHED"
        goal_x=6
        goal_y=7
        add_turtle(goal_x, goal_y, pi/2,"goal3")
    elif goal_num==4:
        remove_turtle("goal3")
        print "GOAL 4 REACHED"
    else:
        pass

def callback_head(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[0]=pos.x
    snake_members_y[0]=pos.y
    snake_members_theta[0]=pos.theta
    print snake_members_x[0]

def callback_member1(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[1]=pos.x
    snake_members_y[1]=pos.y
    snake_members_theta[1]=pos.theta
    print snake_members_x[1]
def callback_member2(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[2]=pos.x
    snake_members_y[2]=pos.y
    snake_members_theta[2]=pos.theta
    print snake_members_x[2]
def callback_member3(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[3]=pos.x
    snake_members_y[3]=pos.y
    snake_members_theta[3]=pos.theta
    print snake_members_x[3]
def callback_member4(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[4]=pos.x
    snake_members_y[4]=pos.y
    snake_members_theta[4]=pos.theta
    print snake_members_x[4]
def callback_member5(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[5]=pos.x
    snake_members_y[5]=pos.y
    snake_members_theta[5]=pos.theta
    print snake_members_x[5]
def callback_member6(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[6]=pos.x
    snake_members_y[6]=pos.y
    snake_members_theta[6]=pos.theta
    print snake_members_x[6]
def callback_member7(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[7]=pos.x
    snake_members_y[7]=pos.y
    snake_members_theta[7]=pos.theta
    print snake_members_x[7]
def callback_member8(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[8]=pos.x
    snake_members_y[8]=pos.y
    snake_members_theta[8]=pos.theta
    print snake_members_x[9]
def callback_member9(pos):
    global snake_members_x, snake_members_y, snake_members_theta, velocity,goal_num
    snake_members_x[9]=pos.x
    snake_members_y[9]=pos.y
    snake_members_theta[9]=pos.theta
    print snake_members_x[9]

def snake_walk():
    global head, velocity
    head.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member1.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member2.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member3.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member4.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member5.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member6.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member7.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member8.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member8.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8
    member9.publish(velocity)
    velocity.linear.x=velocity.linear.x*.8

def head_move():
    global velocity, angle_got, goal_num
    goal_num=0
    while 1:
        velocity.linear.x=6
        velocity.angular.z=0
        snake_walk()

        if is_close_to(snake_members_x[0],goal_x):
            angle_got=snake_members_theta[0]
            break

    while not is_close_to(abs(snake_members_theta[0]-angle_got),pi/2):
        velocity.linear.x=3
        velocity.angular.z=7
        snake_walk()

    while 1:
        velocity.linear.x=6
        velocity.angular.z=0
        snake_walk()

        if is_close_to(snake_members_y[0],goal_y):
            angle_got=snake_members_theta[0]
            break
    goal_hit()

    while not is_close_to(abs(snake_members_theta[0]-angle_got),4.7):

        velocity.linear.x=3
        velocity.angular.z=7
        snake_walk()

    while 1:
        velocity.linear.x=6
        velocity.angular.z=0
        snake_walk()

        if is_close_to(snake_members_x[0],goal_x):
            angle_got=snake_members_theta[0]
            break
    goal_hit()

    while not is_close_to(abs(snake_members_theta[0]-angle_got),1.6):

        velocity.linear.x=3
        velocity.angular.z=7
        snake_walk()


    while 1:
        velocity.linear.x=6
        velocity.angular.z=0
        snake_walk()

        if is_close_to(snake_members_y[0],goal_y):
            angle_got=snake_members_theta[0]
            break
    goal_hit()
    while 1:
        velocity.linear.x=3
        velocity.angular.z=7
        snake_walk()

        if is_close_to(snake_members_theta[0],1):
            break


    while 1:
        velocity.linear.x=6
        velocity.angular.z=0
        snake_walk()

        if is_close_to(snake_members_y[0],goal_y):
            break
    goal_hit()

    while 1:
        velocity.linear.x=0
        velocity.angular.z=0
        snake_walk()



def snake():
    global snake_members_x, snake_members_y, snake_members_theta, goal_x, goal_y, r
    global pi,velocity, head, add_turtle, remove_turtle
    global  member1, member2, member3, member4, member5, member6
    global member7,  member8,  member9, velocity1, velocity2

    goal_x=10.5
    goal_y=10
    pi=math.pi
    velocity=Twist()
    velocity1=Twist()
    velocity2=Twist()
    velocity3=Twist()
    velocity4=Twist()
    velocity5=Twist()
    velocity6=Twist()
    velocity7=Twist()
    velocity8=Twist()
    velocity9=Twist()


    i=1
    rospy.init_node('snake_control',anonymous=True)
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    rospy.wait_for_service('kill')
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    remove_turtle("turtle1")
    add_turtle(5.544445, 5.544445,0, "head")
    add_turtle(goal_x, goal_y, pi/2,"goal")
    r=numpy.sqrt((goal_x-5.544445)*(goal_x-5.544445)+(goal_y-5.544445)*(goal_y-5.544445))/2
    snake_members_pub=[]
    snake_members_x=[]
    snake_members_y=[]
    snake_members_theta=[]
    j=0
    while j<10:
        snake_members_x.append(0)
        snake_members_y.append(0)
        snake_members_theta.append(0)
        j+=1
    head=rospy.Publisher("head/cmd_vel", Twist, queue_size=10)

    rospy.Subscriber("/head/pose",Pose, callback_head)
    rospy.sleep(2)
    member1=rospy.Publisher("member1/cmd_vel", Twist, queue_size=10)
    member2=rospy.Publisher("member2/cmd_vel", Twist, queue_size=10)
    member3=rospy.Publisher("member3/cmd_vel", Twist, queue_size=10)
    member4=rospy.Publisher("member4/cmd_vel", Twist, queue_size=10)
    member5=rospy.Publisher("member5/cmd_vel", Twist, queue_size=10)
    member6=rospy.Publisher("member6/cmd_vel", Twist, queue_size=10)
    member7=rospy.Publisher("member7/cmd_vel", Twist, queue_size=10)
    member8=rospy.Publisher("member8/cmd_vel", Twist, queue_size=10)
    member9=rospy.Publisher("member9/cmd_vel", Twist, queue_size=10)

    rospy.Subscriber("/member1/pose", Pose, callback_member1)
    rospy.Subscriber("/member2/pose", Pose, callback_member2)
    rospy.Subscriber("/member3/pose", Pose, callback_member3)
    rospy.Subscriber("/member4/pose", Pose, callback_member4)
    rospy.Subscriber("/member5/pose", Pose, callback_member5)
    rospy.Subscriber("/member6/pose", Pose, callback_member6)
    rospy.Subscriber("/member7/pose", Pose, callback_member7)
    rospy.Subscriber("/member8/pose", Pose, callback_member8)
    rospy.Subscriber("/member9/pose", Pose, callback_member9)

    quantity=input("How many arcs?")
    while i<quantity:
        name="member"+str(i)
        add_turtle((5.544445-i*.5), 5.544445,0, name)
        rospy.sleep(.3)
        i+=1

    head_move()















if __name__ == '__main__':
    try:
        snake()
    except rospy.ROSInterruptException:
        pass
