#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE cvmaxoperatorplane test

#include <boost/test/unit_test.hpp>
#include <opencv/cv.h>

#include "cvmaxoperatorplane.h"

BOOST_AUTO_TEST_CASE( cvmaxoperatorplane_test )
{
    CvSize featureMap = cvSize(2, 2);
    CvSize neuronSize = cvSize(2, 2);
    CvMaxOperatorPlane maxOperatorPlane("test", featureMap, neuronSize);
} // BOOST_AUTO_TEST_CASE 


