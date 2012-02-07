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
include samples/c/CMakeFiles/example_delaunay.dir/depend.make

# Include the progress variables for this target.
include samples/c/CMakeFiles/example_delaunay.dir/progress.make

# Include the compile flags for this target's objects.
include samples/c/CMakeFiles/example_delaunay.dir/flags.make

samples/c/CMakeFiles/example_delaunay.dir/delaunay.o: samples/c/CMakeFiles/example_delaunay.dir/flags.make
samples/c/CMakeFiles/example_delaunay.dir/delaunay.o: samples/c/delaunay.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object samples/c/CMakeFiles/example_delaunay.dir/delaunay.o"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/example_delaunay.dir/delaunay.o   -c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c/delaunay.c

samples/c/CMakeFiles/example_delaunay.dir/delaunay.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/example_delaunay.dir/delaunay.i"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c/delaunay.c > CMakeFiles/example_delaunay.dir/delaunay.i

samples/c/CMakeFiles/example_delaunay.dir/delaunay.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/example_delaunay.dir/delaunay.s"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c/delaunay.c -o CMakeFiles/example_delaunay.dir/delaunay.s

samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.requires:
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.requires

samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.provides: samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.requires
	$(MAKE) -f samples/c/CMakeFiles/example_delaunay.dir/build.make samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.provides.build
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.provides

samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.provides.build: samples/c/CMakeFiles/example_delaunay.dir/delaunay.o

# Object files for target example_delaunay
example_delaunay_OBJECTS = \
"CMakeFiles/example_delaunay.dir/delaunay.o"

# External object files for target example_delaunay
example_delaunay_EXTERNAL_OBJECTS =

bin/delaunay: samples/c/CMakeFiles/example_delaunay.dir/delaunay.o
bin/delaunay: lib/libopencv_core.so.2.2.0
bin/delaunay: lib/libopencv_flann.so.2.2.0
bin/delaunay: lib/libopencv_imgproc.so.2.2.0
bin/delaunay: lib/libopencv_highgui.so.2.2.0
bin/delaunay: lib/libopencv_ml.so.2.2.0
bin/delaunay: lib/libopencv_video.so.2.2.0
bin/delaunay: lib/libopencv_objdetect.so.2.2.0
bin/delaunay: lib/libopencv_features2d.so.2.2.0
bin/delaunay: lib/libopencv_calib3d.so.2.2.0
bin/delaunay: lib/libopencv_legacy.so.2.2.0
bin/delaunay: lib/libopencv_contrib.so.2.2.0
bin/delaunay: lib/libopencv_ml.so.2.2.0
bin/delaunay: lib/libopencv_video.so.2.2.0
bin/delaunay: lib/libopencv_objdetect.so.2.2.0
bin/delaunay: lib/libopencv_features2d.so.2.2.0
bin/delaunay: lib/libopencv_flann.so.2.2.0
bin/delaunay: lib/libopencv_calib3d.so.2.2.0
bin/delaunay: lib/libopencv_highgui.so.2.2.0
bin/delaunay: lib/libopencv_imgproc.so.2.2.0
bin/delaunay: lib/libopencv_core.so.2.2.0
bin/delaunay: 3rdparty/lib/libopencv_lapack.a
bin/delaunay: 3rdparty/lib/libzlib.a
bin/delaunay: samples/c/CMakeFiles/example_delaunay.dir/build.make
bin/delaunay: samples/c/CMakeFiles/example_delaunay.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable ../../bin/delaunay"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_delaunay.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/c/CMakeFiles/example_delaunay.dir/build: bin/delaunay
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/build

samples/c/CMakeFiles/example_delaunay.dir/requires: samples/c/CMakeFiles/example_delaunay.dir/delaunay.o.requires
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/requires

samples/c/CMakeFiles/example_delaunay.dir/clean:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c && $(CMAKE_COMMAND) -P CMakeFiles/example_delaunay.dir/cmake_clean.cmake
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/clean

samples/c/CMakeFiles/example_delaunay.dir/depend:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/c/CMakeFiles/example_delaunay.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/c/CMakeFiles/example_delaunay.dir/depend

