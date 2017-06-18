'''
Date Created : 6/3/2017

Theme : TensorFlow - Practice #2 : matrix operations

Author : David Hsu

Date Modified : 6/3/2017
'''
import numpy as np
import tensorflow as tf

# matrices set up
A = tf.constant([[3,1,4],[1,5,9]]) # shape:(2,3)
B = tf.constant([[1],[2],[3]]) # shape:(3,1)
C = tf.matmul(A,B)  # shape is expected to be (2,1)

# execution set up
sess = tf.Session()
ans = sess.run(C)
print(ans)
sess.close()
