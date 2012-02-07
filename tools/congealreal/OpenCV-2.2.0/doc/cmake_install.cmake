# Install script for directory: /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opencv/doc" TYPE FILE FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/haartraining.htm"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/packaging.txt"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/CMakeLists.txt"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/README.txt"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/license.txt"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/opencv.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/opencv-logo.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/opencv-logo2.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/pattern.pdf"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/opencv_cheatsheet.pdf"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/opencv.pdf"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opencv/doc/papers" TYPE FILE FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/papers/algo_tracking.pdf"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/papers/camshift.pdf"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/papers/avbpa99.ps"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opencv/doc/vidsurv" TYPE FILE FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/vidsurv/Blob_Tracking_Tests.doc"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/vidsurv/TestSeq.doc"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/doc/vidsurv/Blob_Tracking_Modules.doc"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")

