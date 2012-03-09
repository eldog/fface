#include <new>

#include "uk_me_eldog_fface_FaceCaptureView.h"
#include "cnn.h"

JNIEXPORT jlong JNICALL Java_uk_me_eldog_fface_FaceCaptureView_loadFaceDetector
(JNIEnv* env, jclass cls, jstring cascadeFileName, jstring cnnFileName)
{
    const char *cascadeFile;
    cascadeFile = env->GetStringUTFChars(cascadeFileName, 0);
    const char *cnnFile;
    cnnFile = env->GetStringUTFChars(cnnFileName, 0);
    
    Cnn* cnn = new (std::nothrow) Cnn();
    if (cnn != 0)
    {
        cnn->loadCascade(cascadeFile);
        cnn->loadConvNet(cnnFile);
    } // if
    return (jlong) cnn;
} // loadFaceDetector

JNIEXPORT jlong JNICALL Java_uk_me_eldog_fface_FaceCaptureView_findFaces
(JNIEnv* env, jclass cls, jlong cnnPointer, jint width, jint height, jbyteArray yuv, jintArray bgra)
{
    Cnn* cnn = (Cnn*) cnnPointer;

    jbyte* _yuv  = env->GetByteArrayElements(yuv, 0);
    jint*  _bgra = env->GetIntArrayElements(bgra, 0);

    cv::Mat myuv(height + height/2, width, CV_8UC1, (unsigned char *)_yuv);
    cv::Mat mbgra(height, width, CV_8UC4, (unsigned char *)_bgra);
    cv::Mat mgray(height, width, CV_8UC1, (unsigned char *)_yuv);
    cv::cvtColor(myuv, mbgra, CV_YUV420sp2BGR, 4);

    std::vector<cv::Rect> faces;
    faces = cnn->findFaces(mbgra);
    
    cnn->drawRectangles(faces, mbgra);
    env->ReleaseIntArrayElements(bgra, _bgra, 0);
    env->ReleaseByteArrayElements(yuv, _yuv, 0);

    return (jlong) cnn;
} // findFaces

JNIEXPORT void JNICALL Java_uk_me_eldog_fface_FaceCaptureView_releaseFaceDetector
  (JNIEnv* env, jclass cls, jlong cnnPointer)
{
    delete (Cnn*) cnnPointer;
} // releaseFaceDetector


