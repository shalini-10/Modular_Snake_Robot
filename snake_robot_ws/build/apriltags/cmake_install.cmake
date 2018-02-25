# Install script for directory: /home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pi/Modular_Snake_Robot/snake_robot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/apriltags/cmake" TYPE FILE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/apriltags/catkin_generated/installspace/apriltags-msg-paths.cmake")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/pi/Modular_Snake_Robot/snake_robot_ws/devel/lib/python2.7/dist-packages/apriltags")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/devel/lib/python2.7/dist-packages/apriltags")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/apriltags/catkin_generated/installspace/apriltags.pc")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/apriltags/cmake" TYPE FILE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/apriltags/catkin_generated/installspace/apriltags-msg-extras.cmake")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/apriltags/cmake" TYPE FILE FILES
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/apriltags/catkin_generated/installspace/apriltagsConfig.cmake"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/apriltags/catkin_generated/installspace/apriltagsConfig-version.cmake"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/apriltags" TYPE FILE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/package.xml")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags"
         RPATH "/home/pi/Modular_Snake_Robot/snake_robot_ws/install/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/src" TYPE EXECUTABLE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/devel/lib/apriltags/apriltags")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags"
         OLD_RPATH "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/lib:/home/pi/Modular_Snake_Robot/snake_robot_ws/install/lib:/home/pi/ros_ws/devel/lib:/usr/local/lib:"
         NEW_RPATH "/home/pi/Modular_Snake_Robot/snake_robot_ws/install/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/src/apriltags")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/src" TYPE FILE FILES
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Edge.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/FloatImage.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/GLine2D.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/GLineSegment2D.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Gaussian.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/GrayModel.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Gridder.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Homography33.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/MathUtil.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Quad.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Segment.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Serial.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag16h5.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag16h5_other.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag25h7.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag25h9.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag36h11.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag36h11_other.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/Tag36h9.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/TagDetection.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/TagDetector.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/TagFamily.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/UnionFindSimple.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/XYWeight.h"
    "/home/pi/Modular_Snake_Robot/snake_robot_ws/src/apriltags/src/pch.h"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pi/Modular_Snake_Robot/snake_robot_ws/build/lib/pkgconfig/apriltags.pc")
endif()

