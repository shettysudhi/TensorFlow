#Variables allow us to add trainable parameters to a graph. They are constructed with a type and initial value

import tensorflow as tf

W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

x = tf.placeholder(tf.float32)

lenear_model = W * x + b

#variables are not initialized when you call tf.Variable
#Constants are initialized when you call tf.constant, and their value can never change

#initialize all the variables in a TensorFlow program, you must explicitly call a special operat
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(lenear_model, {x:[1,2,3,4]}))
sess.close()