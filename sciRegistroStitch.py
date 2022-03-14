from skimage import io, transform,  color

import numpy as np
import matplotlib.pyplot as plt
import os

data_source='/home/madperez/Documentos/investigacion/images/incendios/recorridocosta0120/'
num_image=419

# Load the two landscape photos
img0 = color.rgb2gray(io.imread(data_source+'costa'+str(num_image)+'.jpg'))
img1 = color.rgb2gray(io.imread(data_source+'costa'+str(num_image+1)+'.jpg'))


def choose_corresponding_points():
    """Utility function for finding corresponding features in images.
    Alternately click on image 0 and 1, indicating the same feature.
    """
    f, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(img0, cmap='gray')
    ax1.imshow(img1, cmap='gray')

    coords = plt.ginput(8, timeout=0)

    np.savez('_reg_coords.npz', source=coords[::2], target=coords[1::2])

    plt.close()


# Re use previous coordinates, if found
if not os.path.exists('_reg_coords.npz'):
    choose_corresponding_points()

coords = np.load('_reg_coords.npz')

# Estimate the transformation between the two sets of coordinates,
# assuming it is an affine transform
tf = transform.estimate_transform('similarity', coords['source'], coords['target'])

# Use a translation transformation to center both images for display purposes
offset = transform.SimilarityTransform(translation=(-200, -170))

img0_warped = transform.warp(img0, inverse_map=offset,
                             output_shape=(600, 600))

img1_warped = transform.warp(img1, inverse_map=offset + tf,
                             output_shape=(600, 600))


# Find where both images overlap; in that region average their values
mask = (img0_warped != 0) & (img1_warped != 0)
registered = img0_warped + img1_warped
registered[mask] /= 2

# Display the results
#f, (ax0, ax1, ax2) = plt.subplots(1, 3, subplot_kw={'xticks': [], 'yticks': []})
fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2, sharex=ax1, sharey=ax1)
ax3 = plt.subplot(1, 3, 3)
ax3.imshow(img0, cmap='gray')
ax1.imshow(img1, cmap='gray')
ax2.imshow(registered, cmap='gray')

# ## ## Display image boundaries
# y, x = img1.shape[:2]
# box = np.array([[0, 0], [0, y], [x, y], [x, 0], [0, 0]])
# tf_box = (offset + tf).inverse(box)
# plt.plot(tf_box[:, 0], tf_box[:, 1], 'r-')

plt.show()
