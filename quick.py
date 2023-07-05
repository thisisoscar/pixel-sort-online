from PIL import Image
import numpy as np

location = input('Enter the directory of the image you want to sort: ')

image = Image.open(location).convert('RGB')

image = image.convert('HSV')

pixels = list(image.getdata())

pixels.sort(key=lambda x: (x[0], x[2], x[1]))

pixels = np.array(pixels)

pixels = pixels.reshape(image.height, image.width, 3)

new_image = Image.fromarray(pixels.astype(np.uint8), 'HSV')

image.show()
new_image.show()
