https://lydianlee.medium.com/building-a-cat-identification-system-with-raspberry-pi-tensorflow-a29232381152

https://www.tensorflow.org/tutorials/images/classification


tensorflow lite on pi...
train in cloud?



To get running on buster with motioneye 
NB motioneye broken on bullseye becuase of camera rewrite in bullseye
NB buster too old get working tensorflow so:
* download and build python3.9
* download and install mumpy "python3.9 -m pip install numpy-1.24.2.tar.gz"
* python3.9 -m pip install tflite-runtime


// numbers match?
from pi against Red_sunflower
2.481455: badbw
-4.073643: clara
same image in jupyter
[[-35.796406  50.721348]]


// should be object detection? https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi