import numpy as np
from numba import cuda, float32

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
A=np.matrix([[1,2,3],[1,2,3],[1,2,3]])
B=np.matrix([[1,2,3],[1,2,3],[1,2,3]])
C=np.empty_like(A)
TPB = 3

@cuda.jit
def median_mat(A, C):
    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x    # blocks per grid

    if x >= C.shape[0] and y >= C.shape[1]:
        # Quit if (x, y) is outside of valid C boundary
        return

    # Each thread computes one element in the result matrix.
    # The dot product is chunked into dot products of TPB-long vectors.
    tmp = 0.
    for i in range(bpg):
        # Preload data into shared memory
        sA[tx, ty] = A[tx+i*TPB, ty + i * TPB]
        #sB[tx, ty] = B[tx + i * TPB, y]

        # Wait until all threads finish preloading
        cuda.syncthreads()

        # Computes partial product on the shared memory
        for j in range(TPB):
            tmp += sA[tx, ty]

        # Wait until all threads finish computing
        cuda.syncthreads()

    C[x, y] = tmp
median_mat[3,3](A,C)
cuda.synchronize()
print(A,B,C)
