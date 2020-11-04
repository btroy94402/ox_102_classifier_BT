def main(*args):
	'''main function'''

	import tensorflow as tf
	import keras
	import json
	import numpy as np
	import PIL.Image as Image
	import utilsBT
	import argparse

	parser = argparse.ArgumentParser(description='My example explanation')

	parser.add_argument('test_image', type=str, help='path_and_file_of_test_image')
	parser.add_argument('model', type=str, help='*.h5 model name')
	parser.add_argument(
		'--topK',
		type=int,
		default=3,
		help='provide integer of top probs (default: 3)'
	)
	parser.add_argument(
		'--category_names',
		help='provide className.json filename'
	)

	args = parser.parse_args()

	image_path = args.test_image
	model = args.model
	top_k = args.topK
	if args.category_names:
		classFilePath = args.category_names
	else:
		classFilePath = 'noLabels'
		
	probs, labels = utilsBT.predict(image_path,model,top_k,classFilePath)

	print("The proabilities are of correct prediction are: ", probs)
	print("The corresponding predicted flower classes are: ", labels)

if __name__ == "__main__":
    import sys 
    main(*sys.argv)