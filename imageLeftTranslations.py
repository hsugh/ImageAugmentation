from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

try:
    os.chdir(os.path.join(os.getcwd(), '..'))
    print(os.getcwd())
except:
    pass

img = Image.open('./NIKE.png')
img = np.array(img)
shift_left = img.copy()
HEIGHT, WIDTH, _ = shift_left.shape
print(HEIGHT, WIDTH)


#左移
for i in range(WIDTH, 1, -1):
    for j in range(HEIGHT):
        if (i < WIDTH - 20):
            shift_left[j][i] = shift_left[j][i - 20]
        elif (i < WIDTH - 1):
            shift_left[j][i] = 255

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(shift_left)
plt.title('shift_left')
plt.show()