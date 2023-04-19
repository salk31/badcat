import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

import time


print("hello from core")

class Core:
  def __init__(self):
    model_file = 'model.tflite'
    num_threads = 1

    ext_delegate = None
    ext_delegate_options = {}

    self.interpreter = tflite.Interpreter(
        model_path=model_file,
        experimental_delegates=ext_delegate,
        num_threads=num_threads)
    self.interpreter.allocate_tensors()

    self.input_details = self.interpreter.get_input_details()
    self.output_details = self.interpreter.get_output_details()

    # check the type of the input tensor
    self.floating_model = self.input_details[0]['dtype'] == np.float32

    # NxHxWxC, H:1, W:2
    self.height = self.input_details[0]['shape'][1]
    self.width = self.input_details[0]['shape'][2]
  
  
  def process(self, image):
    img = Image.open(image).resize((self.width, self.height))

    # add N dim
    img_array = np.expand_dims(img, axis=0)

    if self.floating_model:
      img_array = np.float32(img_array)

  

    #self.interpreter.set_tensor(self.input_details[0]['index'], input_data)

    start_time = time.time()
    #self.interpreter.invoke()
    classify_lite = self.interpreter.get_signature_runner('serving_default')
    predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
    stop_time = time.time()

    #output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
    #results = np.squeeze(output_data)
    print(str(predictions_lite))

    top_k = results.argsort()[-5:][::-1]
    labels = ['badbw', 'clara']
    for i in top_k:
      if self.floating_model:
        print('{:08.6f}: {}'.format(float(results[i]), labels[i]))
      else:
        print('{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i]))

    print('time: {:.3f}ms'.format((stop_time - start_time) * 1000))