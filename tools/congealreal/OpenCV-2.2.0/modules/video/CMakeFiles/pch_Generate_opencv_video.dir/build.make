# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/cmake-gui

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0

# Utility rule file for pch_Generate_opencv_video.

modules/video/CMakeFiles/pch_Generate_opencv_video: modules/video/precomp.hpp.gch/opencv_video_Release.gch

modules/video/precomp.hpp.gch/opencv_video_Release.gch: modules/video/src/precomp.hpp
modules/video/precomp.hpp.gch/opencv_video_Release.gch: modules/video/precomp.hpp
modules/video/precomp.hpp.gch/opencv_video_Release.gch: lib/libopencv_video_pch_dephelp.a
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating precomp.hpp.gch/opencv_video_Release.gch"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video && /usr/bin/c++ -O3 -DNDEBUG -fomit-frame-pointer -O3 -ffast-math -msse -msse2 -DNDEBUG -O3 -DNDEBUG -fomit-frame-pointer -O3 -ffast-math -msse -msse2 -DNDEBUG -fPIC -I/usr/lib/pymodules/python2.7/numpy/core/include -I/usr/include/eigen2 -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/. -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/include -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/include/opencv -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/include -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/src -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/../core/include -I/home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/../imgproc/include -D PYTHON_USE_NUMPY=1 -DHAVE_CONFIG_H -DCVAPI_EXPORTS -D PYTHON_USE_NUMPY=1 -DHAVE_CONFIG_H -Wall -Wno-long-long -pthread -ffunction-sections -x c++-header -o /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/precomp.hpp.gch/opencv_video_Release.gch /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/precomp.hpp

modules/video/precomp.hpp: modules/video/src/precomp.hpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating precomp.hpp"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video && /usr/bin/cmake -E copy /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/src/precomp.hpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/precomp.hpp

pch_Generate_opencv_video: modules/video/CMakeFiles/pch_Generate_opencv_video
pch_Generate_opencv_video: modules/video/precomp.hpp.gch/opencv_video_Release.gch
pch_Generate_opencv_video: modules/video/precomp.hpp
pch_Generate_opencv_video: modules/video/CMakeFiles/pch_Generate_opencv_video.dir/build.make
.PHONY : pch_Generate_opencv_video

# Rule to build all files generated by this target.
modules/video/CMakeFiles/pch_Generate_opencv_video.dir/build: pch_Generate_opencv_video
.PHONY : modules/video/CMakeFiles/pch_Generate_opencv_video.dir/build

modules/video/CMakeFiles/pch_Generate_opencv_video.dir/clean:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video && $(CMAKE_COMMAND) -P CMakeFiles/pch_Generate_opencv_video.dir/cmake_clean.cmake
.PHONY : modules/video/CMakeFiles/pch_Generate_opencv_video.dir/clean

modules/video/CMakeFiles/pch_Generate_opencv_video.dir/depend:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/modules/video/CMakeFiles/pch_Generate_opencv_video.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : modules/video/CMakeFiles/pch_Generate_opencv_video.dir/depend

