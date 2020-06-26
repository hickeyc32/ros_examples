#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
flag=0

pi=math.pi



def is_close_to(a,b):
    if a<b and a+.8>=b: #Change constant for collision range, evasion distance should be around 2-2.3
        return True
    if a>b and a-.8<b:
        return True
    else:
        return False




def callback1(pos):
    global pos1,d1
    pos1=pos



def callback2(pos):
    global pos2
    pos2=pos

    if is_close_to(pos1.x,pos2.x): #is_close_to is continously called, and if the turtles are too close, they're
        velocity1.linear.x=0       #Change based on desired velocity in collision scenario
        velocity2.linear.x=0

        #Uncomment for evade
        #velocity1.linear.x=2
        #evade()





def evade():
    global velocity2,flag
    velocity2.linear.x=3
    if not flag:        #flagged if run more than once, can change for amount of evasions desired

        velocity2.angular.z=4
        rospy.sleep(.3)
        velocity2.angular.z=-4
        rospy.sleep(.28)
        velocity2.angular.z=0
        flag=1

def collision_test():

    global velocity1, velocity2, pub1,pub2,pos1,pos2
    pos1=Pose()
    pos2=Pose()
    pos1.x=10
    pos2.x=1.08889
    pos1.y=5.544445
    pos2.y=5.544445
    rospy.init_node('turtle_circle_control',anonymous=True)
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    remove_turtle("turtle1")
    add_turtle(pos1.x, pos1.y, -pi, 'turtle1')
    add_turtle(pos2.x, pos2.y, 0, 'turtle2')
    pub1=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pub2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, callback1)
    rospy.Subscriber('/turtle2/pose',Pose, callback2)
    velocity1=Twist()
    velocity2=Twist()


    velocity1.linear.x=3
    velocity2.linear.x=3
    rospy.sleep(1)

    while not rospy.is_shutdown():
        pub1.publish(velocity1)
        pub2.publish(velocity2)




if __name__ == '__main__':
    try:
        collision_test()
    except rospy.ROSInterruptException:
        pass
