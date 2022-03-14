from io import BytesIO
from PIL import Image
from urllib2 import request
import matplotlib.pyplot as plt # this is if you want to plot the map using pyplot

url = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"

buffer = BytesIO(request.urlopen(url).read())
image = Image.open(buffer)

# Show Using PIL
image.show()

# Or using pyplot
plt.imshow(image)
plt.show()
