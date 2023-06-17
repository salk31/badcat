https://lydianlee.medium.com/building-a-cat-identification-system-with-raspberry-pi-tensorflow-a29232381152

https://www.tensorflow.org/tutorials/images/classification


tensorflow lite on pi...
train in cloud?

find /var/lib/motioneye/Camera1 -name 1?-??-??.jpg -delete

To get running on buster with motioneye 
NB motioneye broken on bullseye becuase of camera rewrite in bullseye
NB buster too old get working tensorflow so:
* download and build python3.9
* download and install mumpy "python3.9 -m pip install numpy-1.24.2.tar.gz"
* python3.9 -m pip install tflite-runtime

* install pigpiod and enable systemd service


// should be object detection? https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi

# 7.2v battery goes flat...
A - Switch to 5v pumps
CON - not got them and are they scary enough? A: Bought some and quite powerful

B - Use ATX power supply with 12 trickle charge
PRO - can power lamp
CON - overkill
CON - bulky

C - Use ATX power supply with 12 motor (or over drive)
PRO - can power lamp
CON - overkill?
CON - bulky

D - Switch that doesn't drain battery
CON - still battery will run down (have to recharge water anyway)
E - Step up converter to trickle charge