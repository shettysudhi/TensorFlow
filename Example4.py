import tensorflow as tf

x = 2
y = 3

op1 = tf.add(x,y)
op2 = tf.multiply(x,y)

#here graph doesnt depend on op3,
# so session does not evaluate op3(useless)
op3 = tf.multiply(x, op1)

op4 = tf.pow(op2, op1)
with tf.Session() as sess:
    op5 = sess.run(op4)
    print("Result : {}".format(op5))

