# ros_examples
Examples and testing of ROS features using Turtlesim and Gazebo. Each example is scripted with python and can be executed in one line with the roslaunch command. To run the examples, download the .py and corresponding .launch file to a desired package location within a catkin workspace and use:
```
roslaunch [PACKAGE] example.launch
```

Only dependencies required are ROS (Kinetic or later), OpenCV2, and Gazebo unless otherwise noted.

## Installation Tutorials
[ROS](http://wiki.ros.org/melodic/Installation/Ubuntu)

[OpenCV2](https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html)

[Gazebo](http://gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros#Introduction)

## Script Uses

#### collision_test
Implements basic collision detection based on pose callback. The collision radius can be modified to allow for evasion or other responses.

#### formation_test
An elaboration of vision_test that now spawns a multi-turtle formation based on user input that goes to a OpenCV2 determined point.

#### gazebo_test
[REQUIRES TURTLEBOT3 PACKAGE FOUND HERE](https://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/)

A wandering turtlebot3 in gazebo that detects and avoids obstacles using the /scan topic.

#### relative_arc
A demonstration of areas swept out by turtles (1 to 10) moving at some relative velocity to a leader turtle.

#### turtle_circle
Multi-turtle circular movement with user determined radius.

#### turtle_invaders
A space invaders clone in turtlesim that uses multithreading extensively.

#### turtle_join
An elaboration of turtle_circle that uses multithreading for dynamic turtle spawn and priority collision detection in the joining process.

#### vision_test
Goes to a OpenCV2 determined point using a static photo taken by webcam.

#### OARbot_nav
Basic go-to point test of the OARbot that demonstrates it's omnidirectional movement capabilities

#### face_control
By using Haar Cascades in OpenCV2, a webcam can detect a users face and smile to control the movement of the OARbot.

#### banjOAR_kazooie
The pygame library is used to control the OARbot with WASD movement and mouse-controlled look. The gazebo world is a *rough* recreation of the level "Spiral Mountain" from Banjo-Kazooie

