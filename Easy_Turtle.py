#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv
import math
import threading
pi=math.pi

class Easy_Turtle:
    count=0
    current_positions=[]
    rospy.wait_for_service('spawn')
    add_turtle=rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    rospy.wait_for_service('kill')
    remove_turtle=rospy.ServiceProxy('kill', turtlesim.srv.Kill)

    def __init__(self,x_spawn,y_spawn,theta_spawn):
        self.number=Easy_Turtle.count
        self.current_position=Pose()
        self.current_position.x=x_spawn
        self.current_position.y=y_spawn
        self.current_position.theta=theta_spawn
        Easy_Turtle.current_positions.append(self.current_position)
        self.name="turtle"+str(Easy_Turtle.count)
        self.pub_name=self.name+"/cmd_vel"
        self.sub_name="/"+self.name+"/pose"
        self.velocity=Twist()
        self.pub=rospy.Publisher(self.pub_name, Twist, queue_size=10)
     
        rospy.Subscriber(self.sub_name,Pose, self.callback, callback_args=self)
        Easy_Turtle.add_turtle(x_spawn, y_spawn, theta_spawn, self.name)
        current_thread=threading.Thread(target=self.publish_velocity,args=())
        current_thread.start()
        Easy_Turtle.count+=1

    #Begins real-time control loop based on user-input
    def control(self):
        control_thread=threading.Thread(target=self.runtime,args=())
        control_thread.start()

    def runtime(self):
        print "Menu:\n1.Forward \n2. Backward \n3. Circle \n4.Spin \n5.Stop"
        while not rospy.is_shutdown():
            key=raw_input()
            if key=='1':
                self.velocity.linear.x+=.2
            elif key=='2':
                 self.velocity.linear.x-=.2        
            elif key=='3':
                self.circle(4)
            elif key=='4':
                self.velocity.linear.x=0
                self.velocity.angular.z+=.2
            elif key=='5':
                self.velocity.linear.x=0
                self.velocity.angular.z=0
            else:
                pass
        
    def publish_velocity(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.velocity)
           
    def circle(self,r):
        if self.velocity.angular.z==0:
            self.velocity.angular.z=2
        self.velocity.linear.x=self.velocity.angular.z*r

    def delete(self):
        Easy_Turtle.remove_turtle(self.name)
        self.current_position.x=None
        self.current_position.y=None

    @staticmethod
    def is_close_to(a,b):
        if a<b and a+.8>=b: #Change constant for collision range, evasion distance should be around 2-2.3
            return True
        if a>b and a-.8<b:
            return True
        else:
            return False


    @staticmethod
    def is_colliding(p1,p2):
        if Easy_Turtle.is_close_to(p1.x,p2.x) and Easy_Turtle.is_close_to(p1.y,p2.y):
            return True
        else:
            return False

    @staticmethod
    def callback(pos,self):

       self.current_position=pos
       Easy_Turtle.current_positions[self.number]=pos
       s=Easy_Turtle.current_positions[0:self.number]
       for priority in reversed(s):       
           if Easy_Turtle.is_colliding(pos,priority):               #is_colliding is continously called, and if the turtles are too close, their velocity is updated
               self.velocity.linear.x=-.5
               self.velocity.angular.z=0
             
      


def turtle_member():
    rospy.init_node('EZ_Turtle_control',anonymous=True)
    Easy_Turtle.remove_turtle("turtle1")
    rospy.sleep(2)

    t1=Easy_Turtle(1,5,0)
    t2=Easy_Turtle(10,5,pi)






    print "This turtle is named: ",t1.name
    print "This turtle is named: ",t2.name
    t2.velocity.linear.x=1
    rospy.sleep(1)
    print "3"
    rospy.sleep(1)
    print "2"
    rospy.sleep(1)
    print "1"
    rospy.sleep(1)
   
    print "CURRENT POS: ",t1.current_position.x
    rospy.sleep(1)
    print "CURRENT POS: ", Easy_Turtle.current_positions[0].x
    t1.delete()
    rospy.spin()





if __name__ == '__main__':
    try:
        turtle_member()
    except rospy.ROSInterruptException:
        pass
