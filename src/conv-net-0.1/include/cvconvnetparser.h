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
 * \brief XML Parser header
 * \author Akhmed Umyarov
 * \date 2007
 */

#ifndef CVCONVNETPARSER_H
#define CVCONVNETPARSER_H

//! Maximum size of plane feature map
/*! When XML parser encounters an attempt to create 
 *  a featuremap bigger than this constant, it is interpreted
 *  as an error.
 */
const int CVCONVOLUTIONALNET_MAX_FMAPSZ=129;

#include <map>
#include <vector>
#include <string>

class CvGenericPlane;

int parse(std::string xml, std::string &creator,
		std::string &name, 
		std::string &info, 
 		std::vector<CvGenericPlane *> &plane,
		std::map<std::string,int> &idmap);

#endif // CVCONVNETPARSER_H
