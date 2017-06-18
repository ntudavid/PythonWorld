'''
Date Created : 6/3/2017

Theme : TensorFlow - Practice #4 : tf.Variable()

Author : David Hsu

Date Modified : 6/3/2017
'''
import numpy as np
import tensorflow as tf

# variables set up
var = tf.Variable(0, name = 'var1') # var1, initial 0
const_1 = tf.constant(1)

# structure set up
increasing_step = tf.add(var,const_1)
update = tf.assign(var, increasing_step)

# execution 
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print('initial value:',sess.run(var))
    for i in range(10):
        sess.run(update)
        print(i,sess.run(var))
