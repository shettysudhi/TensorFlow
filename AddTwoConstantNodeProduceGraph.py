import tensorflow as tf

## Add two constant node produce new graph

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

node3 = tf.add(node1, node2)

print(node3) #OUTPUT : Tensor("Add:0", shape=(), dtype=float32)
print(type(node3)) #OUTPUT : <class 'tensorflow.python.framework.ops.Tensor'>
with tf.Session() as sess:
    result = sess.run(node3)
    print(result) #OUTPUT : 7.0
    print(type(result)) #OUTPUT : <class 'numpy.float32'>
    writer = tf.summary.FileWriter("C:\PYCHARM\TMP")
    writer.add_graph(sess.graph)

#Graph here produce always constant output as it takes always constant as input
#Next we can see for plceholder

