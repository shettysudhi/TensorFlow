import tensorflow as tf

#TensorFlow operation arranged into graph of nodes(Operation, variable, constant) Each node takes
# 0 or more tensors as input and produces tensor as output.


#Data flow as Graph

#Assemble a graph where
#Node is operation, variable, constants
#Edges is tensor

#Tensor nothing but
# 0 Dimension Tensor : scalar
# 1 Dimension Tensor : vector
# 2 Dimension Tensor : matrix
# and so on....

# below graph look like
#       add ----> Operation (Node)
#       / \  -------> Edge(Tensor) carries 3 (scalar)
#      /   \
#     2     3 ------> Constant (Node)

a = tf.add(2,3)

#Use session to execute operation in the Graph
sess = tf.Session()

#Within session evaluate the graph
print(sess.run(a))

sess.close()