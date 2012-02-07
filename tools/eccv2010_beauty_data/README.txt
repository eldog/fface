HOTorNOT dataset, v1.0

Doug Gray (dr.de3ug@gmail.com)

Legal:
This dataset was collected from the website www.hotornot.com with permission from the staff durring the summer of 2007.  Users who upload photos to this site implicitly waive all reasonable rights to privacy.  This data is made available to other researchers strictly for scientific research.  You may not publicly redistribute it without permission from the author.  If you wish to use this data in your research please be sure to cite our ECCV 2010 paper:

D. Gray, K. Yu, W. Xu, Y. Gong, "Predicting Facial Beauty without Landmarks", European Conference on Computer Vision (ECCV), 2010.

Usage:
The folder hotornot_face contains 2056 face images with score information given in hotornot_face_all.xml.  Additionally the number of ratings used to compute the score is given to allow filtering of uncertain scores.  Note that this filtering has already been done for the 5 train test splits given in eccv2010_split1-5.csv.  If you wish to compare your algorithm to ours, please report the average performance on these 5 train test splits.  Also note that these images are unaligned, however our results used images that were aligned using an automated algorithm.  We found that alignment could significantly improve performance for this task, your millage may vary.

