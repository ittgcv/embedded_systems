import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from skimage import data, io, filters,  color,  exposure
import time

numimage=610
#from skimage.util import compare_images

image = data.coins()
# ... or any other NumPy array!
edges = filters.sobel(image)
#io.imshow(edges)
#io.show()

fig = plt.figure(figsize=(8, 9))
data_source='/home/madperez/Documentos/investigacion/images/incendios/recorridocosta0120/fotos_aereas/video10/'
gs = GridSpec(3, 2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1:, :])
img1=io.imread(data_source+'termica/frame'+str(numimage)+'ir.jpg')
imrgb=io.imread(data_source+'rgb/frame'+str(numimage)+'.jpg')
imgray=color.rgb2gray(img1)
im_eq=exposure.equalize_hist(imgray)
cm=plt.get_cmap('jet')
#comp_equalized = compare_images(img1, imrgb, method='checkerboard')
print(img1.shape)
colored_image=cm(im_eq)
ax0.imshow(img1, cmap='gray')
ax0.set_title('Original')
ax1.imshow(imrgb, cmap='gray')
ax1.set_title('Equalized')
ax2.imshow(colored_image)
ax2.set_title('Checkerboard comparison')
io.imsave(data_source+'framecolor'+str(numimage)+'.jpeg', color.rgba2rgb(colored_image))
for a in (ax0, ax1, ax2):
    a.axis('off')
plt.tight_layout()
plt.plot()
plt.show()
#time.sleep(5)
