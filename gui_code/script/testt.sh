#!/bin/bash

pkill -f "controller_spawner"
pkill -f "joint_state_publisher"
pkill -f "robot_hardware_interface"
pkill -f "robot_state_publisher"
pkill -f "rviz"
pkill -f "serial_node.py"



