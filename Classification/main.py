import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import time

img_width, img_height = 95, 95


model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
test_path = r'C:\Users\suhaa\Desktop\OCV\Chess_Detector'
