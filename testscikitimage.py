import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from skimage import data, io, filters
from skimage.util import compare_images

image = data.coins()
# ... or any other NumPy array!
edges = filters.sobel(image)
io.imshow(edges)
io.show()

fig = plt.figure(figsize=(8, 9))

gs = GridSpec(3, 2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1:, :])
img1=io.imread('frame0ir.jpg')
imrgb=io.imread('frame0.jpg')
comp_equalized = compare_images(img1, imrgb, method='checkerboard')

ax0.imshow(img1, cmap='gray')
ax0.set_title('Original')
ax1.imshow(imrgb, cmap='gray')
ax1.set_title('Equalized')
ax2.imshow(comp_equalized, cmap='gray')
ax2.set_title('Checkerboard comparison')
for a in (ax0, ax1, ax2):
    a.axis('off')
plt.tight_layout()
plt.plot()
