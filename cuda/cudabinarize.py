from numba import cuda
import numba
import numpy as np
from PIL import Image


@cuda.jit
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
x = np.reshape(image_np,width*height)
print(width, height)
result = np.empty_like(x)
threshold=np.float32(90.0)
print(threshold)
cuda_binarize[width, height](result, x, threshold)
# se convierte la imagen de tipo numpy a pillow
print(result[:50])
result_=np.reshape(result,(width,height))
PIL_image = Image.fromarray(np.uint8(result_))
PIL_image.show()
