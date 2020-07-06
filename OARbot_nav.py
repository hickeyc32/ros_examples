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
import threading
pi=math.pi


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
        if goal.x>position_x and not is_close_to(goal.x,position_x):
       
            velocity.linear.x=2
        elif goal.x<position_x and not is_close_to(goal.x,position_x):
      
            velocity.linear.x=-2
        else:
          
            velocity.linear.x=0
            
        if goal.y>position_y and not is_close_to(goal.y,position_y):
           
            velocity.linear.y=2
        elif goal.y<position_y and not is_close_to(goal.y,position_y):
           
            velocity.linear.y=-2
        else:
           
            velocity.linear.y=0

       
        bot.publish(velocity)
        
    

def talk():
    while not rospy.is_shutdown():                   
        print "Current Location: (",position_x ,",",position_y,")"
        rospy.sleep(5)
        
def OARbot_nav():
    global velocity, bot, goal,x,y
    x=0
    y=0
    rospy.init_node('OARbot_control', anonymous=True)
    rate=rospy.Rate(100)
    goal=location(x,y)
    bot=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    arm=rospy.Publisher('/j2n6s300/effort_joint_trajectory_controller/command',JointTrajectory, queue_size=1)
    rospy.Subscriber('/odom',Odometry, pose_callback)
    velocity=Twist()
    jointcmds=[0.0,2.9,1.3,4.2,1.4,0.0]
    jointCmd=JointTrajectory()
    point=JointTrajectoryPoint()
    jointCmd.header.stamp = rospy.Time.now() + rospy.Duration.from_sec(0.0);  
    point.time_from_start = rospy.Duration.from_sec(5.0)

    for i in range(0, 6):
        jointCmd.joint_names.append('j2n6s300_joint_'+str(i+1))
        point.positions.append(jointcmds[i])
        point.velocities.append(5)
        point.accelerations.append(0)
        point.effort.append(0)
    jointCmd.points.append(point)
    rospy.sleep(2)
    key=raw_input("ready?")
    x=float(raw_input("Where to?"))
    y=float(raw_input())
    goal=location(x,y)
    walk_thread=threading.Thread(target=walk, args=())
    walk_thread.start()
    talk_thread=threading.Thread(target=talk, args=())
    talk_thread.start()
    rospy.sleep(1)

    while not rospy.is_shutdown():                   
        x=float(raw_input("Where to?"))
        y=float(raw_input())
        goal=location(x,y)    
  
        rospy.sleep(1)
      


try:
    OARbot_nav()
except rospy.ROSInterruptException:
    pass



