'''
Date Created : 6/5/2017     

Theme : TensorFlow - Practice #9 : classification - 2 layers with dropout method

Author : David Hsu

Date Modified : 6/5/2017
'''
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# add_layer function
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
    bias = tf.Variable(tf.zeros([1, out_size])+0.1, name='b')
    scores = tf.matmul(inputs,Weights)+bias
    # dropout for regularization
    scores = tf.nn.dropout(scores, keep_prob)
    if activation_function is None:
        outputs = scores
    else:
        outputs = activation_function(scores)
    return outputs

def compute_accuracy(val_xs,val_ys,keep):
    global results
    global layer1
    y_tmp = sess.run(layer1, feed_dict={xs:val_xs, keep_prob:keep})
    y_pre = sess.run(results, feed_dict={layer1:y_tmp, keep_prob:keep})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(val_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    return sess.run(accuracy, feed_dict={xs:val_xs,ys:val_ys,keep_prob:keep})


# data set up
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
xs = tf.placeholder(tf.float32,[None,784]) # 28x28=784
ys = tf.placeholder(tf.float32,[None,10]) # 0~9
keep_prob = tf.placeholder(tf.float32)

# neural network structure
layer1 = add_layer(xs, 784, 10, activation_function = tf.nn.tanh) #activation_function = tf.nn.tanh is needed, or failed
results = add_layer(layer1, 10, 10, activation_function = tf.nn.softmax)
#results = add_layer(xs, 784, 10, activation_function = tf.nn.softmax)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(results),reduction_indices=[1]))
model = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# execution set up
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
for i in range(10001):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(model,feed_dict = {xs:batch_xs, ys:batch_ys, keep_prob:1})
    if(i%1000==0):
        print(compute_accuracy(mnist.test.images, mnist.test.labels,1))
        #print(compute_accuracy(batch_xs, batch_ys))
        #print(sess.run(cross_entropy, feed_dict={xs:batch_xs, ys:batch_ys, keep_prob:0.5}))
    

