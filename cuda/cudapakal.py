from numba import cuda
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from pdb import set_trace


@cuda.jit
def colorize(colorr, colores, image_pakal):
    # binarize an image
    i = cuda.grid(1)  # equivalent to i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    val_pixel = image_pakal[i]
    colorr[i] = val_pixel


@cuda.jit
def convolve(result, maska, maskb, maskc, lut_vector_referencia, image):
    # expects a 2D grid and 2D blocks,
    # a mask with odd numbers of rows and columns, (-1-)
    # a grayscale image

    # (-2-) 2D coordinates of the current thread:
    i, j = cuda.grid(2)
    # rows of vectors of reference
    reference_rows = lut_vector_referencia.shape[0]

    # (-3-) if the thread coordinates are outside of the image, we ignore the thread:
    image_rows, image_cols = image.shape
    if (i >= image_rows) or (j >= image_cols):
        return

    # To compute the result at coordinates (i, j), we need to use delta_rows rows of the image
    # before and after the i_th row,
    # as well as delta_cols columns of the image before and after the j_th column:
    delta_rows = maska.shape[0] // 2
    delta_cols = maska.shape[1] // 2

    # The result at coordinates (i, j) is equal to
    # sum_{k, l} mask[k, l] * image[i - k + delta_rows, j - l + delta_cols]
    # with k and l going through the whole mask array:
    sa = 0
    sb = 0
    sc = 0
    for k in range(maska.shape[0]):
        for l in range(maska.shape[1]):
            i_k = i - k + delta_rows
            j_l = j - l + delta_cols
            # (-4-) Check if (i_k, j_k) coordinates are inside the image:
            if (i_k >= 0) and (i_k < image_rows) and (j_l >= 0) and (j_l < image_cols):
                sa += maska[k, l] * image[i_k, j_l]
                sb += maskb[k, l] * image[i_k, j_l]
                sc += maskc[k, l] * image[i_k, j_l]
                # magnitude of vector describing the window
                m1 = math.sqrt(sa * sa + sb * sb + sc * sc)
                minimum_difference = 2 * 3.14
                d_min = 0
                for item in range(reference_rows):
                    dot_vectors = math.sqrt(
                        sa * lut_vector_referencia[item, 1] + sb * lut_vector_referencia[item, 2] + sc *
                        lut_vector_referencia[item, 2])
                    difference_vectors = math.acos(dot_vectors / m1 / lut_vector_referencia[item, 0])
                    # print(difference_vectors)
                    # if i == 0 and j==0:
                    #    set_trace()
                    ###
                    if difference_vectors < minimum_difference:
                        minimum_difference = difference_vectors
                        d_min = item

    # valdif=int(minimum_difference*10)
    result[i, j] = item
    print('item', i, j, item)


# full_image = rgb2gray(skimage.data.coffee()).astype(np.float32) / 255
# plt.figure()
# plt.imshow(full_image, cmap='gray')
# plt.title("Full size image:")
# image = full_image[150:350, 200:400].copy() # We don't want a view but an array and therefore use copy()
# vectores de referencia [cuadrante, vector]
def pakal_color(im_pakal, lut):
    rows, cols = im_pakal.shape
    im_color = np.zeros((rows, cols, 3))
    for i in range(rows):
        for j in range(cols):
            # print(i,lut[int(im_pakal[i,j])])
            try:
                im_color[i, j, :] = lut[int(im_pakal[i, j])]
            except:
                pass
    return im_color


# [cuadrante, vector]
lut_vector_referencia = np.array(
    [[0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [2, -1, 1, 1], [2, -1, 0, 1], [3, -1, -1, 1],
     [3, 0, -1, 1], [4, 1, -1, 1]])
lut_colores = np.array(
    [[255, 0, 0], [255, 128, 0], [255, 255, 0], [128, 255, 0], [0, 255, 0], [0, 255, 128], [0, 255, 255], [0, 128, 255],
     [0, 0, 255]])
# se transforma a [magnitud, vector]
r, c = lut_vector_referencia.shape
for i in range(r):
    vector = lut_vector_referencia[i, 1:4]
    lut_vector_referencia[i, 0] = np.sqrt(vector.dot(vector))
image_pil = Image.open('einstein.jpg').convert('L')
new_size = (255, 255)
image_pil = image_pil.resize(new_size)
image = np.array(image_pil, dtype=float)
rows, cols = image.shape
print(rows, cols)
# plt.figure()
# plt.imshow(image_pil, cmap='gray')
# plt.title("Part of the image we use:")
# plt.show()
# We preallocate the result array:
result = np.empty_like(image)
# resultr = np.empty_like(image)

# We choose a random mask:
# mask = np.random.rand(13, 13).astype(np.float32)
# mask /= mask.sum()  # We normalize the mask
maska = np.array([[-1 / 6, -1 / 6, -1 / 6], [0, 0, 0], [1 / 6, 1 / 6, 1 / 6]])
maskb = np.array([[-1 / 6, 0, 1 / 6], [-1 / 6, 0, 1 / 6], [-1 / 6, 0, 1 / 6]])
maskc = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
vector = np.zeros(3)
# We use blocks of 32x32 pixels:
blockdim = (32, 32)
print('Blocks dimensions:', blockdim)

# We compute grid dimensions big enough to cover the whole image:
griddim = (image.shape[0] // blockdim[0] + 1, image.shape[1] // blockdim[1] + 1)
print('Grid dimensions:', griddim)

# We apply our convolution to our image:
convolve[griddim, blockdim](result, maska, maskb, maskc, lut_vector_referencia, image)
# colorize[griddim, blockdim](resultr, lut_colores, result)
resultr = pakal_color(result, lut_colores)

# We plot the result:
plt.figure()
plt.imshow(image, cmap='gray')
plt.title("Before convolution:")
plt.figure()
plt.imshow(resultr, cmap='gray')
plt.title("After convolution:")
plt.show()
