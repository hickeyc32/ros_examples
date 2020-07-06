#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from kinova_msgs.msg import PoseVelocity
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from threading import Thread
import pygame



class location:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        


def is_close_to(a,b):
    if a<b and a+.05>=b:
        return True
    if a>b and a-.05<b:
        return True
    else:
        return False



def pose_callback(pos):
    global position_x, position_y, ang_vel, d
    position_x = pos.pose.pose.position.x
    position_y = pos.pose.pose.position.y
    ang_vel=pos.pose.pose.orientation.w
    
    if is_close_to(position_x,goal.x) and is_close_to(position_y,goal.y):
        velocity.linear.x=0
        velocity.linear.y=0
  
def walk():
    global velocity
    while not rospy.is_shutdown():     
        bot.publish(velocity)
        
        
    

def talk():
    while not rospy.is_shutdown():                   
        print "Current Location: (",position_x ,",",position_y,")"
        rospy.sleep(5)
        
def OARbot_nav():
    global velocity, bot, goal,x,y
    x=100
    y=100
    goal=location(x,y)
    rospy.init_node('OARbot_control', anonymous=True)
    rate=rospy.Rate(100)
    goal=location(x,y)
    bot=rospy.Publisher('/cmd_vel', Twist, queue_size=10)   
    velocity=Twist()
    t1=Thread(target=walk, args=())
    t1.start()
    rospy.sleep(2)
    key=raw_input("ready?")      
    rospy.sleep(1)
    pygame.init()
    screen = pygame.display.set_mode((1920, 100))
    pygame.display.set_caption("Control From Here")

    pygame.key.set_repeat(1,1)

    while not rospy.is_shutdown():                   
        for event in pygame.event.get():
                state = pygame.key.get_pressed()
                if state[pygame.K_w]:
                        velocity.linear.x=-1
                      

                elif state[pygame.K_a]:
                        velocity.linear.y=-1
                       
                
                elif state[pygame.K_s]:
                        velocity.linear.x=1
                    

                elif state[pygame.K_d]:
                        velocity.linear.y=1
                                                         
                elif event.type==pygame.MOUSEMOTION:
                        if pygame.mouse.get_rel()[0]>0:
                                velocity.angular.z=-3
                               
                        else:
                                velocity.angular.z=3
                               
            
                else:
                    
                    velocity.linear.x=0
                    velocity.linear.y=0
                    velocity.angular.z=0

#pygame.quit()


try:
    OARbot_nav()
except rospy.ROSInterruptException:
    pass



