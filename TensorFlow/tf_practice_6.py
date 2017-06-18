'''
Date Created : 6/3/2017

Theme : TensorFlow - Practice #6 : neural networks and visualization

Author : David Hsu

Date Modified : 6/3/2017
'''
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# add_layer function
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    bias = tf.Variable(tf.zeros([1, out_size])+0.1)
    scores = tf.matmul(inputs,Weights)+bias
    if activation_function is None:
        outputs = scores
    else:
        outputs = activation_function(scores)
    return outputs

# data set up
x = np.linspace(-1,1,300)[:,np.newaxis]  # x.shape = (300,1)
xs = tf.placeholder(tf.float32,[None,1])
noise = np.random.normal(0, 0.1, x.shape)
y = np.square(x)+0.5+noise
ys = tf.placeholder(tf.float32,[None,1])

# neural network structure
layer1 = add_layer(xs, 1, 10, activation_function = tf.nn.relu)
results = add_layer(layer1, 10, 1, activation_function = None)
loss_function = tf.reduce_mean(tf.reduce_sum(tf.square(ys-results),reduction_indices=[1]))
model = tf.train.GradientDescentOptimizer(0.1).minimize(loss_function)

# visualization
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x,y)
plt.ion() # no block for plt.show()
plt.show()

# execution set up
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1001):
    sess.run(model, feed_dict = {xs:x, ys:y})
    if(i%100==0):
        print(sess.run(loss_function, feed_dict = {xs:x, ys:y}))
        # draw the hypothesis
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        predictions = sess.run(results, feed_dict = {xs:x})
        lines = ax.plot(x, predictions, 'r', lw=5)
        plt.pause(0.1)
    





