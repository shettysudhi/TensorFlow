import tensorflow as tf

a = tf.add(2,3)

#Session object encapsulates the environment in which Operation objects are executed
# and Tensor object are evaluated

#with clause takes care of sess.close()
with tf.Session() as sess:
    print(sess.run(a))