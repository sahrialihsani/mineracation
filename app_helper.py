# # from tensorflow.keras.applications.resnet50 import ResNet50 as myModel
# from tensorflow.keras import load_model
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# from tensorflow.keras.preprocessing import image
# import numpy as np

# def get_classes(file_path):
#     # model = myModel(weights="imagenet")
#     model = load_model("VGG16_50_epochs_new.h5")
#     img = image.load_img(file_path, target_size=(150, 150))
#     x = image.img_to_array(img)
#     x= np.array([x])
#     x = preprocess_input(x)
#     preds = model.predict(x)
#     predictions = decode_predictions(preds, top=3)[0]
#     return predictions
# from tensorflow.keras.applications.resnet50 import ResNet50 as myModel
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import numpy as np

def get_classes(file_path):
    # model = myModel(weights="imagenet")
    model = load_model("https://drive.google.com/file/d/1EdV19ekRbnID25f3FXogLQ03h-HxW8yN/view?usp=sharing")
    img = image.load_img(file_path, target_size=(240, 240))
    img=img_to_array(img)
    img=np.expand_dims(img,axis=0)
    predictions = model.predict(img)
    return predictions
