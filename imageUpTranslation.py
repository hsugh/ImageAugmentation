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
shift_up = img.copy()
HEIGHT, WIDTH, _ = shift_up.shape
print(HEIGHT, WIDTH)

for i in range(HEIGHT):
    for j in range(WIDTH):
        if (i < HEIGHT - 20 and i > 20):
            shift_up[i][j] = shift_up[i + 20][j]
        else:
            shift_up[i][j] = 255

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(shift_up)
plt.title('shift_up')
plt.show()

