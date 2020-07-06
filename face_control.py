#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import math
import time
import numpy
from nav_msgs.msg import Odometry
from threading import Thread
import cv2
from matplotlib import pyplot
from cv_bridge import CvBridge, CvBridgeError
pi=math.pi
#CHANGE FOR PATH TO HAARCASCADES THAT COME WITH OPENCV
face_cascade=cv2.CascadeClassifier('/home/chris/opencv_build/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('/home/chris/opencv_build/opencv/data/haarcascades/haarcascade_smile.xml')
vid=cv2.VideoCapture(0)


def pose_callback(pos):
    global position_x, position_y, ang_vel
    position_x = pos.pose.pose.position.x
    position_y = pos.pose.pose.position.y
    ang_vel=pos.pose.pose.orientation.w

def face_detect():
    global velocity,bot
    while not rospy.is_shutdown():
        choice=3
        check, pic = vid.read()   
        gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        velocity.linear.x=0
        velocity.angular.z=5
       
        for (x,y,w,h) in face:
            
            pic =cv2.putText(pic,"Face",(x+40,y+100), cv2. FONT_HERSHEY_PLAIN,4,(200,0,500),2)
            bwimage = gray[y:y+h, x:x+w]
            feed = pic[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(bwimage)
            if face.size>0:
                choice=1
                
            for (a,b,ew,eh) in smile:
                cv2.putText(feed,"Smile",(a-40,b+100), cv2.FONT_HERSHEY_PLAIN,2,(500,500,500),2)
        
                if smile.size>0:
                    choice=2
                    velocity.linear.x=5
                    velocity.angular.z=0
                        
        if choice==1:               
            velocity.linear.x=-5
            velocity.angular.z=0
               
        elif choice==2:
            velocity.linear.x=5
            velocity.angular.z=0
        else:
            pass
      
        bot.publish(velocity)
        cv2.imshow('say_cheese',pic)
        cv2.waitKey(1)
  


        
def face_control():
    global velocity, bot, velocity1
    rospy.init_node('smile_control', anonymous=True)
    rate=rospy.Rate(100)
    bot=rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.Subscriber('/odom',Odometry, pose_callback)
    velocity=Twist()
    velocity1=Twist()
    velocity1.linear.x=-5
    velocity1.angular.z=0
    
    key=raw_input()
    print "Face moves forward, Smile moves back, No Face spins" 
    key=raw_input()
    while not rospy.is_shutdown():
     
        face_detect()
     
        




try:
    face_control()
except rospy.ROSInterruptException:
    pass



