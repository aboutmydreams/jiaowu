from PIL import Image
import numpy as np
import pandas as pd
import scipy.misc



np.set_printoptions(threshold = np.inf)

def cut_img(num):
    img = Image.open('imgs/{}.png'.format(str(num)))
    img = img.convert('L')
    box1 = (4, 4, 12, 16)
    box2 = (14, 4, 22, 16)
    box3 = (24, 4, 32, 16)
    box4 = (34, 4, 42, 16)
    box5 = (44, 4, 52, 16)
    img1 = img.crop(box1)
    img2 = img.crop(box2)
    img3 = img.crop(box3)
    img4 = img.crop(box4)
    img5 = img.crop(box5)
    imgs = [img1, img2, img3, img4]

    mode = np.asarray(img5)
    mode = np.where(mode<120,0,255)
    print(mode)
    # print(img.format,img.size,img.mode)
    # img1.show()
    return img2

# ximgs = []
# i = 0
# mode1 = np.asarray(cut_img(0))

# while i < 10:
#     ximgs.append(cut_img(i))
#     mode2 = np.asarray(cut_img(i + 1))
#     mode1 = np.hstack((mode1, mode2))
#     i += 1
# print(mode1, type(mode1))

# image1 = Image.fromarray(mode1)
# image1.show()


cut_img(13)
