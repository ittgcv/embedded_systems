from numba import cuda
import numpy as np
@cuda.jit
def cuda_binary(result, array, coeffs):
    # Evaluate a polynomial function over an array with Horner's method.
    # The coefficients are given in descending order.
    i = cuda.grid(1) # equivalent to i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    val = array[i]+coeffs
    result[i] = val
array = np.random.rand(10 * 10).astype(np.float32)
threshold = np.float32(90)
result = np.empty_like(array)
cuda_binary[10, 10](result, array, threshold)
print(array,result)
