# Install script for directory: /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann

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
  FOREACH(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so.2.2.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so.2.2"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so"
      )
    IF(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      FILE(RPATH_CHECK
           FILE "${file}"
           RPATH "/usr/local/lib")
    ENDIF()
  ENDFOREACH()
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/lib/libopencv_flann.so.2.2.0"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/lib/libopencv_flann.so.2.2"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/lib/libopencv_flann.so"
    )
  FOREACH(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so.2.2.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so.2.2"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_flann.so"
      )
    IF(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      FILE(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/lib:"
           NEW_RPATH "/usr/local/lib")
      IF(CMAKE_INSTALL_DO_STRIP)
        EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "${file}")
      ENDIF(CMAKE_INSTALL_DO_STRIP)
    ENDIF()
  ENDFOREACH()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/flann" TYPE FILE FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/random.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/hdf5.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/ground_truth.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/linear_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/logger.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/composite_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/dist.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/kmeans_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/sampling.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/timer.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/heap.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/general.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/object_factory.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/allocator.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/saving.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/all_indices.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/nn_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/kdtree_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/matrix.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/flann_base.hpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/result_set.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/index_testing.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/autotuned_index.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/simplex_downhill.h"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/flann/include/opencv2/flann/flann.hpp"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "main")

