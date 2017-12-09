from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.inception_v3 import preprocess_input, decode_predictions
import numpy as np
import nasnet

img = image.load_img('image.jpg', target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

model = nasnet.mobile()
model.load_weights('mobile.h5')

y = model.predict(x)
for index, res in enumerate(decode_predictions(y)[0]):
    print('{}. {}: {:.3f}%'.format(index + 1, res[1], 100 * res[2]))