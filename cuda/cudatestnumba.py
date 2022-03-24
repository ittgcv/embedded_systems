from numba import cuda
import numpy as np
@cuda.jit
def cudakernel0(array):
    for i in range(array.size):
        array[i] += 0.5
array = np.array([0, 1], np.float32)
print('Initial array:', array)
# one block and one thread per block
print('Kernel launch: cudakernel0[1, 1](array)')
cudakernel0[1, 1](array)
print('Updated array:',array)

# gridsize blocks and blocksize threads per block
gridsize = 1024
blocksize = 1024
print("Grid size: {}, Block size: {}".format(gridsize, blocksize))
print("Total number of threads:", gridsize * blocksize)
print('Kernel launch: cudakernel0[gridsize, blocksize](array)')
cudakernel0[gridsize, blocksize](array)
print('Updated array:',array)
# there are no control over the syncronisation

#cuda.grid() function that returns the absolute position of the current thread inside the whole grid.
@cuda.jit
def cudakernel1(array):
    thread_position = cuda.grid(1)
    array[thread_position] += 0.5
array = np.array([0, 1], np.float32)
print('Initial array:', array)
print('Kernel launch: cudakernel1[1, 2](array)')
cudakernel1[1, 2](array)
print('Updated array:',array)
