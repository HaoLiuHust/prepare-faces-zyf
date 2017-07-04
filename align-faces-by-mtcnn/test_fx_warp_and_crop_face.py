# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:32:00 2017

@author: zhaoy
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

from fx_warp_and_crop_face import warp_and_crop_face, get_normalized_5points

img_fn = './Jennifer_Aniston_0016.jpg'
#imgSize = [96, 112]; # cropped dst image size

# facial points in cropped dst image
#    coord5points = [[30.2946, 65.5318, 48.0252, 33.5493, 62.7299],
#                    [51.6963, 51.5014, 71.7366, 92.3655, 92.2041]];

# facial points in src image
#facial5points = [[105.8306, 147.9323, 121.3533, 106.1169, 144.3622],
#                 [109.8005, 112.5533, 139.1172, 155.6359, 156.3451]];
facial5points = [[ 105.8306,  109.8005],
       [ 147.9323,  112.5533],
       [ 121.3533,  139.1172],
       [ 106.1169,  155.6359],
       [ 144.3622,  156.3451]
       ];

def test(img_fn, facial5points, normalized_facial_points=None, output_size=(112,96)):
    print('Loading image {}'.format(img_fn))
    image = cv2.imread(img_fn, True);

    #for pt in pts_src[0:3]:
    #    cv2.circle(image, (int(pt[0]), int(pt[1])), 3, (255, 255, 0), 1, 8, 0)

    image_show = image[...,::-1]# swap BGR to RGB to show image by pyplot

    plt.figure();
    plt.imshow(image_show)
    #dst_img = transform_and_crop_face(image, facial5points, coord5points, imgSize)

    dst_img = warp_and_crop_face(image, facial5points, normalized_facial_points, output_size)
    print 'warped image shape: ', dst_img.shape

    dst_img_show = dst_img[...,::-1]# swap BGR to RGB to show image by pyplot

    plt.figure()
    plt.imshow(dst_img_show )

test(img_fn, facial5points)

# crop settings, set the region of cropped faces
output_square = True
padding_factor = 0.25
output_padding = (0, 0)
output_size = (224, 224)

# get the normalized 5 landmarks position in the crop settings
normalized_5pts = get_normalized_5points(
    output_size, padding_factor, output_padding, output_square)
print normalized_5pts

test(img_fn, facial5points, normalized_5pts, output_size)
