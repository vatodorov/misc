# -*- coding: utf-8 -*-
"""
These are some experiments while
reading and learning about Tensorflow.

Code is based on tutorials from TensorFlow's website
https://www.tensorflow.org/get_started/
"""

import tensorflow as tf


############ 1. Some basic stuff
# Create nodes
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

# We need to run the nodes in a session in order to evaluate them and print
sess = tf.Session()
print(sess.run([node1, node2]))

# Add up the nodes
node3 = tf.add(node1, node2)
print(node3)
print(sess.run(node3))

print(sess.run(node1 + node2))


# Add parameters to the graph using a placeholder
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b # the + sign is instead of tf.add()

print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 89], b: [45, 56]}))


# Add another operation
add_multiply = adder_node * 12
print(sess.run(add_multiply, {a: 6, b: 7}))


############ 2. Create a model
#  Create a variable - this is a trainable object
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)
model = W * x + b

# Initialize the variables
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(model, {x: [1, 2, 3, 4]}))


y = tf.placeholder(tf.float32)
squared_deltas = tf.square(model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


# Go back and change the values of the input parameters
# This is manual backpropagation :)
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))


############ 3. MNIST tutorial























