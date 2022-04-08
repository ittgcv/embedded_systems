from numba import cuda
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


@cuda.jit
def stereo_sad(result, mask, im_left, im_right, dmax):
    # expects a 2D grid and 2D blocks,
    # a mask with odd numbers of rows and columns, (-1-)
    # a grayscale image

    # (-2-) 2D coordinates of the current thread:
    i, j = cuda.grid(2)

    # (-3-) if the thread coordinates are outside of the image, we ignore the thread:
    image_rows, image_cols = im_left.shape
    if (i >= image_rows) or (j >= image_cols):
        return

    # To compute the result at coordinates (i, j), we need to use delta_rows rows of the image
    # before and after the i_th row,
    # as well as delta_cols columns of the image before and after the j_th column:
    delta_rows = mask.shape[0] // 2
    delta_cols = mask.shape[1] // 2

    # The result at coordinates (i, j) is equal to
    # sum_{k, l} mask[k, l] * image[i - k + delta_rows, j - l + delta_cols]
    # with k and l going through the whole mask array:
    dmin = 0
    cmin = 5000
    for d in range(dmax):
        s = 0
        for k in range(mask.shape[0]):
            for l in range(mask.shape[1]):
                i_k = i - k + delta_rows
                j_l = j - l + delta_cols
                # (-4-) Check if (i_k, j_k) coordinates are inside the image:
                if (i_k >= 0) and (i_k < image_rows) and (j_l >= 0) and (j_l < image_cols):
                    s += abs(im_left[i_k, j_l] - im_right[i_k, j_l + d])
        if s < cmin:
            cmin = s
            dmin = d
    result[i, j] = dmin * dmax


image_left = Image.open('tsukuba_left.png').convert('L')
image_right = Image.open('tsukuba_right.png').convert('L')
imnp_left = np.array(image_left, dtype=np.float)
imnp_right = np.array(image_right, dtype=np.float)
# plt.figure()
# plt.imshow(image_left, cmap='gray')
# plt.title("Part of the image we use:")
# plt.show()
# We preallocate the result array:
result = np.empty_like(imnp_left)

# We choose a random mask:
mask = np.random.rand(7, 7).astype(np.float32)
mask /= mask.sum()  # We normalize the mask
print('Mask shape:', mask.shape)
print('Mask first (3, 3) elements:\n', mask[:3, :3])

# We use blocks of 32x32 pixels:
blockdim = (32, 32)
print('Blocks dimensions:', blockdim)

# We compute grid dimensions big enough to cover the whole image:
griddim = (imnp_left.shape[0] // blockdim[0] + 1, imnp_left.shape[1] // blockdim[1] + 1)
print('Grid dimensions:', griddim)
dmax = 15
# We apply our convolution to our image:
stereo_sad[griddim, blockdim](result, mask, imnp_left, imnp_right, dmax)

# We plot the result:
plt.figure()
plt.imshow(image_left, cmap='gray')
plt.title("Before convolution:")
plt.figure()
plt.imshow(result, cmap='gray')
plt.title("After convolution:")
plt.show()
