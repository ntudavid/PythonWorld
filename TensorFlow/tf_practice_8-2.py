'''
Date Created : 6/5/2017     

Theme : TensorFlow - Practice #8-2 : classification

Author : David Hsu

Date Modified : 6/5/2017
'''
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# add_layer function
def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('bias'):
            bias = tf.Variable(tf.zeros([1, out_size])+0.1, name='b')
        with tf.name_scope('scores'):
            scores = tf.matmul(inputs,Weights)+bias
        if activation_function is None:
            outputs = scores
        else:
            outputs = activation_function(scores)
        return outputs

def compute_accuracy(val_xs,val_ys):
    global results
    y_pre = sess.run(results, feed_dict={xs:val_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(val_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    return sess.run(accuracy, feed_dict={xs:val_xs,ys:val_ys})


# data set up
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
xs = tf.placeholder(tf.float32,[None,784]) # 28x28=784
ys = tf.placeholder(tf.float32,[None,10]) # 0~9

# neural network structure
results = add_layer(xs, 784, 10, activation_function = tf.nn.softmax)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(results),reduction_indices=[1]))
model = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# execution set up
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
for i in range(1001):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(model, feed_dict = {xs:batch_xs, ys:batch_ys})
    if(i%100==0):
        print(i/100+1)
        print(sess.run(cross_entropy, feed_dict={xs:batch_xs, ys:batch_ys}))
        print(sess.run(cross_entropy, feed_dict={xs:mnist.test.images, ys:mnist.test.labels}))
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
        print()
    





