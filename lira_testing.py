"""
This file will test the post_processing's denoise_predictions method, on data
    obtained from some predictions used in a separate LIRA project.
More info on these predictions below.

-Blake Edwards / Dark Element
"""
import numpy as np
import sys, cv2, h5py
import post_processing
from post_processing import *

def get_concatenated_row(samples):
    """
    Concatenate each sample in samples horizontally, along axis 1.
    Return the resulting array.
    """
    return np.concatenate([sample for sample in samples], axis=1)

def get_concatenated_col(samples):
    """
    Concatenate each sample in samples vertically, along axis 0.
    Return the resulting array.
    """
    return np.concatenate([sample for sample in samples], axis=0)

def generate_overlay(img, predictions, colors, sub_h, sub_w):
    """
    Arguments:
        img: a np array of shape (h, w, 3),
            h is obtained by prediction_h * sub_h
            w is obtained by prediction_w * sub_w
            3 is color channel.
        predictions: an int np array of shape (prediction_h, prediction_w)
            with each entry being an index for the colors array, a prediction.
        colors: a list of colors for each prediction, a color key.
        sub_h, sub_w: heights of our subsections to assign each prediction to.

    Modifies the given image by placing rectangles of the color specified by each index in the predictions array,
        so that the resulting image is a bunch of colored rectangles of size sub_h x sub_w

    This is useful when we have predictions that are scalars for large areas, such as 80x145, and want to scale them up to overlay them.
    """

    for row_i, row in enumerate(predictions):
        for col_i, prediction in enumerate(row):
            color = colors[int(prediction)]
            img[row_i*sub_h:row_i*sub_h+sub_h, col_i*sub_w:col_i*sub_w+sub_w] = color

"""
Ok, so here's what happens.
Denoising is usually thought of as applying to images, where we have some random noise from a guassian distribution,
    or maybe a low resolution image, or something. Just having a bit of static or something on the image, as a start.
This is "noise", and the goal of "de-noising" is to remove the noise, as you probably could guess. 

However, these denoising algorithms can be applied to other things as well, as long as they are in the format of an image.
    i.e. a matrix.

In the LIRA project, we had these massive input images (about size 65,000 x 30,000 pixels), and we got classifications on the images
    by sliding an 80x145 window across these images, getting predictions on each 80x145 window.

Each of these predictions were a vector across the possible classifications each subsection could be, such that the predictions array ended
    up being a 3-tensor, of shape (h, w, class_n).

If we're being really specific, h = image height // subsection height, w = image width // subsection width. But you don't need to keep this in mind,
    just remember that the predictions array is a 3-tensor, so we can essentially treat it as an image, with each "pixel" being the prediction vector
    for a subsection.

Since our LIRA classifier made a lot of random miscellaneous mistakes throughout these massive images (as you'd expect, the images were REALLY big),
    we wanted to remove these miscellaneous mistakes.

So, we denoised them! The script found in post_processing does exactly this, extended from a paper here:

    http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0051947

Which talks about the case for binary labels. We extended it to multiclass classification.

After denoising them, we wanted to test to see how well they were improved from the original. 
So, for each "pixel" in the predictions array, we draw a colored rectangle of sub_h x sub_w size,
    with the color indexed from our colors list, with the index determined by the argmax of the prediction vector, 
    for that "pixel" in the predictions array. 

For an example, if we had the vector [0.3, 0.8, 0.1] as one entry in our predictions, 
    we'd argmax that to get the index 1, then we'd reference our colors list to get some unique color for that index / classification,
    like (255, 0, 0) (red) or (0, 255, 0) (blue).
"""

"""
The size to draw each of our predictions (as colored rectangles). Was originally 80x145 but can be smaller for quick viewing or really any size.
"""
sub_h = 4
sub_w = 7

"""
Essentially our smoothing parameter, this changes how much importance we put on the neighbors of each pixel,
    or in this case each neighboring prediction. 
Higher values mean smoother results, and vice versa. 
Use with caution however, as higher values may result in losing too much data about the original image.
"""
neighbor_weight = 0.8

"""
Our color key, to go from classification index to a color for that classification's rectangle
"""
colors = [(255, 0, 255), (0, 0, 255), (0, 255, 0), (200, 200, 200), (0, 255, 255), (255, 0, 0), (244,66,143)]

"""
Loop through all the predictions in our predictions.h5 file, to get plenty of tests.
Each dataset in the file is a 3-tensor of predictions for an image, so we can just loop through the number of keys.
"""
with h5py.File("predictions.h5") as hf:
    img_n = len(hf.keys())
    for img_i in range(img_n):
        """
        Print for progress
        """
        sys.stdout.write("\rImage %i / %i" % (img_i, img_n))
        sys.stdout.flush()

        """
        Each of our datasets is conveniently named as the index of the image, 
            so we can just cast each image index to a string to get the dataset.
        """
        predictions = np.array(hf.get(str(img_i)))

        """
        Get this info from our array
        """
        h, w, class_n = predictions.shape

        """
        Denoise the predictions using our denoise_predictions method from post_processing.py .
        Documentation for that can be found there.
        """
        denoised_predictions = denoise_predictions(predictions, neighbor_weight)

        """
        For both our original and denoised predictions,
            1. Argmax our predictions so we have indices to reference when getting colors,
            2. Create a zeroed img to store the colored overlay of predictions in,
            3. Then generate an overlay with our zeroed img, predictions, and colors (and sub_h and sub_w).
        """
        predictions = np.argmax(predictions, axis=2)
        predictions_img = np.zeros((h*sub_h, w*sub_w, 3), dtype=np.uint8)
        generate_overlay(predictions_img, predictions, colors, sub_h, sub_w)

        denoised_predictions = np.argmax(denoised_predictions, axis=2)
        denoised_predictions_img = np.zeros((h*sub_h, w*sub_w, 3), dtype=np.uint8)
        generate_overlay(denoised_predictions_img, denoised_predictions, colors, sub_h, sub_w)

        """
        Then concatenate the images horizontally for easy comparison,
            and save them to an image of the same name as our image index.
        """
        comparison_img = get_concatenated_row((predictions_img, denoised_predictions_img))
        cv2.imwrite("results/%i.jpg"%(img_i), comparison_img)

