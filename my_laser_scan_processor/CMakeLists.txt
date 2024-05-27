cmake_minimum_required(VERSION 3.0.2)
project(my_laser_scan_processor)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(laser_scan_processor src/laser_scan_processor.cpp)

target_link_libraries(laser_scan_processor
  ${catkin_LIBRARIES}
)

