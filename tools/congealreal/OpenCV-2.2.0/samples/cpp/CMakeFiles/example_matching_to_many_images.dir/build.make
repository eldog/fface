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
include samples/cpp/CMakeFiles/example_matching_to_many_images.dir/depend.make

# Include the progress variables for this target.
include samples/cpp/CMakeFiles/example_matching_to_many_images.dir/progress.make

# Include the compile flags for this target's objects.
include samples/cpp/CMakeFiles/example_matching_to_many_images.dir/flags.make

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/flags.make
samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o: samples/cpp/matching_to_many_images.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o -c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/matching_to_many_images.cpp

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.i"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/matching_to_many_images.cpp > CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.i

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.s"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/matching_to_many_images.cpp -o CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.s

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.requires:
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.requires

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.provides: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.requires
	$(MAKE) -f samples/cpp/CMakeFiles/example_matching_to_many_images.dir/build.make samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.provides.build
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.provides

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.provides.build: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o

# Object files for target example_matching_to_many_images
example_matching_to_many_images_OBJECTS = \
"CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o"

# External object files for target example_matching_to_many_images
example_matching_to_many_images_EXTERNAL_OBJECTS =

bin/matching_to_many_images: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o
bin/matching_to_many_images: lib/libopencv_core.so.2.2.0
bin/matching_to_many_images: lib/libopencv_flann.so.2.2.0
bin/matching_to_many_images: lib/libopencv_imgproc.so.2.2.0
bin/matching_to_many_images: lib/libopencv_highgui.so.2.2.0
bin/matching_to_many_images: lib/libopencv_ml.so.2.2.0
bin/matching_to_many_images: lib/libopencv_video.so.2.2.0
bin/matching_to_many_images: lib/libopencv_objdetect.so.2.2.0
bin/matching_to_many_images: lib/libopencv_features2d.so.2.2.0
bin/matching_to_many_images: lib/libopencv_calib3d.so.2.2.0
bin/matching_to_many_images: lib/libopencv_legacy.so.2.2.0
bin/matching_to_many_images: lib/libopencv_contrib.so.2.2.0
bin/matching_to_many_images: lib/libopencv_ml.so.2.2.0
bin/matching_to_many_images: lib/libopencv_video.so.2.2.0
bin/matching_to_many_images: lib/libopencv_objdetect.so.2.2.0
bin/matching_to_many_images: lib/libopencv_features2d.so.2.2.0
bin/matching_to_many_images: lib/libopencv_flann.so.2.2.0
bin/matching_to_many_images: lib/libopencv_calib3d.so.2.2.0
bin/matching_to_many_images: lib/libopencv_highgui.so.2.2.0
bin/matching_to_many_images: lib/libopencv_imgproc.so.2.2.0
bin/matching_to_many_images: lib/libopencv_core.so.2.2.0
bin/matching_to_many_images: 3rdparty/lib/libopencv_lapack.a
bin/matching_to_many_images: 3rdparty/lib/libzlib.a
bin/matching_to_many_images: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/build.make
bin/matching_to_many_images: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../../bin/matching_to_many_images"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_matching_to_many_images.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/cpp/CMakeFiles/example_matching_to_many_images.dir/build: bin/matching_to_many_images
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/build

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/requires: samples/cpp/CMakeFiles/example_matching_to_many_images.dir/matching_to_many_images.o.requires
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/requires

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/clean:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -P CMakeFiles/example_matching_to_many_images.dir/cmake_clean.cmake
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/clean

samples/cpp/CMakeFiles/example_matching_to_many_images.dir/depend:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/CMakeFiles/example_matching_to_many_images.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/cpp/CMakeFiles/example_matching_to_many_images.dir/depend

