##Writeup Template
###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./output_images/car.jpg
[image2]: ./output_images/not_car.jpg
[image3]: ./output_images/Original.jpg
[image4]: ./output_images/HOG.jpg
[image5]: ./output_images/Combined_0.jpg
[image6]: ./output_images/Combined_1.jpg
[image7]: ./output_images/Combined_2.jpg
[image8]: ./output_images/Combined_3.jpg
[image9]: ./output_images/Combined_4.jpg
[image10]: ./output_images/Combines_5.jpg

##Rubric Points
###Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
###Writeup / README

####1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

Yes.

###Histogram of Oriented Gradients (HOG)

####1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The extraction of features for a given image is done in another file called `moreFunctions.py`. The function `hog_features()` extracts the features from a given image in all the 3 channels.

Initially there were two classes one for Cars and the other for Non-Cars.

![alt text][image1] ![alt text][image2]

For the extraction of HOG fetures I used:
* No. of orientation = 18
* pix_per_cell = 8
* cell_per_block = 2

Here is an example of HOG extraction on an image.

![alt text][image3] ![alt text][image4]

####2. Explain how you settled on your final choice of HOG parameters.

* For the colorspace of the image I tried some other colorspaces but "YUV" seemed to work the best.
* I also noticed that higher number of bins or spatial binning did not help in increasing the accuracy significantly.
* But increasing the number of orientations for HOG did increase the accuracy significantly.
* The final values for the parameters are:
	* Colorspace = 'YUV'
	* No. of Orientations = 18.
	* pix_per_cell = 8.
	* cell_per_block = 2.
	* No. of histogram bins = 16.
	* Size after spatially binning = (16,16).

####3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

* I did use the histogram and the spatial binning along with the HOG features for the image.
* All of the Three features were concatenated together in order to form a feature vector.
* This feature vector was passed into a Linear SVM for classification of the images.
* The calssification can be seen in the 8th cell of the Notebook.

###Sliding Window Search

####1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

* I fixed the Start and Stop coordinates for the Sliding Widow search at 400 and 656.
* Different scales were used : 1.5, 1.75, 2.0.
* The Sliding Window search is there in the 10th cell of the Notebook.


####2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Here are some example of some images.

![alt text][image5]

![alt text][image6]

![alt text][image7]

![alt text][image8]

![alt text][image9]

![alt text][image10]

---

### Video Implementation

####1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
The video has been uploaded in the repository.


####2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example's of all the test images given :

![alt text][image5]

![alt text][image6]

---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  

