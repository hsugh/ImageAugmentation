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
img = np.array(img) # 将图片像素矩阵转为数组
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
img_flip = np.fliplr(img)
plt.subplot(1, 2, 2)
plt.imshow(img_flip)
plt.title('Flipped')
plt.show()