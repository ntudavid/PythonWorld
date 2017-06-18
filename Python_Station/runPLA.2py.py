'''
   Perceptron Learning Algorithm

'''

import numpy as np
import matplotlib.pyplot as plt
import time

def runPLA(num): # num = number of sample points
    # target_function: f = [a,b,c] to represent the line: ax+by+c=0
    a,b,c = np.random.rand(3)*100-50
    f = [a,b,c]
    x = np.array([-55,55])
    y = eval('(-a*x-c)/b')
    fig = plt.plot(x,y,'c-')
    # samples [[x1,y1,1],[x2,y2,1],...]
    points = np.random.rand(num,2)*100-50
    offset = np.ones((num,1))
    points = np.hstack([points,offset])
    # classify the labels and plot
    Labels = np.ones(num)
    for i in range(num):
        check = np.dot(f, points[i,:])
        if(check<0):
            Labels[i] = -1
            fig = plt.plot(points[i,0], points[i,1], 'g^')
        else:
            fig = plt.plot(points[i,0], points[i,1], 'ro')
            
    # plot
    plt.axis([-55,55,-55,55])  # [Xmin,Xmax,Ymin,Ymax]
    plt.title('Sample points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.setp(fig, color = 'r', linewidth = 2.0)
    #plt.show()
    time.sleep(1)
    # PLA algorithm
    w = np.zeros(3)
    pointsT = points.transpose()
    num = points.shape[0]
    x = np.array([-55,55])
    cnt = 0
    while(True):
        misClassify = []
        scores = np.dot(w, pointsT)
        for i in range(num):
            if(scores[i]>=0 and Labels[i]==-1):
                misClassify.append(i)
            if(scores[i]<0 and Labels[i]==1):
                misClassify.append(i)
        n = len(misClassify)
        if(n==0):
            break
        #pick = misClassify[np.random.randint(n)]
        pick = misClassify[0]
        vect = points[pick,:]
        # draw the misPoint
        fig = plt.plot(vect[0], vect[1], 'bs')
        # draw w
        a, b, c = w
        y = eval('(-a*x-c)/b')
        fig = plt.plot(x,y,'b-')
        time.sleep(0.5)
        # update w
        w = w + Labels[pick]*vect
        cnt = cnt + 1

    print('Iterations', cnt, 'times')
    plt.show()


runPLA(80)

    
    
            
