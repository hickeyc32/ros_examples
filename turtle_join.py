#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
import multiprocessing
import threading
pi=math.pi


def is_close_to(a,b):
    if a<b and a+1>=b: #Change constant for collision range, evasion distance should be around 2-2.3
        return True
    if a>b and a-1<b:
        return True
    else:
        return False

def is_colliding(p1,p2):
    if is_close_to(p1.x,p2.x) and is_close_to(p1.y,p2.y):
        return True
    else:
        return False

def first_turtle_run():
    global joined1
    joined1=0

    while not rospy.is_shutdown():

        while not joined1:
            velocity1.angular.z=4
            pub1.publish(velocity1)
            if pos1.theta>3.1 or pos1.theta<0:
                joined1=1 or pos1.theta<0
                break

        velocity1.angular.z=2
        velocity1.linear.x=velocity1.angular.z*r
        pub1.publish(velocity1)


def second_turtle_run():
    global joined2
    joined2=0
    ended2=0
    while not rospy.is_shutdown():
        while not joined2:
            if is_colliding(pos2,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity2.angular.z=0
                velocity2.linear.x=0
                pub2.publish(velocity3)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity2.linear.x=lin_vel
                velocity2.angular.z=4
                pub2.publish(velocity2)
            if pos2.theta>3.1 or pos2.theta<0:
                joined2=1
                break

        velocity2.angular.z=2
        velocity2.linear.x=velocity2.angular.z*r
        pub2.publish(velocity2)

def third_turtle_run():
    global joined3
    joined3=0
    while not rospy.is_shutdown():
        while not joined3:
            if is_colliding(pos3,pos2) or is_colliding(pos3,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity3.angular.z=0
                velocity3.linear.x=0
                pub3.publish(velocity3)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity3.linear.x=lin_vel
                velocity3.angular.z=4
                pub3.publish(velocity3)
            if pos3.theta>3.1:
                joined3=1
                break


        velocity3.angular.z=2
        velocity3.linear.x=velocity3.angular.z*r
        pub3.publish(velocity3)


def fourth_turtle_run():
    global joined4
    joined4=0
    while not rospy.is_shutdown():
        while not joined4:
            if is_colliding(pos4,pos3) or is_colliding(pos4,pos2) or is_colliding(pos4,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity4.angular.z=0
                velocity4.linear.x=0
                pub4.publish(velocity4)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity4.linear.x=lin_vel
                velocity4.angular.z=4
                pub4.publish(velocity4)
            if pos4.theta>3.1:
                joined4=1
                break

        velocity4.angular.z=2
        velocity4.linear.x=velocity4.angular.z*r
        pub4.publish(velocity4)

def fifth_turtle_run():
    global joined5
    joined5=0
    while not rospy.is_shutdown():
        while not joined5:
            if is_colliding(pos5,pos4) or is_colliding(pos5,pos3) or is_colliding(pos5,pos2) or is_colliding(pos5,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity5.angular.z=0
                velocity5.linear.x=0
                pub5.publish(velocity5)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity5.linear.x=lin_vel
                velocity5.angular.z=4
                pub5.publish(velocity5)
            if pos5.theta>3.1:
                joined5=1
        velocity5.angular.z=2
        velocity5.linear.x=velocity5.angular.z*r
        pub5.publish(velocity5)

def sixth_turtle_run():
    global joined6
    joined6=0
    while not rospy.is_shutdown():
        while not joined6:
            if is_colliding(pos6,pos5) or is_colliding(pos6,pos4) or is_colliding(pos6,pos3) or is_colliding(pos6,pos2) or is_colliding(pos6,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity6.angular.z=0
                velocity6.linear.x=0
                pub6.publish(velocity6)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity6.linear.x=lin_vel
                velocity6.angular.z=4
                pub6.publish(velocity6)
            if pos6.theta>3.1:
                joined6=1
        velocity6.angular.z=2
        velocity6.linear.x=velocity6.angular.z*r
        pub6.publish(velocity6)


def seventh_turtle_run():
    global joined7
    joined7=0
    while not rospy.is_shutdown():
        while not joined7:
            if is_colliding(pos7,pos6) or  is_colliding(pos7,pos5) or is_colliding(pos7,pos4) or is_colliding(pos7,pos3) or is_colliding(pos7,pos2) or is_colliding(pos7,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity7.angular.z=0
                velocity7.linear.x=0
                pub7.publish(velocity7)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity7.linear.x=lin_vel
                velocity7.angular.z=4
                pub7.publish(velocity7)
            if pos7.theta>3.1:
                joined7=1
        velocity7.angular.z=2
        velocity7.linear.x=velocity7.angular.z*r
        pub7.publish(velocity7)


def eighth_turtle_run():
    global joined8
    joined8=0
    while not rospy.is_shutdown():
        while not joined8:
            if is_colliding(pos8,pos7) or is_colliding(pos8,pos6) or  is_colliding(pos8,pos5) or is_colliding(pos8,pos4) or is_colliding(pos8,pos3) or is_colliding(pos8,pos2) or is_colliding(pos8,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity8.angular.z=0
                velocity8.linear.x=0
                pub8.publish(velocity8)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity8.linear.x=lin_vel
                velocity8.angular.z=4
                pub8.publish(velocity8)
            if pos8.theta>3.1:
                joined8=1
        velocity8.angular.z=2
        velocity8.linear.x=velocity8.angular.z*r
        pub8.publish(velocity8)

def ninth_turtle_run():
    global joined9
    joined9=0
    while not rospy.is_shutdown():
        while not joined9:
            if is_colliding(pos9,pos8) or is_colliding(pos9,pos7) or is_colliding(pos9,pos6) or  is_colliding(pos9,pos5) or is_colliding(pos9,pos4) or is_colliding(pos9,pos3) or is_colliding(pos9,pos2) or is_colliding(pos9,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity9.angular.z=0
                velocity9.linear.x=0
                pub9.publish(velocity9)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity9.linear.x=lin_vel
                velocity9.angular.z=4
                pub9.publish(velocity9)
            if pos9.theta>3.1:
                joined9=1
        velocity9.angular.z=2
        velocity9.linear.x=velocity9.angular.z*r
        pub9.publish(velocity9)

def tenth_turtle_run():
    global joined10
    joined10=0
    while not rospy.is_shutdown():
        while not joined10:
            if is_colliding(pos10,pos9) or is_colliding(pos10,pos8) or is_colliding(pos10,pos7) or is_colliding(pos10,pos6) or  is_colliding(pos10,pos5) or is_colliding(pos10,pos4) or is_colliding(pos10,pos3) or is_colliding(pos10,pos2) or is_colliding(pos10,pos1):
                print "\n\nCOLLISION DETECTED"
                velocity10.angular.z=0
                velocity10.linear.x=0
                pub10.publish(velocity10)
                rospy.sleep(2)
                print "\n\nAVERTED COLLISION"
            else:
                velocity10.linear.x=lin_vel
                velocity10.angular.z=4
                pub10.publish(velocity10)
            if pos10.theta>3.1:
                joined10=1
        velocity10.angular.z=2
        velocity10.linear.x=velocity10.angular.z*r
        pub10.publish(velocity10)



def callback1(pos):
    global pos1,d1
    pos1=pos
def callback2(pos):
    global pos2
    pos2=pos



def callback3(pos):
    global pos3
    pos3=pos

def callback4(pos):
    global pos4
    pos4=pos

def callback5(pos):
    global pos5
    pos5=pos
def callback6(pos):
    global pos6
    pos6=pos
def callback7(pos):
    global pos7
    pos7=pos
def callback8(pos):
    global pos8
    pos8=pos
def callback9(pos):
    global pos9
    pos9=pos
def callback10(pos):
    global pos10
    pos10=pos

def multi_test():
    global velocity1, velocity2, velocity3, velocity4, velocity5,velocity6
    global velocity7,velocity8,velocity9,velocity10
    global joined1, joined2,joined3,joined4,joined5,joined6,joined7
    global joined8,joined9,joined10
    global pub1,pub2,pub3,pub4,pub5,pub6,pub7,pub8,pub9,pub10,r, initial_x
    global initial_y, lin_vel
    global pos1,pos2,pos3, pos4, pos5, pos6, pos7,pos8,pos9,pos10
    global turtle_count
    global ended1, ended2
    ended1=False
    ended2=False
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
    turtle_count=1
    initial_x=5.544445
    initial_y=5.544445
    initial_theta=0
    rospy.init_node('turtle_join_control',anonymous=True)
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)

    pub1=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pub2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
    pub3=rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
    pub4=rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=10)
    pub5=rospy.Publisher('turtle5/cmd_vel', Twist, queue_size=10)
    pub6=rospy.Publisher('turtle6/cmd_vel', Twist, queue_size=10)
    pub7=rospy.Publisher('turtle7/cmd_vel', Twist, queue_size=10)
    pub8=rospy.Publisher('turtle8/cmd_vel', Twist, queue_size=10)
    pub9=rospy.Publisher('turtle9/cmd_vel', Twist, queue_size=10)
    pub10=rospy.Publisher('turtle10/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, callback1)
    rospy.Subscriber('/turtle2/pose',Pose, callback2)
    rospy.Subscriber('/turtle3/pose',Pose, callback3)
    rospy.Subscriber('/turtle4/pose',Pose, callback4)
    rospy.Subscriber('/turtle5/pose',Pose, callback5)
    rospy.Subscriber('/turtle6/pose',Pose, callback6)
    rospy.Subscriber('/turtle7/pose',Pose, callback7)
    rospy.Subscriber('/turtle8/pose',Pose, callback8)
    rospy.Subscriber('/turtle9/pose',Pose, callback9)
    rospy.Subscriber('/turtle10/pose',Pose, callback10)
    velocity1=Twist()
    velocity2=Twist()
    velocity3=Twist()
    velocity4=Twist()
    velocity5=Twist()
    velocity6=Twist()
    velocity7=Twist()
    velocity8=Twist()
    velocity9=Twist()
    velocity10=Twist()



    r=input("Input circle radius: ")
    if r>5:
        r=5
    velocity1.angular.z=2
    velocity1.linear.x=velocity1.angular.z*r
    lin_vel=velocity1.linear.x



    p1 = threading.Thread(target=first_turtle_run, args=())
    p1.start()

    while not rospy.is_shutdown():
        key=raw_input("Press A to add a Turtle, or R to Remove a  Turtle")
        if key=='a':
            if turtle_count==0:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle1')
                p1 = threading.Thread(target=first_turtle_run, args=())
                velocity1.angular.z=2
                velocity1.linear.x=velocity1.angular.z*r
                p1.start()
            elif turtle_count==1:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle2')
                p2 = threading.Thread(target=second_turtle_run, args=())
                velocity2.angular.z=2
                velocity2.linear.x=velocity2.angular.z*r
                p2.start()
            elif turtle_count==2:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle3')
                p3 = threading.Thread(target=third_turtle_run, args=())
                velocity3.angular.z=2
                velocity3.linear.x=velocity3.angular.z*r
                p3.start()
            elif turtle_count==3:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle4')
                p4 = threading.Thread(target=fourth_turtle_run, args=())
                velocity4.angular.z=2
                velocity4.linear.x=velocity4.angular.z*r
                p4.start()
            elif turtle_count==4:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle5')
                p5 = threading.Thread(target=fifth_turtle_run, args=())
                velocity5.angular.z=2
                velocity5.linear.x=velocity5.angular.z*r
                p5.start()
            elif turtle_count==5:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle6')
                p6 = threading.Thread(target=sixth_turtle_run, args=())
                velocity6.angular.z=2
                velocity6.linear.x=velocity6.angular.z*r
                p6.start()
            elif turtle_count==6:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle7')
                p7 = threading.Thread(target=seventh_turtle_run, args=())
                velocity7.angular.z=2
                velocity7.linear.x=velocity7.angular.z*r
                p7.start()
            elif turtle_count==7:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle8')
                p8 = threading.Thread(target=eighth_turtle_run, args=())
                velocity8.angular.z=2
                velocity8.linear.x=velocity8.angular.z*r
                p8.start()
            elif turtle_count==8:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle9')
                p9 = threading.Thread(target=ninth_turtle_run, args=())
                velocity9.angular.z=2
                velocity9.linear.x=velocity9.angular.z*r
                p9.start()
            elif turtle_count==9:
                turtle_count+=1
                add_turtle(initial_x, initial_y, initial_theta,'turtle10')
                p10 = threading.Thread(target=tenth_turtle_run, args=())
                velocity10.angular.z=2
                velocity10.linear.x=velocity10.angular.z*r
                p10.start()
            else:
                print "MAX TURTLES ADDED"





        elif key=='r':
            if turtle_count==1:

                remove_turtle("turtle1")
                turtle_count-=1
                ended1=True

            elif turtle_count==2:
                remove_turtle("turtle2")
                turtle_count-=1

                ended2=True
            elif turtle_count==3:
                remove_turtle("turtle3")
                turtle_count-=1
                joined3=0

            elif turtle_count==4:
                remove_turtle("turtle4")
                turtle_count-=1
                joined4=0

            elif turtle_count==5:
                remove_turtle("turtle5")
                turtle_count-=1
                joined5=0

            elif turtle_count==6:
                remove_turtle("turtle6")
                turtle_count-=1
                joined6=0

            elif turtle_count==7:
                remove_turtle("turtle7")
                turtle_count-=1
                joined7=0

            elif turtle_count==8:
                remove_turtle("turtle8")
                turtle_count-=1
                joined8=0

            elif turtle_count==9:
                remove_turtle("turtle9")
                turtle_count-=1
                joined9=0

            elif turtle_count==10:
                remove_turtle("turtle10")
                turtle_count-=1
                joined10=0

            else:
                print "NO TURTLES TO REMOVE"


        else:
            pass




if __name__ == '__main__':
    try:
        multi_test()
    except rospy.ROSInterruptException:
        pass
