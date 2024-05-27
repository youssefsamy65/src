#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>

// Publisher for distance flag
ros::Publisher pub_flag;
// Publisher for velocity command
ros::Publisher pub_vel;
std_msgs::Float64 distance_flag;

// Function to stop the robot
void stopRobot() {
    geometry_msgs::Twist stop_msg;
    stop_msg.linear.x = 0.0;
    stop_msg.linear.y = 0.0;
    stop_msg.linear.z = 0.0;
    stop_msg.angular.x = 0.0;
    stop_msg.angular.y = 0.0;
    stop_msg.angular.z = 0.0;
    pub_vel.publish(stop_msg);
}

void callback(const sensor_msgs::LaserScan::ConstPtr& msg) {
    distance_flag.data = 0;

    for (int i = 0; i < 720; i++) {
        if (msg->ranges[i] < 0.2) {
            distance_flag.data = 0;
            // Stop the robot if an obstacle is detected
            stopRobot();
            ros::Duration(0.3).sleep();
            break;
        }
    }

    pub_flag.publish(distance_flag);
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "check_obstacle");
    ros::NodeHandle nh;

    pub_flag = nh.advertise<std_msgs::Float64>("/distance_flag", 1);
    pub_vel = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);  // Topic for robot velocity command
    ros::Subscriber sub = nh.subscribe("/myrobot1/laser_scan", 1, callback);

    ros::spin();

    return 0;
}

