from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import numpy as np

def get_classes(file_path):
    # model = myModel(weights="imagenet")
    model = load_model("https://www.mediafire.com/file/4kqodbiqke74c2t/VGG16_32_epochs_new.h5")
    img = image.load_img(file_path, target_size=(240, 240))
    img=img_to_array(img)
    img=np.expand_dims(img,axis=0)
    predictions = model.predict(img)
    return predictions
