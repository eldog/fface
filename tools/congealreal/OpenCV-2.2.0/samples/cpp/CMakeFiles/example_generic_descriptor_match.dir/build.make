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
include samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/depend.make

# Include the progress variables for this target.
include samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/progress.make

# Include the compile flags for this target's objects.
include samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/flags.make

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/flags.make
samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o: samples/cpp/generic_descriptor_match.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o -c /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/generic_descriptor_match.cpp

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.i"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/generic_descriptor_match.cpp > CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.i

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.s"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/generic_descriptor_match.cpp -o CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.s

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.requires:
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.requires

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.provides: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.requires
	$(MAKE) -f samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/build.make samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.provides.build
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.provides

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.provides.build: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o

# Object files for target example_generic_descriptor_match
example_generic_descriptor_match_OBJECTS = \
"CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o"

# External object files for target example_generic_descriptor_match
example_generic_descriptor_match_EXTERNAL_OBJECTS =

bin/generic_descriptor_match: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o
bin/generic_descriptor_match: lib/libopencv_core.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_flann.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_imgproc.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_highgui.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_ml.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_video.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_objdetect.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_features2d.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_calib3d.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_legacy.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_contrib.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_ml.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_video.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_objdetect.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_features2d.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_flann.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_calib3d.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_highgui.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_imgproc.so.2.2.0
bin/generic_descriptor_match: lib/libopencv_core.so.2.2.0
bin/generic_descriptor_match: 3rdparty/lib/libopencv_lapack.a
bin/generic_descriptor_match: 3rdparty/lib/libzlib.a
bin/generic_descriptor_match: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/build.make
bin/generic_descriptor_match: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../../bin/generic_descriptor_match"
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_generic_descriptor_match.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/build: bin/generic_descriptor_match
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/build

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/requires: samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/generic_descriptor_match.o.requires
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/requires

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/clean:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp && $(CMAKE_COMMAND) -P CMakeFiles/example_generic_descriptor_match.dir/cmake_clean.cmake
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/clean

samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/depend:
	cd /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0 /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp /home/eldog/Dropbox/University/COMP30040/fface/tools/congealreal/OpenCV-2.2.0/samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/cpp/CMakeFiles/example_generic_descriptor_match.dir/depend

