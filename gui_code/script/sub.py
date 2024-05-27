#!/usr/bin/env python3
import subprocess
import rospy
from std_msgs.msg import Int32

# Callback function to handle incoming integer messages
def integer_callback(msg):
    rospy.loginfo("Received integer: %d", msg.data)
    if msg.data == 1:
        subprocess.run(["/home/oem/catkin_ws/src/gui_code/script/test.sh"])
    if msg.data == 1:
        subprocess.run(["/home/oem/catkin_ws/src/gui_code/script/testt.sh"])
def subscribe_integer():
    # Initialize the ROS node
    rospy.init_node('integer_subscriber', anonymous=True)

    # Create a subscriber for the 'integer_topic' topic
    rospy.Subscriber('button_topic', Int32, integer_callback)

    # Spin to keep the node alive and receive messages
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_integer()
    except rospy.ROSInterruptException:
        pass

