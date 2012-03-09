#include <iostream>
#include <fstream>
#include <sstream>

#include <opencv/highgui.h> 

#include "cvconvnet.h"
#include "ConvNet.h"

using namespace std;

JNIEXPORT jdouble JNICALL
Java_ConvNet_runConv(JNIEnv *env, 
                     jobject obj, 
                     jstring xmlFilePath, 
                     jstring imageFilePath)
{
    // Parse the file path strings
    const char *xmlFile;
    xmlFile = env->GetStringUTFChars(xmlFilePath, 0);
    const char *imageFile;
    imageFile = env->GetStringUTFChars(imageFilePath, 0);
    
    CvConvNet net;
    CvSize input_size = cvSize(128, 128);
    
    // Load the xml file
    ifstream ifs(xmlFile);
    string xml((istreambuf_iterator<char>(ifs)), istreambuf_iterator<char>());
    
    if (!net.fromString(xml))
    {
        return -1000.0;
    } // if
    
    cvNamedWindow("Image", CV_WINDOW_AUTOSIZE);
    cvMoveWindow("Image", input_size.height, input_size.width);
    CvFont font;
    cvInitFont(&font, CV_FONT_HERSHEY_PLAIN, 1.0, 1.0);
    
    IplImage *img;

    if ((img = cvLoadImage(imageFile, CV_LOAD_IMAGE_GRAYSCALE)) == 0)
    {
        return -1000.0;
    } // if

    jdouble value;
    value = (jdouble) net.fprop(img);
    ostringstream displayValue;
    displayValue << (double) value;

    cvPutText(img, 
              displayValue.str().c_str(),
              cvPoint(0, input_size.height / 2),
              &font,
              CV_RGB(0, 255, 0));
    cvShowImage("Image", img);
    cvWaitKey(1000);
    cvReleaseImage(&img);

    return value;
} // Java_ConvNet_runConv
