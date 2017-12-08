import nasnet

# NASNet-A_Mobile_224
model = nasnet.mobile(load_weights=True)
model.save_weights('mobile.h5')