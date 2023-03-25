#!/usr/bin/env python3

from tflite_runtime.interpreter import Interpreter

TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

interpreter = Interpreter(model_path=TF_MODEL_FILE_PATH)
print("got interpreter")

classify_lite = interpreter.get_signature_runner('serving_default')
print("got classify")

predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
score_lite = tf.nn.softmax(predictions_lite)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
)