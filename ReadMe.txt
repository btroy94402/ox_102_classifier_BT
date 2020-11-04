Oxford 102 Flower Dataset Deep Learning Classifier Model Project
Created by: Brian Troy 
Date: Nov 3, 2020

ox_102_classifier_BT Folder Contents:

	test_images directory (with 4 images)
	assets directory (rns with Jupyter notebook)
	image_classifier_1604289582.h5
	label_map.json
	predict.py
	utils.py
	Project_Image_Classifier_BT.html
	Project_Image_Classifier_BT.ipynb
	ReadMe.txt


Built with:

	Python (3.8.3)
	Jupyter (7.10.2)

Prerequisites:

	time
	json (2.0.9)
	pandas (1.1.1)
	numpy (1.18.5)
	matplotlib (3.1.1)
	tensorflow (2.3.1)
	tensorflow_datasets (4.0.1+nightly)
	tensorflow_hub (0.9.0)
	keras (2.4.0)
	PIL (7.1.2)

Usage:

	This project is for completion of the 'Udacity Intro to Machine Learning with Tensorflow' Nanodegree Deep Learning Section.
	The project uses Tensorflow/Keras and builds a transfer learning model used for inference on a dataset of 102 varieties of flower types.
	The dataset is the Oxford 102 dataset: 
		https://www.tensorflow.org/datasets/catalog/oxford_flowers102

	The completed project exists as .py scripts (predict.py and utils.py), Jupyter Notebook Version, or and an HTML version of the completed Jupyter Notebook version.
	The HTML file can be used for learning and/or help working around issues in similar deep/transfer learning projects.
	
	The predict.py script can be used with individual images from the Oxford 102 Flower dataset to predict
	flower types and associated label.

	To use predict.py, the following files must also be present in the same directory:
		utils.py #(supporting functions)
		label_map.json #(Look up table translates class codes to flower labels)
		image_classifier_model.h5 #(saved classifier model)

	The command line arguments used with predict.py are:
		1) test image path and name (required)
		2) model name (required)
		3) --topK (the number of topK probabilities for flower type predicted (optional, default is 3))
		4) --category_names (the Look Up Table (.json) that maps flower classes to flower type (optional))

Example Usage:

	C:\...\ox102classifier> python predict.py .\test_images\wild_pansy.jpg image_classifier_1604289582.h5 --topK 5 --category_names label_map.json