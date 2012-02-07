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

# Include any dependencies generated for this target.
include samples/cpp/CMakeFiles/example_kalman.dir/depend.make

# Include the progress variables for this target.
include samples/cpp/CMakeFiles/example_kalman.dir/progress.make

# Include the compile flags for this target's objects.
include samples/cpp/CMakeFiles/example_kalman.dir/flags.make

samples/cpp/CMakeFiles/example_kalman.dir/kalman.o: samples/cpp/CMakeFiles/example_kalman.dir/flags.make
samples/cpp/CMakeFiles/example_kalman.dir/kalman.o: samples/cpp/kalman.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object samples/cpp/CMakeFiles/example_kalman.dir/kalman.o"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example_kalman.dir/kalman.o -c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/kalman.cpp

samples/cpp/CMakeFiles/example_kalman.dir/kalman.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_kalman.dir/kalman.i"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/kalman.cpp > CMakeFiles/example_kalman.dir/kalman.i

samples/cpp/CMakeFiles/example_kalman.dir/kalman.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_kalman.dir/kalman.s"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/kalman.cpp -o CMakeFiles/example_kalman.dir/kalman.s

samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.requires:
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.requires

samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.provides: samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.requires
	$(MAKE) -f samples/cpp/CMakeFiles/example_kalman.dir/build.make samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.provides.build
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.provides

samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.provides.build: samples/cpp/CMakeFiles/example_kalman.dir/kalman.o

# Object files for target example_kalman
example_kalman_OBJECTS = \
"CMakeFiles/example_kalman.dir/kalman.o"

# External object files for target example_kalman
example_kalman_EXTERNAL_OBJECTS =

bin/kalman: samples/cpp/CMakeFiles/example_kalman.dir/kalman.o
bin/kalman: lib/libopencv_core.so.2.2.0
bin/kalman: lib/libopencv_flann.so.2.2.0
bin/kalman: lib/libopencv_imgproc.so.2.2.0
bin/kalman: lib/libopencv_highgui.so.2.2.0
bin/kalman: lib/libopencv_ml.so.2.2.0
bin/kalman: lib/libopencv_video.so.2.2.0
bin/kalman: lib/libopencv_objdetect.so.2.2.0
bin/kalman: lib/libopencv_features2d.so.2.2.0
bin/kalman: lib/libopencv_calib3d.so.2.2.0
bin/kalman: lib/libopencv_legacy.so.2.2.0
bin/kalman: lib/libopencv_contrib.so.2.2.0
bin/kalman: lib/libopencv_ml.so.2.2.0
bin/kalman: lib/libopencv_video.so.2.2.0
bin/kalman: lib/libopencv_objdetect.so.2.2.0
bin/kalman: lib/libopencv_features2d.so.2.2.0
bin/kalman: lib/libopencv_flann.so.2.2.0
bin/kalman: lib/libopencv_calib3d.so.2.2.0
bin/kalman: lib/libopencv_highgui.so.2.2.0
bin/kalman: lib/libopencv_imgproc.so.2.2.0
bin/kalman: lib/libopencv_core.so.2.2.0
bin/kalman: 3rdparty/lib/libopencv_lapack.a
bin/kalman: 3rdparty/lib/libzlib.a
bin/kalman: samples/cpp/CMakeFiles/example_kalman.dir/build.make
bin/kalman: samples/cpp/CMakeFiles/example_kalman.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../../bin/kalman"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_kalman.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/cpp/CMakeFiles/example_kalman.dir/build: bin/kalman
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/build

samples/cpp/CMakeFiles/example_kalman.dir/requires: samples/cpp/CMakeFiles/example_kalman.dir/kalman.o.requires
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/requires

samples/cpp/CMakeFiles/example_kalman.dir/clean:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -P CMakeFiles/example_kalman.dir/cmake_clean.cmake
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/clean

samples/cpp/CMakeFiles/example_kalman.dir/depend:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/CMakeFiles/example_kalman.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/cpp/CMakeFiles/example_kalman.dir/depend

