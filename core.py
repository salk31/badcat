import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
#import cv2

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
    self.input_details = self.interpreter.get_input_details()
    self.output_details = self.interpreter.get_output_details()
    self.height = self.input_details[0]['shape'][1]
    self.width = self.input_details[0]['shape'][2]

    self.float_input = (self.input_details[0]['dtype'] == np.float32)

    self.input_mean = 127.5
    self.input_std = 127.5
  
  
  def process(self, image):
    # Load image and resize to expected shape [1xHxWx3]
    # TODO was using opencv ... couldn't install so do simple way, but colour space wrong?
    img = Image.open(image).resize((self.width, self.height))

    # add N dim
    input_data = np.expand_dims(img, axis=0)



    # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
    if self.float_input:
      input_data = (np.float32(input_data) - self.input_mean) / self.input_std

    # Perform the actual detection by running the model with the image as input
    self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
    self.interpreter.invoke()

    # Retrieve detection results
    boxes = self.interpreter.get_tensor(self.output_details[1]['index'])[0] # Bounding box coordinates of detected objects
    classes = self.interpreter.get_tensor(self.output_details[3]['index'])[0] # Class index of detected objects
    scores = self.interpreter.get_tensor(self.output_details[0]['index'])[0] # Confidence of detected objects
    
    print(str(classes))
    print(str(scores))
    