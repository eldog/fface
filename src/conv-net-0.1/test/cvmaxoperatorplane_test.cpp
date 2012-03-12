#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE cvmaxoperatorplane test
#define CHECK_MESSAGE(a, b) {\
                                BOOST_CHECK_MESSAGE(a == b,\
                                                  "target:" << b <<\ 
                                                  " result:" << a);\
                            }
#include <vector>
#include <boost/test/unit_test.hpp>
#include <opencv/cv.h>

#include "cvgenericplane.h"
#include "cvmaxoperatorplane.h"
#include "cvsourceplane.h"

CvSourcePlane createTestCvSourcePlane()
{
    CvSize featureMapSize = cvSize(8, 8);
    return CvSourcePlane("test_source_plane", featureMapSize);
} // createTestCvSourcePlane

CvMaxOperatorPlane createTestMaxOperatorPlane(CvSize featureMapSize,
                                              CvSize neuronSize)
{
    return CvMaxOperatorPlane("test_max", featureMapSize, neuronSize);
} // createTestMaxOperatorPlane

BOOST_AUTO_TEST_CASE( cvmaxoperatorplane_test )
{
    // Create our max operatortest plane
    CvSourcePlane sourcePlane = createTestCvSourcePlane();
    
    // test the basic forward propagation
    double sourcePlaneFeatureMapValues[] = 
                        {
                              0,   1,   2,   3,   4,   5,   6,   7,
                              8,   9,  10,  11,  12,  13,  14,  15,
                             16,  17,  18,  19,  20,  21,  22,  23,
                             24,  25,  26,  27,  28,  29,  30,  31,
                             32,  33,  34,  35,  36,  37,  38,  39,
                             40,  41,  42,  43,  44,  45,  46,  47,
                             48,  49,  50,  51,  52,  53,  54,  55,
                             56,  57,  58,  59,  60,  61,  62,  63
                        };
    CvMat sourcePlaneFeatureMap = cvMat(8, 
                                        8, 
                                        CV_64FC1, 
                                        sourcePlaneFeatureMapValues);

    CHECK_MESSAGE(sourcePlane.setfmap(&sourcePlaneFeatureMap), 1);

    std::vector<CvGenericPlane *> parentPlanes;
    parentPlanes.push_back(&sourcePlane);

    // Test a 1 x 1 output
    CvMaxOperatorPlane maxOperatorPlane = 
        createTestMaxOperatorPlane(cvSize(1, 1), cvSize(8, 8));
    maxOperatorPlane.connto(parentPlanes);
    CHECK_MESSAGE(cvmGet(maxOperatorPlane.fprop(), 0, 0), 63);
    
    // Test a 2 x 2 output
    CvMaxOperatorPlane maxOperatorPlane2 = 
        createTestMaxOperatorPlane(cvSize(2, 2), cvSize(4, 4));
    maxOperatorPlane2.connto(parentPlanes);
    CvMat* fprop1 = maxOperatorPlane2.fprop();
    BOOST_CHECK(fprop1 != 0);
    CHECK_MESSAGE(cvmGet(fprop1, 0, 0), 27);
    CHECK_MESSAGE(cvmGet(fprop1, 0, 1), 31);
    CHECK_MESSAGE(cvmGet(fprop1, 1, 0), 59);
    CHECK_MESSAGE(cvmGet(fprop1, 1, 1), 63);

    CvMaxOperatorPlane maxOperatorPlane3 =
        createTestMaxOperatorPlane(cvSize(4, 4), cvSize(2, 2));
    maxOperatorPlane3.connto(parentPlanes);
    CvMat * fprop2 = maxOperatorPlane3.fprop();
    BOOST_CHECK(fprop2 != 0);
    CHECK_MESSAGE(cvmGet(fprop2, 0, 0), 9);
    CHECK_MESSAGE(cvmGet(fprop2, 0, 1), 11);
    CHECK_MESSAGE(cvmGet(fprop2, 0, 2), 13);
    CHECK_MESSAGE(cvmGet(fprop2, 0, 3), 15);
    CHECK_MESSAGE(cvmGet(fprop2, 1, 0), 25);
    CHECK_MESSAGE(cvmGet(fprop2, 1, 1), 27);
    CHECK_MESSAGE(cvmGet(fprop2, 1, 2), 29);
    CHECK_MESSAGE(cvmGet(fprop2, 1, 3), 31);
    CHECK_MESSAGE(cvmGet(fprop2, 2, 0), 41);
    CHECK_MESSAGE(cvmGet(fprop2, 2, 1), 43);
    CHECK_MESSAGE(cvmGet(fprop2, 2, 2), 45);
    CHECK_MESSAGE(cvmGet(fprop2, 2, 3), 47);
    CHECK_MESSAGE(cvmGet(fprop2, 3, 0), 57);
    CHECK_MESSAGE(cvmGet(fprop2, 3, 1), 59);
    CHECK_MESSAGE(cvmGet(fprop2, 3, 2), 61);
    CHECK_MESSAGE(cvmGet(fprop2, 3, 3), 63);

} // BOOST_AUTO_TEST_CASE 

BOOST_AUTO_TEST_CASE( cvsourceplane_test )
{
    CvSourcePlane sourcePlane = createTestCvSourcePlane();
    // Create our source plane to test
    int testFeatureMapValues[] = {
                                      0,   1,   2,   3,   4,   5,   6,   7,
                                      8,   9,  10,  11,  12,  13,  14,  15,
                                     16,  17,  18,  19,  20,  21,  22,  23,
                                     24,  25,  26,  27,  28,  29,  30,  31,
                                     32,  33,  34,  35,  36,  37,  38,  39,
                                     40,  41,  42,  43,  44,  45,  46,  47,
                                     48,  49,  50,  51,  52,  53,  54,  55,
                                     56,  57,  58,  59,  60,  61,  62,  63
                                 };
    CvMat testFeatureMap = cvMat(8, 8, CV_8UC1, testFeatureMapValues);
    CHECK_MESSAGE(sourcePlane.setfmap(&testFeatureMap), 1);
} // BOOST_AUTO_TEST_CASE

