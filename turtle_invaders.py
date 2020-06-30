#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
import getpass
import threading
pi=math.pi

def is_close_to(a,b):
    if a<b and a+.3>=b:
        return True
    if a>b and a-.3<b:
        return True
    else:
        return False

def is_colliding(p1,p2):
    if is_close_to(p1.x,p2.x) and is_close_to(p1.y,p2.y):
        return True
    else:
        return False

def march():
    while not rospy.is_shutdown():
        velocity_march.linear.x=.25
        pub3.publish(velocity_march)
        pub4.publish(velocity_march)
        pub5.publish(velocity_march)
        pub6.publish(velocity_march)
        pub10.publish(velocity_march)
        pub11.publish(velocity_march)
        rospy.sleep(1)
        pub7.publish(velocity_march)
        pub8.publish(velocity_march)
        pub9.publish(velocity_march)

        pub12.publish(velocity_march)
        pub13.publish(velocity_march)
        rospy.sleep(1)

def player_move():
    while not rospy.is_shutdown():
        player_pub.publish(velocity_player)



def callback_player(pos):
    global pos1
    pos1=pos

    if pos1.x<=1 or pos1.x>=11:
      velocity_player.linear.x=0

def callback_bullet(pos):
    global pos2
    pos2=pos
    velocity_bullet.linear.x=9
    bullet_pub.publish(velocity_bullet)
    if pos2.y>=10:

        remove_turtle("bullet")
        pos2.y=launch_point
        velocity_bullet.linear.x=9
        bullet_pub.publish(velocity_bullet)


#3-9 are the marching enemies
def callback3(pos):
    global pos3
    pos3=pos

    if is_colliding(pos3,pos2):
        remove_turtle("turtle3")


def callback4(pos):
    global pos4
    pos4=pos
    if is_colliding(pos4,pos2):
        remove_turtle("turtle4")

def callback5(pos):
    global pos5
    pos5=pos
    if is_colliding(pos5,pos2):
        remove_turtle("turtle5")

def callback6(pos):
    global pos6
    pos6=pos
    if is_colliding(pos6,pos2):
        remove_turtle("turtle6")

def callback7(pos):
    global pos7
    pos7=pos
    if is_colliding(pos7,pos2):
        remove_turtle("turtle7")

def callback8(pos):
    global pos8
    pos8=pos
    if is_colliding(pos8,pos2):
        remove_turtle("turtle8")

def callback9(pos):
    global pos9
    pos9=pos
    if is_colliding(pos9,pos2):
        remove_turtle("turtle9")

def callback10(pos):
    global pos10
    pos10=pos
    if is_colliding(pos10,pos2):
        remove_turtle("turtle10")

def callback11(pos):
    global pos11
    pos11=pos
    if is_colliding(pos11,pos2):
        remove_turtle("turtle11")


def callback12(pos):
    global pos12
    pos12=pos
    if is_colliding(pos12,pos2):
        remove_turtle("turtle12")


def callback13(pos):
    global pos13
    pos13=pos
    if is_colliding(pos11,pos2):
        remove_turtle("turtle11")


def turtle_invaders():

    global velocity_march, player_pub, velocity_player, velocity_bullet,bullet_pub
    global pub3,pub4,pub5,pub6,pub7,pub8,pub9, remove_turtle,pos1,pos2,pos3
    global pos4,pos5,pos6,pos7,pos8,pos9, pos10,pos11,pos12,pos13,pub10,pub11
    global pub12,pub13,launch_point
    pos1=Pose()
    pos2=Pose()
    pos3=Pose()
    pos4=Pose()
    pos5=Pose()
    pos6=Pose()
    pos7=Pose()
    pos8=Pose()
    pos9=Pose()
    pos10=Pose()
    pos11=Pose()
    pos12=Pose()
    pos13=Pose()
    rospy.init_node('turtle_invaders',anonymous=True)
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    remove_turtle("turtle1")
    add_turtle(5.544445,.5,0,"player")
    player_pub=rospy.Publisher('player/cmd_vel', Twist, queue_size=10)
    bullet_pub=rospy.Publisher('bullet/cmd_vel', Twist, queue_size=10)
    pub3=rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
    pub4=rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=10)
    pub5=rospy.Publisher('turtle5/cmd_vel', Twist, queue_size=10)
    pub6=rospy.Publisher('turtle6/cmd_vel', Twist, queue_size=10)
    pub7=rospy.Publisher('turtle7/cmd_vel', Twist, queue_size=10)
    pub8=rospy.Publisher('turtle8/cmd_vel', Twist, queue_size=10)
    pub9=rospy.Publisher('turtle9/cmd_vel', Twist, queue_size=10)
    pub10=rospy.Publisher('turtle10/cmd_vel', Twist, queue_size=10)
    pub11=rospy.Publisher('turtle11/cmd_vel', Twist, queue_size=10)
    pub12=rospy.Publisher('turtle12/cmd_vel', Twist, queue_size=10)
    pub13=rospy.Publisher('turtle13/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/player/pose',Pose, callback_player)

    rospy.Subscriber('/turtle3/pose',Pose, callback3)
    rospy.Subscriber('/turtle4/pose',Pose, callback4)
    rospy.Subscriber('/turtle5/pose',Pose, callback5)
    rospy.Subscriber('/turtle6/pose',Pose, callback6)
    rospy.Subscriber('/turtle7/pose',Pose, callback7)
    rospy.Subscriber('/turtle8/pose',Pose, callback8)
    rospy.Subscriber('/turtle9/pose',Pose, callback9)
    rospy.Subscriber('/turtle10/pose',Pose, callback10)
    rospy.Subscriber('/turtle11/pose',Pose, callback11)
    rospy.Subscriber('/turtle12/pose',Pose, callback12)
    rospy.Subscriber('/turtle13/pose',Pose, callback13)

    velocity_player=Twist()
    velocity_bullet=Twist()
    velocity_march=Twist()
    velocity_bullet.linear.x=9
    bullet_pub.publish(velocity_bullet)


    ready=raw_input("Ready?")
    if ready:
        pass
    print"\n\n"
    add_turtle(2.5,10.5,-pi/2,"turtle3")
    add_turtle(4.5,10.5,-pi/2,"turtle4")
    add_turtle(6.5,10.5,-pi/2,"turtle5")
    add_turtle(8.5,10.5,-pi/2,"turtle6")
    add_turtle(.5,10.5,-pi/2,"turtle10")
    add_turtle(10.5,10.5,-pi/2,"turtle11")

    add_turtle(3.5,8.5,-pi/2,"turtle7")
    add_turtle(5.5,8.5,-pi/2,"turtle8")
    add_turtle(7.5,8.5,-pi/2,"turtle9")
    add_turtle(1.5,8.5,-pi/2,"turtle12")
    add_turtle(9.5,8.5,-pi/2,"turtle13")
    rospy.sleep(2)

    player_thread = threading.Thread(target=player_move, args=())
    player_thread.start()
    march_thread=threading.Thread(target=march, args=())
    march_thread.start()
    print "a for left, d for right, s for stop, w for shoot"
    while not rospy.is_shutdown():


        launch_point=pos1.x

        key=getpass.getpass('')
        if key=='d':
            velocity_player.linear.x=5


        elif key=='a':

            velocity_player.linear.x=-5


        elif key=='s':
            velocity_player.linear.x=0


        elif key=='w':

            add_turtle(launch_point, .5, pi/2,'bullet')
            rospy.Subscriber('/bullet/pose',Pose, callback_bullet)




        else:
            pass





    rospy.spin()







if __name__ == '__main__':
    try:
        turtle_invaders()
    except rospy.ROSInterruptException:
        pass
