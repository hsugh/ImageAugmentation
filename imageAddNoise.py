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
add_noise = img.copy()
HEIGHT, WIDTH, CHANNEL = add_noise.shape
print(HEIGHT, WIDTH, CHANNEL)
noise = np.random.randint(5, size=(HEIGHT,  WIDTH, CHANNEL+1), dtype = 'uint8')
for i in range(HEIGHT):
    for j in range(WIDTH):
        for k in range(CHANNEL):
            if add_noise[i][j][k] != 255:
                add_noise[i][j][k] += noise[i][j][k]
    
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(add_noise)
plt.title('add_noise')
plt.show()