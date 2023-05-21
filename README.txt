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
* python3.9 -m pip install opencv-python-headless==4.5.5.64

* python3.9 -m pip install pygame (after https://www.pygame.org/wiki/CompileUbuntu)
* install pigpiod and enable systemd service


// should be object detection? https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi