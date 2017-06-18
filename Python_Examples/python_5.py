'''
tutorial (5) - file I/O, csv file, numpy ndarray

2016/06/16

David Hsu
'''

import numpy as np

def csvReadTest(fileName):
    file = open(fileName)
    # read one line data 
    dataALine = file.readline()
    # tpye of file.readline()
    print('The type of dataALine is',type(dataALine))

    for item in dataALine:
        print(item)
    # read all lines
    dataAllLines = file.readlines()
    print('The type of dataAllLines is',type(dataAllLines))

    for item2 in dataAllLines:
        print(item2)

    # set cursor back the file's origin
    file.seek(0)
    dataALine = file.readline()
    # tpye of file.readline()
    print('The type of dataALine is',type(dataALine))
    aLine = dataALine.split(',')
    print('aLine type =', type(aLine))
    print('Length of aLine =', len(aLine))
    i=1
    for item in aLine:
        print(i,type(item),item,len(item))
        i += 1

    # .strip() function to truncate '\n'
    aLine2 = dataALine.strip().split(',')
    print('aLine2 type =', type(aLine))
    print('Length of aLine2 =', len(aLine))
    i=1
    for item in aLine2:
        print(i,type(item),item,len(item))
        i += 1
        
    # set cursor back the file's origin
    file.seek(0)
    dataAllLines = file.readlines()
    # tpye of file.readlines()
    print('dataAllLines type =', type(dataAllLines))
    # tpye of file.readline()
    print('dataALine type =', type(dataALine))
    # tpye of element in file.readline()
    print('Lines item type =', type(dataAllLines[0]))
    # number of elements in each line
    print('Length of each Line =', len(dataAllLines[0].strip().split(',')))
    # number of elements in file.readline()
    print('Length of Lines =', len(dataAllLines))
    m = len(dataAllLines)
    n = len(dataAllLines[0].strip().split(','))
    data = np.zeros((m,n))
    for i in range(m):
        aLine = dataAllLines[i].strip().split(',')
        for j in range(n):
            data[i,j] = float(aLine[j])
    file.close()

    return data

def csvWriteTest(fileName,dataArr):
    shape = dataArr.shape
    # tuple
    print('The type of shape is', type(shape))

    # use two variables to catch row and col information
    m, n = dataArr.shape
    print('row =', m,'shape[0] =',shape[0])
    print('col =', n,'shape[1] =',shape[1])
    print(dataArr)
    
    # file = open(fileName)
    # If the file does not exist, create one : w+
    file = open(fileName,'w+')
    for i in range(m):
        for j in range(n):
            file.write(str(dataArr[i,j]))
            print(dataArr[i,j],end='')
            if j < n-1:
                file.write(',')
                print(',',end='')
            else:
                file.write('\n')
                print('\n',end='')

    file.close()

    

    


            
        

