from PIL import Image
import numpy as np


def collage_maker(image1, image2, new):
    img1 = np.array(image1)
    img2 = np.array(image2)

    collage = np.vstack([img1, img2])
    image = Image.fromarray(collage, 'RGB')
    image.save(new)


collage_maker("1.jpg", "2.jpg", "new.jpg")
