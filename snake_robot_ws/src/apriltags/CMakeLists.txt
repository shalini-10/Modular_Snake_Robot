cmake_minimum_required(VERSION 2.8.3)
project(apriltags)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  message_generation
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend tag for "message_generation"
##   * add a build_depend and a run_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependency has been pulled in
##     but can be declared for certainty nonetheless:
##     * add a run_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder

#add_message_files(
#   FILES
#    )

# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
   geometry_msgs
 )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## To declare and build dynamic reconfigure parameters within this
## package, follow these steps:
## * In the file package.xml:
##   * add a build_depend and a run_depend tag for "dynamic_reconfigure"
## * In this file (CMakeLists.txt):
##   * add "dynamic_reconfigure" to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * uncomment the "generate_dynamic_reconfigure_options" section below
##     and list every .cfg file to be processed

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES apriltags
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(apriltags
#   src/${PROJECT_NAME}/apriltags.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(apriltags ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
# add_executable(apriltags_node src/apriltags_node.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(apriltags_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(apriltags_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS apriltags apriltags_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_apriltags.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
set(POD_NAME apriltags)
include(cmake/pods.cmake)

SET(SOURCES ${PROJECT_SOURCE_DIR}/src/main.cpp
            ${PROJECT_SOURCE_DIR}/src/Edge.cc
            ${PROJECT_SOURCE_DIR}/src/FloatImage.cc
            ${PROJECT_SOURCE_DIR}/src/Gaussian.cc
            ${PROJECT_SOURCE_DIR}/src/GLine2D.cc
            ${PROJECT_SOURCE_DIR}/src/GLineSegment2D.cc
            ${PROJECT_SOURCE_DIR}/src/GrayModel.cc
            ${PROJECT_SOURCE_DIR}/src/Homography33.cc
            ${PROJECT_SOURCE_DIR}/src/MathUtil.cc
            ${PROJECT_SOURCE_DIR}/src/Quad.cc
            ${PROJECT_SOURCE_DIR}/src/Segment.cc
            ${PROJECT_SOURCE_DIR}/src/TagDetection.cc
            ${PROJECT_SOURCE_DIR}/src/TagDetector.cc
            ${PROJECT_SOURCE_DIR}/src/TagFamily.cc
            ${PROJECT_SOURCE_DIR}/src/UnionFindSimple.cc
            ${PROJECT_SOURCE_DIR}/src/Serial.cpp
              
            )

SET(HEADERS ${PROJECT_SOURCE_DIR}/src/Edge.h
            ${PROJECT_SOURCE_DIR}/src/FloatImage.h
            ${PROJECT_SOURCE_DIR}/src/Gaussian.h
            ${PROJECT_SOURCE_DIR}/src/GLine2D.h
            ${PROJECT_SOURCE_DIR}/src/GLineSegment2D.h
            ${PROJECT_SOURCE_DIR}/src/GrayModel.h
            ${PROJECT_SOURCE_DIR}/src/Homography33.h
            ${PROJECT_SOURCE_DIR}/src/MathUtil.h
            ${PROJECT_SOURCE_DIR}/src/Quad.h
            ${PROJECT_SOURCE_DIR}/src/Segment.h
            ${PROJECT_SOURCE_DIR}/src/TagDetection.h
            ${PROJECT_SOURCE_DIR}/src/TagDetector.h
            ${PROJECT_SOURCE_DIR}/src/TagFamily.h
            ${PROJECT_SOURCE_DIR}/src/UnionFindSimple.h
            ${PROJECT_SOURCE_DIR}/src/Gridder.h
            ${PROJECT_SOURCE_DIR}/src/pch.h
            ${PROJECT_SOURCE_DIR}/src/Tag16h5.h
            ${PROJECT_SOURCE_DIR}/src/Tag16h5_other.h
            ${PROJECT_SOURCE_DIR}/src/Tag25h7.h
            ${PROJECT_SOURCE_DIR}/src/Tag25h9.h
            ${PROJECT_SOURCE_DIR}/src/Tag36h9.h
            ${PROJECT_SOURCE_DIR}/src/Tag36h11.h
            ${PROJECT_SOURCE_DIR}/src/Tag36h11_other.h
            ${PROJECT_SOURCE_DIR}/src/XYWeight.h
	    ${PROJECT_SOURCE_DIR}/src/Serial.h
            )


find_package(OpenCV REQUIRED)

add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})
add_dependencies(${PROJECT_NAME} ${catkin_EXPORTED_TARGETS} )
target_link_libraries(${PROJECT_NAME} ${ROS_LIBRARIES} ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
pods_use_pkg_config_packages(apriltags eigen3)

if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  target_link_libraries(apriltags -L/opt/local/lib/) # MacPorts special treatment...
else (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  pods_use_pkg_config_packages(apriltags libv4l2)
endif (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")

pods_install_libraries(apriltags DESTINATION src/)

file(GLOB header_files "src/*.h")
pods_install_headers(${header_files} DESTINATION src/)
pods_install_pkg_config_file(apriltags
    LIBS -lapriltags
    REQUIRES eigen3 opencv2
    VERSION 1.0.0)



