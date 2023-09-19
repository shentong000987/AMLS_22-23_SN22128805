import os
import numpy as np
from skimage.io import imread

def img_reader(input_dir):

    data = []
    for file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, file)
        img = imread(img_path)
        data.append(img.flatten())
    data = np.array(data)

    return data