'''
tutorial (1) - basic functions: elapsed time, print, input, eval, round

2016/06/13

David Hsu
'''

import time
# tic
tic = time.time()

help(time.time)

# get input -> inputData
# use help function to get detailed information of specific BIF
help(input)
inputData = input('Please enter something : ')
# the type of input we got is 'Str'
help(print)
print(type(inputData))
# show the inputData we obtained
print(inputData)
print('* means copy for String :', inputData*2)

# get number input using eval function
number = eval(input('Please enter a number : '))
# the type of input we got became 'Double' if it's valid
print(type(number))
print(number)
print('* means multipling for numbers :', number*2)

# get integer number input using convertion to 'int'
numberInt = int(input('Please enter a integer : '))
# the type of input we got became 'Double' if it's valid
print(type(numberInt))
print(numberInt)
print('* means multipling for numbers :', numberInt*2)

# get integer number input using convertion to 'float'
numberFract = float(input('Please enter a number : '))
# the type of input we got became 'Double' if it's valid
print(type(numberFract))
print(numberFract)
print('* means multipling for numbers :', numberFract*2)

# toc
toc = time.time()
interval = toc - tic
print(type(interval))
# round function to third decimal
elapsedTime = round(interval, 3)
# show elapsed time
print('Elapsed Time = ', elapsedTime, 'sec')


