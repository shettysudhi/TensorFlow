#Graph can be parameterized to accept external input, known as place holder
#Placeholde to promise to provide value later

import tensorflow as tf

node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)

result = tf.add(node1, node2) # shortcut node1 + node2

print(node1) # Tensor("Placeholder:0", dtype=float32)
print(node2) # Tensor("Placeholder_1:0", dtype=float32)

print(result) # Tensor("Add:0", dtype=float32)

with tf.Session() as sess:
    print(sess.run(result, {node1:3, node2:4.5}))
    print(sess.run(result, {node1:[1,3], node2:[4,2]}))