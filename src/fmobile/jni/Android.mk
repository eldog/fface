LOCAL_PATH := $(call my-dir)

common_CFLAGS := -Wall -fexceptions -DHAVE_EXPAT_CONFIG_H

common_C_INCLUDES += \
	$(LOCAL_PATH)/expat/lib \
	$(LOCAL_PATH)/expat

common_COPY_HEADERS_TO := libexpat
common_COPY_HEADERS := \
	expat/lib/expat.h \
	expat/lib/expat_external.h

# Device static library
include $(CLEAR_VARS)
OPENCV_MK_PATH:=$(HOME)/android-opencv-2.3.1/OpenCV-2.3.1/share/OpenCV/OpenCV.mk
ifeq ("$(wildcard $(OPENCV_MK_PATH))","")
	#try to load OpenCV.mk from default install location
	include $(TOOLCHAIN_PREBUILT_ROOT)/user/share/OpenCV/OpenCV.mk
else
	include $(OPENCV_MK_PATH)
endif
LOCAL_CFLAGS += $(common_CFLAGS)
LOCAL_C_INCLUDES += $(common_C_INCLUDES)

LOCAL_COPY_HEADERS_TO := $(common_COPY_HEADERS_TO)
LOCAL_COPY_HEADERS := $(common_COPY_HEADERS)

LOCAL_C_INCLUDES += $(LOCAL_PATH)/cvconvnet
LOCAL_MODULE := FaceCapture
LOCAL_SRC_FILES := \
    expat/lib/xmlparse.c \
    expat/lib/xmlrole.c \
    expat/lib/xmltok.c \
    cvconvnet/cvconvnet.cpp \
    cvconvnet/cvconvolutionplane.cpp \
    cvconvnet/cvgenericplane.cpp \
    cvconvnet/cvmaxplane.cpp \
    cvconvnet/cvregressionplane.cpp \
    cvconvnet/cvsubsamplingplane.cpp \
    cvconvnet/cvconvnetparser.cpp \
    cvconvnet/cvfastsigmoid.cpp \
    cvconvnet/cvmaxoperatorplane.cpp \
    cvconvnet/cvrbfplane.cpp \
    cvconvnet/cvsourceplane.cpp \
    FaceCapture.cpp \
    cnn.cpp
LOCAL_LDLIBS +=  -llog -ldl


include $(BUILD_SHARED_LIBRARY)

