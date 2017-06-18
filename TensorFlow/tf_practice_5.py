'''
Date Created : 6/3/2017

Theme : TensorFlow - Practice #5 : tf.placeholder(type)

Author : David Hsu

Date Modified : 6/3/2017
'''
import numpy as np
import tensorflow as tf

# placeholder set up
ph1 = tf.placeholder(tf.float32,[1,2])
#ph1 = tf.placeholder(tf.float32,[2,1])
ph2 = tf.placeholder(tf.float32,[2,1])

# structure set up
multiply = tf.multiply(ph1,ph2)  # multiplying correspondingly

# execution 
with tf.Session() as sess:
    # run and feed in values to the placeholders
    ans = sess.run(multiply,feed_dict={ph1:[[1,2]],ph2:[[3],[4]]})
    #ans = sess.run(multiply,feed_dict={ph1:[[1],[2]],ph2:[[3],[4]]})
    print(ans)
