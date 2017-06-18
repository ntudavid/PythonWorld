'''
Date Created : 6/3/2017

Theme : TensorFlow - Practice #1 - linear regression training

Author : David Hsu

Date Modified : 6/3/2017
'''
import numpy as np
import tensorflow as tf

# data set up
observations = np.random.rand(100).astype(np.float32)
labels = observations*0.1+0.3

# create the model
# initialize the parameters of hypothesis
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
bias = tf.Variable(tf.zeros([1]))
# predicting results
predictions = Weights*observations + bias
# loss function : mean squared error
loss_function = tf.reduce_mean(tf.square(labels-predictions))
# learning mehtod : Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(0.1) # learning rate = 1
model = optimizer.minimize(loss_function)

# execution set up
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)  # start executing
print('initial values:', sess.run(Weights), sess.run(bias))
for i in range(1000):
    sess.run(model)
    if(i%100==0):
        print(i, sess.run(Weights), sess.run(bias))


