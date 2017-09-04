import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.feature import hog

# Function for converting between colorspaces
def color_space(img, cspace):
	if cspace == 'YCrCb':
		return cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
	elif cspace == 'HSV':
		return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
	elif cspace == 'HLS':
		return cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
	elif cspace == 'LUV':
		return cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
	else:
		return img

# Resizing the image
def bin_spatial(img, size):
	resize_img = cv2.resize(img, size)
	feature_vec = resize_img.ravel()
	return feature_vec

# Generating the histogram og the image in a particular colorspace
def histogram_formation(img, nbins):
	channel1_hist,_ = np.histogram(img[:,:,0], bins=nbins)
	channel2_hist,_ = np.histogram(img[:,:,1], bins=nbins)
	channel3_hist,_ = np.histogram(img[:,:,2], bins=nbins)
	hist_features = np.concatenate((channel1_hist, channel2_hist, channel3_hist))
	return hist_features

# Generating the HOG in all three Color Spaces

def hog_features(img, orient, pix_per_cell, cell_per_block, feature_vec=True):
	feature_c1, hog_image_c1 = hog(img[:,:,0], orientations=orient, pixels_per_cell=(pix_per_cell,pix_per_cell),
								cells_per_block=(cell_per_block,cell_per_block), visualise=True, feature_vector=feature_vec)

	feature_c2, hog_image_c2 = hog(img[:,:,1], orientations=orient, pixels_per_cell=(pix_per_cell,pix_per_cell),
								cells_per_block=(cell_per_block,cell_per_block), visualise=True, feature_vector=feature_vec)
	feature_c3, hog_image_c3 = hog(img[:,:,2], orientations=orient, pixels_per_cell=(pix_per_cell,pix_per_cell),
								cells_per_block=(cell_per_block,cell_per_block), visualise=True, feature_vector=feature_vec)
	hog_image = cv2.merge((hog_image_c1,hog_image_c2,hog_image_c3))

	if feature_vec:
		feature = np.concatenate((feature_c1, feature_c2, feature_c3))
		return feature, hog_image
	else:
		return feature_c1, feature_c2, feature_c3, hog_image

	

# Using the above functions to generate the histogram
def feature_extraction(img, cspace='RGB', re_img = (32,32), hist_bins=32,
						orient=9, pix_per_cell=8, cell_per_block=2):
	
	# Changing the color space
	cs_img = color_space(img, cspace)

	# Resize the image
	resize_img = bin_spatial(cs_img, re_img)

	# Forming histograms w.r.t color spaces
	hist_feature = histogram_formation(cs_img, hist_bins)

	# Applying HOG (Histogram of oriented Gradients)
	hog_feature, hog_image = hog_features(cs_img, orient, pix_per_cell, cell_per_block)
	#hog_feature = np.ravel(hog_feature) # Falttening out the features
	features = np.concatenate((resize_img, hist_feature, hog_feature)) # Concatenating all the features
	#print("Resized Image: ", resize_img.shape)
	#print("Histogram : ", hist_feature.shape)
	#print("hog feature :",hog_feature.shape)

	return features, hog_image