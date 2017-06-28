import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

add_and_triple = adder_node * 3

with tf.Session() as sess:
    print(sess.run(add_and_triple, {a:3, b:4.5}))