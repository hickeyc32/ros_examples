#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from sensor_msgs.msg import Image
import turtlesim.srv
import numpy
import math
import sys
import cv2
from matplotlib import pyplot
from cv_bridge import CvBridge, CvBridgeError

angle=0
bridge = CvBridge()
x_current=5.544445
y_current=5.544445

def analyze_image():
    wait_3_sec()
    identify_pattern(current_image)

def analyze_image_triangle():
    wait_3_sec()
    identify_pattern_triangle(current_image)

def analyze_image_square():
    wait_3_sec()
    identify_pattern_square(current_image)



def wait_3_sec():

    print "3"
    rospy.sleep(1)
    print "2"
    rospy.sleep(1)
    print "1"
    rospy.sleep(1)
    print "Image Captured"

def camera_callback(picture):
    global current_image
    current_image = bridge.imgmsg_to_cv2(picture, "passthrough")

def identify_pattern_square(pattern):
    global x_goal, x_goal_top
    global y_goal, y_goal_top
    global angle_goal, angle_goal_top, angle_goal_left, angle_goal_right
    global point_array


    x_avg=0
    y_avg=0
    i=0
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
        x_goal=12
    if y_goal>11:
        y_goal=12


    x_goal_top=x_goal
    y_goal_top=y_goal




    pyplot.scatter(x_dot,y_dot,color='r')
    pyplot.imshow(pattern)
    pyplot.show()
    print "Centered Coordinates are: (",x_goal,",",y_goal,")"

def identify_pattern_triangle(pattern):
    global x_goal, x_goal_top, x_goal_left, x_goal_right
    global y_goal, y_goal_top, y_goal_left, y_goal_right
    global angle_goal, angle_goal_top, angle_goal_left, angle_goal_right



    x_avg=0
    y_avg=0
    i=0
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
        x_goal=12
    if y_goal>11:
        y_goal=12


    x_goal_top=x_goal
    y_goal_top=y_goal


    x_goal_left=x_goal-1
    y_goal_left=y_goal+1
    x_goal_right=x_goal+1
    y_goal_right=y_goal+1


    pyplot.scatter(x_dot,y_dot,color='r')
    pyplot.imshow(pattern)
    pyplot.show()
    print "Centered Coordinates are: (",x_goal,",",y_goal,")"


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
        x_goal=12
    if y_goal>11:
        y_goal=12

    pyplot.scatter(x_dot,y_dot,color='r')
    pyplot.imshow(pattern)
    pyplot.show()
    print "Determined Coordinates are: (",x_goal,",",y_goal,")"

def is_close_to(a,b):
    if a<b and a+.1>=b:
        return True
    if a>b and a-.1<=b:
        return True
    else:
        return False

def callback1(pos1):
    global position1
    position1=pos1

def callback2(pos2):
    global position2
    position2=pos2

def callback3(pos3):
    global position3
    position3=pos3

def callback4(pos4):
    global position4
    position4=pos4

def callback5(pos5):
    global position5
    position5=pos5

def walk_grabber():
    global turtle1,turtle2,turtle3,turtle4,turtle5, pi
    global velocity1,velocity2, velocity3, velocity4, velocity5
    global x_goal, y_goal
    global add_turtle

    if x_goal>5.544445 and y_goal> 5.544445:
        while 1:
            velocity1.linear.x=1
            turtle1.publish(velocity1)
            if position1.x>=x_goal and position1.y>=y_goal:
                velocity1.linear.x=0
                turtle1.publish(velocity1)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break

    elif x_goal<5.544445 and y_goal> 5.544445:
        while 1:
            velocity1.linear.x=1
            turtle1.publish(velocity1)
            if position1.x<=x_goal and position1.y>=y_goal:
                velocity1.linear.x=0
                turtle1.publish(velocity1)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break

    elif x_goal<5.544445 and y_goal<5.544445:
        while 1:
            velocity1.linear.x=1
            turtle1.publish(velocity1)
            if position1.x<=x_goal and position1.y<=y_goal:
                velocity1.linear.x=0
                turtle1.publish(velocity1)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break

    elif x_goal>5.544445 and y_goal<5.544445:
        while 1:
            velocity1.linear.x=1
            turtle1.publish(velocity1)
            if position1.x>=x_goal and position1.y<=y_goal:
                velocity1.linear.x=0
                turtle1.publish(velocity1)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break


    add_turtle(position1.x, position1.y, position1.theta-pi/2, 'turtle2')

    add_turtle(position1.x, position1.y, position1.theta+pi/2, 'turtle5')
    turtle2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)

    turtle5=rospy.Publisher('turtle5/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle2/pose',Pose, callback2)

    rospy.Subscriber('/turtle5/pose',Pose, callback5)
    velocity2=Twist()

    velocity5=Twist()
    rospy.sleep(1)
    print "Grabbing Object..."
    arm_move()


def arm_move():

    velocity2.linear.x=2
    velocity2.angular.z=2
    velocity5.linear.x=2
    velocity5.angular.z=-2
    turtle2.publish(velocity2)
    turtle5.publish(velocity5)
    rospy.sleep(1)

    while 1:
        velocity2.linear.x=2
        velocity2.angular.z=2
        velocity5.linear.x=2
        velocity5.angular.z=-2



        turtle2.publish(velocity2)
        turtle5.publish(velocity5)

        if is_close_to(position2.x,position5.x) and is_close_to(position2.y,position5.y):
            velocity2.linear.x=0
            velocity2.angular.z=0
            velocity5.linear.x=0
            velocity5.angular.z=0
            turtle2.publish(velocity2)
            turtle5.publish(velocity5)

            rospy.sleep(1)
            break



    x_goal=position1.x
    y_goal=position1.y




    quadrant=1
    x=abs(x_goal-position2.x)
    y=abs(y_goal-position2.y)

    if x_goal>position2.x and y_goal>position2.y:
        quadrant=1
        angle_goal=math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity2.angular.z=1
            velocity5.angular.z=-1
            turtle2.publish(velocity2)
            turtle5.publish(velocity5)
            if position2.theta>=angle_goal and position2.theta>0:
                velocity2.angular.z=0
                velocity5.angular.z=0
                turtle2.publish(velocity2)
                turtle5.publish(velocity5)
                rospy.sleep(1)

                break

    elif x_goal<position2.x and y_goal>position2.y:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity2.angular.z=1
            velocity5.angular.z=-1
            turtle2.publish(velocity2)
            turtle5.publish(velocity5)
            if position2.theta>=angle_goal and position2.theta>0:
                velocity2.angular.z=0
                velocity5.angular.z=0
                turtle2.publish(velocity2)
                turtle5.publish(velocity5)
                rospy.sleep(1)
                break

    elif x_goal<position2.x and y_goal<position2.y:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity2.angular.z=1
            velocity5.angular.z=-1
            turtle2.publish(velocity2)
            turtle5.publish(velocity5)

            if position2.theta>=angle_goal and position2.theta<0:
                velocity2.angular.z=0
                velocity5.angular.z=0
                turtle2.publish(velocity2)
                turtle5.publish(velocity5)
                rospy.sleep(1)
                print "position2.theta= ", position2.theta
                print "angle_goala= ", angle_goal

                break

    elif x_goal>position2.x and y_goal<position2.y:
        quadrant=4
        angle_goal=-math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity2.angular.z=1
            velocity5.angular.z=-1
            turtle2.publish(velocity2)
            turtle5.publish(velocity5)
            if position2.theta>=angle_goal and position2.theta<0:
                velocity2.angular.z=0
                velocity5.angular.z=0
                turtle2.publish(velocity2)
                turtle5.publish(velocity5)
                rospy.sleep(1)
                break


    while 1:
        velocity2.linear.x=2
        velocity5.linear.x=2



        turtle2.publish(velocity2)
        turtle5.publish(velocity5)

        if is_close_to(position2.x,position1.x) and is_close_to(position2.y,position1.y):
            velocity2.linear.x=0

            velocity5.linear.x=0

            turtle2.publish(velocity2)
            turtle5.publish(velocity5)

            rospy.sleep(1)
            print "Object Returned Successfully!"
            break


def turn_to_point_grabber():
    quadrant=1
    x=abs(x_goal-5.544445)
    y=abs(y_goal-5.544445)

    if x_goal>5.544445and y_goal>5.544445:
        quadrant=1
        angle_goal=math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            turtle1.publish(velocity1)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                turtle1.publish(velocity1)
                rospy.sleep(1)

                break

    elif x_goal<5.544445and y_goal>5.544445:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            turtle1.publish(velocity1)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                turtle1.publish(velocity1)
                rospy.sleep(1)

                break

    elif x_goal<5.544445and y_goal<5.544445:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            turtle1.publish(velocity1)

            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                turtle1.publish(velocity1)
                rospy.sleep(1)

                break

    elif x_goal>5.544445and y_goal<5.544445:
        quadrant=4
        angle_goal=-math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            turtle1.publish(velocity1)

            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                turtle1.publish(velocity1)
                rospy.sleep(1)

                break
    walk_grabber()


def square_formation():

    quadrant=1
    x=abs(x_goal_top-5.544445)
    y=abs(y_goal_top-5.544445)

    if x_goal_top>5.544445and y_goal_top>5.544445:
        quadrant=1
        angle_goal=math.atan(y/x)
    #        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            velocity2.angular.z=1
            velocity3.angular.z=1
            velocity4.angular.z=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                velocity4.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Angle: ", angle
                break

    elif x_goal_top<5.544445and y_goal_top>5.544445:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            velocity2.angular.z=1
            velocity3.angular.z=1
            velocity4.angular.z=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                velocity4.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Angle: ", angle
                break

    elif x_goal_top<5.544445and y_goal_top<5.544445:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            velocity2.angular.z=-1
            velocity3.angular.z=-1
            velocity4.angular.z=-1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                velocity4.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print  "Current Angle: ", angle
                break

    elif x_goal_top>5.544445and y_goal_top<5.544445:
        quadrant=4
        angle_goal=-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            velocity2.angular.z=-1
            velocity3.angular.z=-1
            velocity4.angular.z=-1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                velocity4.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Angle: ", angle
                break
    rospy.sleep(1)
    #Now we walk

    if x_goal_top > 5.544445 and y_goal_top > 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            velocity4.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.x>=x_goal_top and position1.y>=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                velocity4.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break




    elif x_goal_top < 5.544445 and y_goal_top > 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            velocity4.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.x<=x_goal_top and position1.y>=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                velocity4.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break

    elif x_goal_top < 5.544445 and y_goal_top < 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            velocity4.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.x<=x_goal_top and position1.y<=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                velocity4.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break



    elif x_goal_top > 5.544445 and y_goal_top < 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            velocity4.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            turtle4.publish(velocity4)
            if position1.x>=x_goal_top and position1.y<=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                velocity4.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                turtle4.publish(velocity4)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break




def triangle_formation():
    quadrant=1
    x=abs(x_goal_top-5.544445)
    y=abs(y_goal_top-5.544445)

    if x_goal_top>5.544445and y_goal_top>5.544445:
        quadrant=1
        angle_goal=math.atan(y/x)
#        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            velocity2.angular.z=1
            velocity3.angular.z=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Angle: ", angle
                break

    elif x_goal_top<5.544445and y_goal_top>5.544445:
        quadrant=2
        angle_goal=numpy.pi-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=1
            velocity2.angular.z=1
            velocity3.angular.z=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            if position1.theta>=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                print "Current Angle: ", angle
                break

    elif x_goal_top<5.544445and y_goal_top<5.544445:
        quadrant=3
        angle_goal=-numpy.pi+math.atan(y/x)
        print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            velocity2.angular.z=-1
            velocity3.angular.z=-1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)

            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print  "Current Angle: ", angle
                break

    elif x_goal_top>5.544445and y_goal_top<5.544445:
        quadrant=4
        angle_goal=-math.atan(y/x)
    #    print angle_goal, "in quadrant: ",quadrant
        while 1:
            velocity1.angular.z=-1
            velocity2.angular.z=-1
            velocity3.angular.z=-1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)

            if position1.theta<=angle_goal:
                velocity1.angular.z=0
                velocity2.angular.z=0
                velocity3.angular.z=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Angle: ", angle
                break
    rospy.sleep(1)
    #Now we walk

    if x_goal_top > 5.544445 and y_goal_top > 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            if position1.x>=x_goal_top and position1.y>=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break




    elif x_goal_top < 5.544445 and y_goal_top > 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)

            if position1.x<=x_goal_top and position1.y>=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break

    elif x_goal_top < 5.544445 and y_goal_top < 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            if position1.x<=x_goal_top and position1.y<=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break



    elif x_goal_top > 5.544445 and y_goal_top < 5.544445:
        while 1:
            velocity1.linear.x=1
            velocity2.linear.x=1
            velocity3.linear.x=1
            turtle1.publish(velocity1)
            turtle2.publish(velocity2)
            turtle3.publish(velocity3)
            if position1.x>=x_goal_top and position1.y<=y_goal_top:
                velocity1.linear.x=0
                velocity2.linear.x=0
                velocity3.linear.x=0
                turtle1.publish(velocity1)
                turtle2.publish(velocity2)
                turtle3.publish(velocity3)
                rospy.sleep(1)
                print "Current Coordinates: (", position1.x,",",position1.y,")"
                break





def grabber_formation():
    global x_goal, y_goal, x_arm_goal, y_arm_goal

    x_dist=abs(x_goal-5.544445)
    y_dist=abs(y_goal-5.544445)

    d_fixed=math.sqrt(x_dist*x_dist+y_dist*y_dist)-2

    t=math.atan(y_goal/x_goal)

    x_arm_goal=abs(math.cos(t)*d_fixed)
    y_arm_goal=(math.sin(t)*d_fixed)

    if x_goal>5.544445 and y_goal>5.544445:
        x_goal=5.544445+x_arm_goal
        y_goal=5.544445+y_arm_goal
    elif x_goal<5.544445 and y_goal>5.544445:
        x_goal=5.544445-x_arm_goal
        y_goal=5.544445+y_arm_goal
    elif x_goal<5.544445 and y_goal<5.544445:
        x_goal=5.544445-x_arm_goal
        y_goal=5.544445-y_arm_goal
    elif x_goal>5.544445 and y_goal<5.544445:
        x_goal=5.544445+x_arm_goal
        y_goal=5.544445-y_arm_goal


    turn_to_point_grabber()

def formation_test():
    global turtle1,turtle2,turtle3,turtle4,turtle5, pi
    global velocity1,velocity2, velocity3, velocity4, velocity5
    global x_goal, y_goal
    global add_turtle
    pi=math.pi
    rospy.init_node('formation_control',anonymous=True)
    turtle1=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, callback1)
    sub_cam = rospy.Subscriber('/camera_feed/image_raw', Image, camera_callback)
    rate = rospy.Rate(10)
    velocity1=Twist()
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)

    rospy.sleep(1)

    print "What shape do you want? \n"

    shape_choice=input("1. Triangle \n2. Diamond  \n3. Grabber \n")

    if shape_choice==1:
        print "TRIANGLE SELECTED"
        while 1:
            analyze_image_triangle()
            key=raw_input("Is this picture good enough? (y/n)")
            while key=='n':
                analyze_image_triangle()
                key=raw_input("Is this picture good enough? (y/n)")
            add_turtle(4.544445, 6.544445, 0, 'turtle2')
            add_turtle(6.544445, 6.544445, 0, 'turtle3')
            turtle2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
            turtle3=rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
            rospy.Subscriber('/turtle2/pose',Pose, callback2)
            rospy.Subscriber('/turtle3/pose',Pose, callback3)
            velocity2=Twist()
            velocity3=Twist()
            rospy.sleep(2)
            triangle_formation()
            key=raw_input("Press q to quit")
            if key=='q':
                break

    elif shape_choice==2:
        print "DIAMOND SELECTED"
        while 1:
            analyze_image_square()
            key=raw_input("Is this picture good enough? (y/n)")
            while key=='n':
                analyze_image_square()
                key=raw_input("Is this picture good enough? (y/n)")
            add_turtle(5.544445, 6.544445, 0, 'turtle2')
            add_turtle(6.544445, 6.544445, 0, 'turtle3')
            add_turtle(6.544445, 5.544445, 0, 'turtle4')
            turtle2=rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
            turtle3=rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
            turtle4=rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=10)
            rospy.Subscriber('/turtle2/pose',Pose, callback2)
            rospy.Subscriber('/turtle3/pose',Pose, callback3)
            rospy.Subscriber('/turtle4/pose',Pose, callback3)
            velocity2=Twist()
            velocity3=Twist()
            velocity4=Twist()

            rospy.sleep(2)
            square_formation()
            key=raw_input("Press q to quit")
            if key=='q':
                break



    else:

        print "GRABBER SELECTED"
        while 1:
            analyze_image()
            key=raw_input("Is this picture good enough? (y/n)")
            while key=='n':
                analyze_image()
                key=raw_input("Is this picture good enough? (y/n)")
            grabber_formation()
            key=raw_input("Press q to quit")
            if key=='q':
                break





















if __name__ == '__main__':
    try:
        formation_test()
    except rospy.ROSInterruptException:
        pass
