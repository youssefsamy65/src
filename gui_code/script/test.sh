#!/bin/bash

cd /home/oem/catkin_ws
source devel/setup.bash
roslaunch robot_control control.launch
