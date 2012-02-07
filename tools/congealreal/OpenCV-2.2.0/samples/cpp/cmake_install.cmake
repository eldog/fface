# Install script for directory: /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp

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

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opencv/samples/cpp" TYPE FILE PERMISSIONS OWNER_READ GROUP_READ WORLD_READ FILES
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/fback.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/stereo_match.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/watershed.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/3calibration.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/meanshift_segmentation.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/calibration.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/filestorage.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/segment_objects.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/matching_to_many_images.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/starter_video.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/demhist.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/video_homography.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/peopledetect.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/brief_match_test.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/kalman.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/inpaint.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/starter_imagelist.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/houghlines.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/connected_components.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/dft.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/distrans.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/build3dmodel.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/matcher_simple.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/calibration_artificial.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/generic_descriptor_match.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/ffilldemo.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/kmeans.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/image.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/contours2.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/grabcut.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/camshiftdemo.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/edge.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/letter_recog.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/convexhull.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/minarea.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/imagelist_creator.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/chamfer.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/lkdemo.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/bagofwords_classification.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/bgfg_segm.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/descriptor_extractor_matcher.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/morphology2.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/cout_mat.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/select3dobj.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/squares.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/fitellipse.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/stereo_calib.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/laplace.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/drawing.cpp"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right07.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/lena.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right13.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left02.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left08.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left12.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/baboon.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left13.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right11.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right04.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left11.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left09.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left01.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right12.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left14.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right01.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/fruits.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right08.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left07.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right09.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left05.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left03.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right03.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right14.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right05.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right02.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left06.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/left04.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/right06.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/stuff.jpg"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic5.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic1.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic2.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic3.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic4.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/logo.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/logo_in_clutter.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/pic6.png"
    "/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/letter-recognition.data"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

