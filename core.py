import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
import cv2

import time


print("hello from core")

class Core:
  def __init__(self):
    modelpath = 'custom_model_lite/detect.tflite'
    lblpath = 'custom_model_lite/labelmap.txt'

    with open(lblpath, 'r') as f:
      labels = [line.strip() for line in f.readlines()]

    # Load the Tensorflow Lite model into memory
    self.interpreter = tflite.Interpreter(model_path=modelpath)
    self.interpreter.allocate_tensors()

    # Get model details
    input_details = self.interpreter.get_input_details()
    output_details = self.interpreter.get_output_details()
    self.height = input_details[0]['shape'][1]
    self.width = input_details[0]['shape'][2]

    self.float_input = (input_details[0]['dtype'] == np.float32)

    input_mean = 127.5
    input_std = 127.5
  
  
  def process(self, image):
    # Load image and resize to expected shape [1xHxWx3]
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imH, imW, _ = image.shape 
    image_resized = cv2.resize(image_rgb, (self.width, self.height))
    input_data = np.expand_dims(image_resized, axis=0)

    # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
    if float_input:
      input_data = (np.float32(input_data) - input_mean) / input_std

    # Perform the actual detection by running the model with the image as input
    self.interpreter.set_tensor(input_details[0]['index'],input_data)
    self.interpreter.invoke()

    # Retrieve detection results
    boxes = self.interpreter.get_tensor(output_details[1]['index'])[0] # Bounding box coordinates of detected objects
    classes = self.interpreter.get_tensor(output_details[3]['index'])[0] # Class index of detected objects
    scores = self.interpreter.get_tensor(output_details[0]['index'])[0] # Confidence of detected objects
    
    print(str(classes))
    print(str(scores))
    