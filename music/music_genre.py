import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import Model
from sklearn.externals import joblib
import numpy as np
from keras.preprocessing import image
from keras import backend as K
import tensorflow as tf
import librosa
from .mel_spectogram import mel_spec
from django.http import HttpResponse
global graph
graph = tf.get_default_graph()

def genre(f):
    K.clear_session()
    model = joblib.load('music/finalized_CNNmodel.sav')
    print("Loading model. Please wait !!!")
    print(model.layers[0].input_shape)

    #preprocessing uploaded file to get mel-spectrogram image
    mel_spec(f)

    test_image=image.load_img(f'media/{f.file.name}.png', target_size=(256,256), color_mode='rgb')
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    result=model.predict(test_image)
    label = np.argmax(result)

    if(label == 0):
        print('Classical')
    elif(label == 1):
        print('Dohori')
    else:
        print('Pop')

    return result
