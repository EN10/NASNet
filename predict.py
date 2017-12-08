import numpy as np
import tensorflow as tf

from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from imageio import imread
from nasnet import mobile, preprocess
import nasnet

image = imread('peacock.jpg')

model = nasnet.mobile()
model.load_weights('mobile.h5')

size = model.input_shape[2]
x = np.expand_dims(preprocess(image, size=size), axis=0)

y = model.predict(x)

for index, res in enumerate(decode_predictions(y)[0]):
    print('{}. {}: {:.3f}%'.format(index + 1, res[1], 100 * res[2]))