import tensorflow as tf

print("TensorFlow version:", tf.__version__)
hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy().decode())
