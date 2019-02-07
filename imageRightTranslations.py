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
shift_right = img.copy()
HEIGHT, WIDTH, _ = shift_right.shape
print(HEIGHT, WIDTH)

for i in range(WIDTH):
    for j in range(HEIGHT):
        if (i < WIDTH - 20):
            shift_right[j][i] = shift_right[j][i + 20]

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(shift_right)
plt.title('shift_right')
plt.show()
