import tensorflow as tf

x = 2
y = 3

op1 = tf.add(x,y)
op2 = tf.multiply(x,y)

op3 = tf.multiply(x,op1)

op4 = tf.pow(op2, op1)
with tf.Session() as sess:
    res1, res2 = sess.run([op4, op3])
    print("Result is {} - {}".format(res1, res2))