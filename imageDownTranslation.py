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
shift_down = img.copy()
HEIGHT, WIDTH, _ = shift_down.shape
print(HEIGHT, WIDTH)

for i in range(HEIGHT, 1, -1):
    for j in range(WIDTH):
        if (i < 144 and i > 20):
            shift_down[i][j] = shift_down[i - 20][j]

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(shift_down)
plt.title('shift_down')
plt.show()

