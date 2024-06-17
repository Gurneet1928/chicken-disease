import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    """
    To Load the Model and Predict the Image
    """
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts","training","trained_model.keras"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)s

        if result[0] == 0:
            prediction = "No Tumor"

        else:
            prediction = "Tumor Detected"

        return [{"image >> " : prediction}]
    
        