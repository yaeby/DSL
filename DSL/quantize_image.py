import numpy as np
from kmeans import Kmeans

class ImageQuantizer:

    def __init__(self, b):
        self.b = b

    def quantize(self, img):
        b = self.b
        C, R, D = img.shape
        self.img = img
        X = np.reshape(img, (C * R, D))
        model = Kmeans(k=pow(2, b))
        model.fit(X)
        self.model = model
        return model.means

    def dequantize(self):
        model = self.model
        means = model.means
        img = self.img
        C, R, D = img.shape
        X = np.reshape(img, (C * R, D))
        y = model.predict(X)
        quantized_img = np.copy(self.img)
        for c in range(C):
            for r in range(R):
                quantized_img[c, r] = means[y[c * R + r]]
        return quantized_img