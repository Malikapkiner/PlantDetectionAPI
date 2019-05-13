# @Author: utkuglsvn <glsvn>
# @Date:   2019-05-12T13:56:37+03:00
# @Last modified by:   glsvn
# @Last modified time: 2019-05-14T00:44:26+03:00
import pyrebase


firebaseConfig = {
 "apiKey": "AIzaSyCpEUkG37S8e5u5DjbC6zCGYy4B5NMaAhI",
  "authDomain": "plantdetectionandroidfirebase.firebaseapp.com",
  "databaseURL": "https://plantdetectionandroidfirebase.firebaseio.com",
  "projectId": "plantdetectionandroidfirebase",
  "storageBucket": "plantdetectionandroidfirebase.appspot.com",
  "messagingSenderId": "23484350177",
  "appId": "1:23484350177:web:6d6662eacbb21f4e"
};


firebase=pyrebase.initialize_app(firebaseConfig)
storage=firebase.storage()

storage.child("images/plantImg").download("downloaded.jpg")

db=firebase.database().child("results")

import numpy as np
from keras.preprocessing import image
from skimage.io import imread
from skimage.transform import resize
from keras.models import load_model
classifier = load_model('model/leaf_model_last.h5')

img = imread('downloaded.jpg')
img = resize(img,(128,128))
img = np.expand_dims(img,axis=0)
if(np.max(img)>1):
    img = img/255.0
prediction = classifier.predict_classes(img)
print (prediction)
if(prediction):
    db.set("saglikli")
    print ("Saglikli")
else:
    db.set("hasta")
    print ("Hasta")
