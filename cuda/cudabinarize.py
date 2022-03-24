from numba import cuda
import numba
import numpy as np
from PIL import Image


@cuda.jit('void(float32,float32)',device=True,inline=True)
def cuda_binarize(result, array, threshold):
    # binarize an image
    i = cuda.grid(1)  # equivalent to i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    val = 0.0
    if array[i] > threshold:
        val = 255.0
    result[i] = val


image = Image.open('einstein.jpg').convert('L')
image_np = np.array(image, dtype=np.float32)
width, height = image_np.shape
print(width, height)
result = np.empty_like(image_np)
cuda_binarize[width, height](result, image_np, np.float32(90))
# se convierte la imagen de tipo numpy a pillow
PIL_image = Image.fromarray(np.uint8(result))
PIL_image
