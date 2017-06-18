'''
Date Created : 6/5/2017     

Theme : TensorFlow - Practice #10 : CNN

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
    y_pre = sess.run(results, feed_dict={xs:val_xs, keep_prob:keep})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(val_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    return sess.run(accuracy, feed_dict={xs:val_xs,ys:val_ys,keep_prob:keep})

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME') # strides=[1,sx,sy,1]

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


# data set up
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
xs = tf.placeholder(tf.float32,[None,784]) # 28x28=784
ys = tf.placeholder(tf.float32,[None,10]) # 0~9
keep_prob = tf.placeholder(tf.float32)
imgData = tf.reshape(xs,[-1,28,28,1])
#print(imgData.shape) # (n_samples,28,28)

# neural network structure
# conv1
W_conv1 = weight_variable([5,5,1,32]) #patch:5x5, 1->32
b_conv1 = bias_variable([32])
conv1 = tf.nn.relu(conv2d(imgData,W_conv1)+b_conv1) # -->28x28x32
pool1 = max_pool_2x2(conv1) # -->14x14x32?
# conv2
W_conv2 = weight_variable([5,5,32,64]) #patch:5x5, 32->64
b_conv2 = bias_variable([64])
conv2 = tf.nn.relu(conv2d(pool1,W_conv2)+b_conv2) # -->14x14x64
pool2 = max_pool_2x2(conv2) # -->7x7x64
# fc1 fully connect layer
W_fc1 = weight_variable([7*7*64,1024])
b_fc1 = bias_variable([1024])
in_fc1 = tf.reshape(pool2,[-1,7*7*64]) # (n_samples,7,7,64) -> (n_samples,7*7*64)
fc1 = tf.nn.relu(tf.matmul(in_fc1,W_fc1)+b_fc1)
fc1_drop = tf.nn.dropout(fc1,keep_prob)
# fc2 fully connect layer
W_fc2 = weight_variable([1024,10])
b_fc2 = bias_variable([10])
results = tf.nn.softmax(tf.matmul(fc1_drop,W_fc2)+b_fc2)
# loss-function set up
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(results),reduction_indices=[1]))
model = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

# execution set up
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print('dropout=',0.4)
for i in range(20001):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(model,feed_dict = {xs:batch_xs, ys:batch_ys, keep_prob:0.4})
    if(i%1000==0):
        print(compute_accuracy(mnist.test.images, mnist.test.labels,0.4))
        #print(compute_accuracy(batch_xs, batch_ys))
        #print(sess.run(cross_entropy, feed_dict={xs:batch_xs, ys:batch_ys, keep_prob:0.5}))
    

