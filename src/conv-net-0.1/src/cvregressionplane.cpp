/*****************************************************************************
 IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING. By
downloading, copying, installing or using the software you agree to this
license. If you do not agree to this license, do not download, install, copy or
use the software.

Contributors License Agreement

Copyright© 2007, Akhmed Umyarov. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.
- The name of Contributor may not be used to endorse or promote products derived
from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
All information provided related to future Intel products and plans is
preliminary and subject to change at any time, without notice.
*****************************************************************************/

/*!\file
 * \brief Implementation of regression plane class
 * \author Lloyd Henning
 * \date 2012
 */

#include "cvregressionplane.h"
#include "cvfastsigmoid.h"
#include <iostream>
#include <sstream>

using namespace std;

// Constructors/Destructors
//  

/*!
 * Constructor creates a new regression plane with specified name,
 * specified size of feature map and specified size of "neuron window"
 * \param id name of the plane
 * \param fmapsz size of the featuremap for this plane
 * \param neurosz size of "neuron window" (for instance 5x5 means that
 * we have a neuron that is connected to 25 outputs of his 
 * parent(s) neuron feature map)
 *
 * The output is only ever going to be scalar
 *
 */
CvRegressionPlane::CvRegressionPlane  (std::string id, CvSize neurosz)
	: CvGenericPlane(id, cvSize(1, 1), neurosz) 
{
 	// Init weights for the neuron of regression plane
 	m_weight.resize(neurosz.height * neurosz.width + 1);
}

CvRegressionPlane::~CvRegressionPlane ( ) 
{ 
}

//  
// Methods
//  

/*! The method forward-propagates data from neuron parents to neuron's 
 * own feature map.
 * Each neuron knows his parents, thus there are no input parameters.
 * \return Pointer to plane's featuremap
 */
CvMat* CvRegressionPlane::fprop()
{
    assert( m_connected );
    // Start with the bias
    int w_index = 0;
    float sum = m_weight[w_index];
    for (int pfmap_index = 0; pfmap_index < m_pplane.size(); pfmap_index++)
    {
        CvMat *fmap = m_pfmap[pfmap_index];
        for (int row = 0; row < m_neurosz.height; row++)
        {
            for (int col = 0; col < m_neurosz.width; col++)
            {
               sum += m_weight[++w_index] * cvmGet(fmap, row, col);
            } // for col
        } // for row
    } // for pfmap_index
    cvmSet(m_fmap, 0, 0, sum);
    return m_fmap;
} // CvRegressionPlane::fprop()


/*! The method produces an XML representation of the complete information about 
 * the plane including information about weights of neuron and connection to
 * parents.
 * The representation does NOT include current state of the plane
 * such as its feature map.
 * The method is mainly used by the CvConvNet object.
 * \return string containing XML description of the plane
 */
string CvRegressionPlane::toString ( ) 
{
	ostringstream xml;
 	xml << "\t<plane id=\"" << m_id << "\" type=\"regression\" featuremapsize=\"" << m_fmapsz.width << "x" << m_fmapsz.height << "\" neuronsize=\"" << m_neurosz.width << "x" << m_neurosz.height << "\">" << endl;

	int windowsz = m_neurosz.height*m_neurosz.width;
	
	xml << "\t\t<bias> " << m_weight[0] << " </bias>" << endl; // Print bias
	// Then print the weights
	
	for (int i=0; i <m_pplane.size(); i++)
	{
		xml << "\t\t<connection to=\"" << m_pplane[i]->getid() << "\"> ";
		for (int j=0;j<windowsz; j++)
		{
				xml << m_weight[j+i*windowsz+1] << " ";
		}
		xml << "</connection>" << endl;
	}
	xml << "\t</plane>" << endl;
	
	return xml.str();
}

/*! The method explicitly sets the weights of the neuron
 * connto() should be invoked BEFORE any attempt to set weights
 * since weights have meaning only when connected
 * \param weights vector of weights to be set. 
 * The vector should contain all weights for ALL connections 
 * \return status of operation
 */
int CvRegressionPlane::setweight(std::vector<float> &weights)
{	
	// Check that the number of weights passed is sane
	if (weights.size() != (m_neurosz.width*m_neurosz.height*m_pplane.size()+1))
		return 0;

	return CvGenericPlane::setweight(weights);
}
