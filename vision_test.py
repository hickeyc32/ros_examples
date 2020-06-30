#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from sensor_msgs.msg import Image
import numpy
import math
import sys
import cv2
from matplotlib import pyplot
from cv_bridge import CvBridge, CvBridgeError




#STEPS FOR CAMERA CONTROL:
#1. HOLD UP OBJECT IN FRONT OF WEBCAM WITH ROS CAM
#2. WAIT 5 SECONDS
#3. TAKE picture and convert to opencv
#4. ANALYZE IMAGE FOR CONTROL RESPONSE
#5. EXECUTE CONTROL

angle=0
bridge = CvBridge()
#current_image=cv2.imread('INSERT_ERROR_PIC',1) #In case of camera read failure, put a desired error picture path here
x_current=5.544445
y_current=5.544445

def wait_5_sec():

    print "5"
    rospy.sleep(1)
    print "4"
    rospy.sleep(1)
    print "3"
    rospy.sleep(1)
    print "2"
    rospy.sleep(1)
    print "1"
    rospy.sleep(1)
    print "Image Captured"

def pose_callback(position): #Constantly updates global coordinates
    global angle
    global x_current
    global y_current
    angle = position.theta
    x_current=position.x
    y_current=position.y

def camera_callback(picture):
    global current_image
    current_image = bridge.imgmsg_to_cv2(picture, "passthrough")

def identify_pattern(pattern):
    global x_goal
    global y_goal
    global angle_goal
    x_avg=0
    y_avg=0
    #image = cv2.imread(pattern,1)
    square_corners = cv2.goodFeaturesToTrack(cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY), 4, 0.1, 3)

    for current_corner in square_corners:
        x_current, y_current=current_corner.ravel()
        x_avg+=x_current
        y_avg+=y_current

    x_dot=x_avg/4
    y_dot=y_avg/4
    x_goal=x_avg/4*12/630
    y_goal=470-y_avg/4
    y_goal=y_goal*12/470


    if x_goal>11:
        x_goal=11
    if y_goal>11:
        y_goal=11

    pyplot.scatter(x_dot,y_dot,color='r')
    pyplot.imshow(pattern)
    pyplot.show()
    print "Determined Coordinates are: (",x_goal,",",y_goal,")"

def analyze_image():
    wait_5_sec()
    identify_pattern(current_image)

def walk():

    if x_goal>5.544445 and y_goal> 5.544445:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current>=x_goal and y_current>=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)
                print "Current Coordinates: (", x_current,",",y_current,")"
                break

    elif x_goal<5.544445 and y_goal> 5.544445:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current<=x_goal and y_current>=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)
                print "Current Coordinates: (", x_current,",",y_current,")"
                break

    elif x_goal<5.544445 and y_goal<5.544445:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current<=x_goal and y_current<=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)
                print "Current Coordinates: (", x_current,",",y_current,")"
                break

    elif x_goal>5.544445 and y_goal<5.544445:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current>=x_goal and y_current<=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)
                print "Current Coordinates: (", x_current,",",y_current,")"
                break

def turn_to_point():

    quadrant=1
    x=abs(x_goal-5.544445)
    y=abs(y_goal-5.544445)

    if x_goal>5.544445and y_goal>5.544445:
        quadrant=1
        angle_goal=math.atan(y/x)
#        print angle_goal, "in quadrant: ",quadrant
        while 1:
            vel.angular.z=1
            pub.publish(vel)
            if angle>=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)
    #            print "Current Angle: ", angle
                break

    elif x_goal<5.544445and y_goal>5.544445:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            vel.angular.z=1
            pub.publish(vel)
            if angle>=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)
            #    print "Current Angle: ", angle
                break

    elif x_goal<5.544445and y_goal<5.544445:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            vel.angular.z=-1
            pub.publish(vel)

            if angle<=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)
        #        print  "Current Angle: ", angle
                break

    elif x_goal>5.544445and y_goal<5.544445:
        quadrant=4
        angle_goal=-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            vel.angular.z=-1
            pub.publish(vel)

            if angle<=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)
        #        print "Current Angle: ", angle
                break
    walk()

def turn_to_center():
    x_goal=5.544445
    y_goal=5.544445
    global x_end
    global y_end
    x_end=x_current
    y_end=y_current
    quadrant=1
    x=abs(x_end-5.544445)
    y=abs(y_end-5.544445)

    print "Returning home..."
    if x_goal>x_end and y_goal>y_end:
        quadrant=1
        angle_goal=math.atan(y/x)

        while 1:
            vel.angular.z=1
            pub.publish(vel)
            if angle>=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal<x_end and y_goal>y_end:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)

        while 1:
            vel.angular.z=1
            pub.publish(vel)
            if angle>=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal<x_end and y_goal<y_end:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)

        while 1:
            vel.angular.z=-1
            pub.publish(vel)

            if angle<=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal>x_end and y_goal<y_end:
        quadrant=4
        angle_goal=-math.atan(y/x)

        while 1:
            vel.angular.z=-1
            pub.publish(vel)

            if angle<=angle_goal:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break


    walk_to_center()

    if quadrant==1 or quadrant==2:
        while 1:
            vel.angular.z=-1
            pub.publish(vel)
            if angle<=0:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    else:
        while 1:
            vel.angular.z=1
            pub.publish(vel)
            if angle>=0:
                vel.angular.z=0
                pub.publish(vel)
                rospy.sleep(1)

                break



    print "Back at home, restarting..."
    rospy.sleep(3)

def walk_to_center():
    x_goal=5.544445
    y_goal=5.544445
    if x_goal>x_end and y_goal> y_end:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current>=x_goal and y_current>=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal<x_end and y_goal> y_end:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current<=x_goal and y_current>=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal<x_end and y_goal<y_end:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current<=x_goal and y_current<=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)

                break

    elif x_goal>x_end and y_goal<y_end:
        while 1:
            vel.linear.x=1
            pub.publish(vel)
            if x_current>=x_goal and y_current<=y_goal:
                vel.linear.x=0
                pub.publish(vel)
                rospy.sleep(1)

                break

def vision_test():
    global vel
    global pub
    rospy.init_node('vision_test', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub_pose = rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    sub_cam = rospy.Subscriber('/camera_feed/image_raw', Image, camera_callback)
    rate = rospy.Rate(10)
    vel = Twist()
    x_goal=5.544445
    y_goal=5.544445
    key='r'

    while 1:


        analyze_image()
        key=raw_input("Is this picture good enough? (y/n)")
        while key=='n':
            analyze_image()
            key=raw_input("Is this picture good enough? (y/n)")
        x_goal=10
        y_goal=10
        turn_to_point()
        key=raw_input("Press any key when ready, q to quit")
        if key=='q':
            break
        else:
            turn_to_center()

if __name__ == '__main__':
    try:
        vision_test()
    except rospy.ROSInterruptException:
        pass
