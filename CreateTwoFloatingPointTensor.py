import tensorflow as tf

#TensorFlow constant, it doesnot take input, and outputs value it stores internally.

# EX: Floating point tensors

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # implictly tf.float32

print(node1, node2)

# OUTPUT : Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)

# printed nodes
# these nodes will evaluate when they run in session

#Run the computation graph in a session

sess = tf.Session()
print(sess.run([node1, node2]))

#OUTPUT : [3.0, 4.0]

