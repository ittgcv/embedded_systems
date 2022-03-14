import numpy as np
import matplotlib.pyplot as plt

from skimage.util import img_as_ubyte
from skimage import data,  io,  color
from skimage.exposure import histogram

numimage=147
data_source='/home/madperez/Documentos/investigacion/images/incendios/recorridocosta0120/'
img1=io.imread(data_source+'costa'+str(numimage)+'.jpg')
imrgb=io.imread(data_source+'costa'+str(numimage)+'.jpg')
imgray=color.rgb2gray(img1)
imhsv=color.rgb2hsv(img1)
imhue=imhsv[:, :, 0]

noisy_image = img_as_ubyte(imhue)
hist, hist_centers = histogram(noisy_image, nbins=2)
print(hist.max)
fig, ax = plt.subplots(ncols=3, figsize=(10, 5))

#ax[0].imshow(noisy_image, cmap=plt.cm.gray)
#ax[0].axis('off')

ax[0].plot(hist_centers, hist, lw=2)
ax[0].set_title('Histogram of grey values')
print(imhue.shape)
#ax[1].imshow(imhue, cmap=plt.cm.gray)
ax[1].imshow(imhue, cmap='hsv')
ax[1].axis('off')
ax[2].imshow(img1)
ax[2].axis('off')
print(np.argmax(hist))
plt.tight_layout()
plt.show()
