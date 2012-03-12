#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE cvmaxoperatorplane test
#define CHECK_MESSAGE(a, b) {                                       \
                                BOOST_CHECK_MESSAGE(a == b,         \
                                                  "target:" << b << \ 
                                                  " result:" << a); \
                            }


#include <boost/test/unit_test.hpp>
#include <opencv/cv.h>

#include "cvmaxoperatorplane.h"
#include "cvsourceplane.h"

BOOST_AUTO_TEST_CASE( cvmaxoperatorplane_test )
{
    // Create our test plane
    CvSize featureMap = cvSize(8, 8);
    CvSize neuronSize = cvSize(8, 8);
    CvMaxOperatorPlane maxOperatorPlane("test", featureMap, neuronSize);
    
    // test the basic forward propagation
    int testMatAValues[] = {
                              0,   1,   2,   3,   4,   5,   6,   7,
                              8,   9,  10,  11,  12,  13,  14,  15,
                             16,  17,  18,  19,  20,  21,  22,  23,
                             24,  25,  26,  27,  28,  29,  30,  31,
                             32,  33,  34,  35,  36,  37,  38,  39,
                             40,  41,  42,  43,  44,  45,  46,  47,
                             48,  49,  50,  51,  52,  53,  54,  55,
                             56,  57,  58,  59,  60,  61,  62,  63
                            };
    CvMat testMatA = cvMat(8, 8, CV_8UC1, testMatAValues);
    CHECK_MESSAGE(maxOperatorPlane.setfmap(&testMatA), 1);
} // BOOST_AUTO_TEST_CASE 


