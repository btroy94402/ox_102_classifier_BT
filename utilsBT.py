import PIL.Image as Image
import tensorflow as tf
import numpy as np
import keras
import json
import tensorflow_hub as hub 

def btTest():
    print("Hi BT")
	
def process_image(IMG_OBJ):
    '''takes a numpy array image object, casts values to float,
    normalizes to 256 GL, resizes x,y to 224 and returns
    the processed image object'''
    IMG_OBJ = tf.cast(IMG_OBJ, tf.float32)
    IMG_OBJ /= 255
    IMG_OBJ = tf.image.resize(IMG_OBJ, (224, 224))
    IMG_OBJ = IMG_OBJ.numpy()
    return IMG_OBJ
	
def predict(image_path, model, top_k, classFilePath):
	'''takes an image, a model, and then returns
	the top 𝐾 most likely class labels along with
	the probabilities'''
	
	model = tf.keras.models.load_model(model,custom_objects=\
		{'KerasLayer':hub.KerasLayer})
	
	im = Image.open(image_path)
	im = np.asarray(im)    
	im = process_image(im)
	myPred = model.predict(np.expand_dims(im,axis=0))
	s =np.copy(myPred)
	s = -np.sort(-s)
	probs = [s.take(i) for i in range(top_k)]
	classes = [np.argsort(-myPred)[0][i] for i in range(top_k)]

	if not classFilePath == 'noLabels':
		Dir= '.'
		with open(Dir + '\\' + classFilePath, 'r') as f:
			class_names = json.load(f)
		labels = [class_names[str(i+1)] for i in classes]
		return probs, labels
	
	else:
		return probs, classes