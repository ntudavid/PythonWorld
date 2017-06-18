import numpy as np

observations = np.array([[10,12,9],[5,10,4]])
# 2 cases, 3 features

layer1 = {'node_0': np.array([1,-1,2]),
          'node_1': np.array([-2,1,-3])}
output = {'node_0': np.array([2,-1]),
          'node_1': np.array([-2,3])}

input_data = observations[1,:]
layer_1_node_0 = np.dot(input_data,layer1['node_0'])
layer_1_node_1 = np.dot(input_data,layer1['node_1'])
layer_1_values = np.array([layer_1_node_0,layer_1_node_1])
print(layer_1_values)
print(np.tanh(layer_1_values))
output_node_0 = np.dot(layer_1_values, output['node_0'])
output_node_1 = np.dot(layer_1_values, output['node_1'])
results = np.array([output_node_0, output_node_1])
print(results)
print(np.tanh(results))
