'''
tutorial (3) - range and for-loop, if condition, while-loop, no switch-case

2016/06/14

David Hsu
'''
# range(5) : 0,1,2,3,4 (exclude 5)
L = list(range(5))
print(L)

for i in range(5):
    print(L[i])

print()

for  item in L:
    print(item)

print()

L2 = list(range(2,8)) # 2,3,4,5,6,7 (exclude 8)
print('L2 =', L2)

L3 = list(range(2,8,2)) # 2,4,6 (exclude 8)
print('L3 =', L3)

L4 = list(range(8,2,-1)) # 8,7,6,5,4,3 (exclude 2)
print('L4 =', L4)

L5 = list(range(2,8,-1)) # nothing is valid
print('L5 =', L5)

'''
# float arguements are unacceptable for range function
for i in range(2,2.8,0.1):
    print(i)
'''

import numpy as np
# use arange function from numpy for float arguements
for i in np.arange(2,2.8,0.1):
    print(i)

nameRoster = ['David', 100, 'Johnny', 62, 'Frank', 78, 'Anna', 39 ]
# check the type of variable: isinstance(var,type)
for i in range(len(nameRoster)):
    if isinstance(nameRoster[i],str):
        print('The student is', nameRoster[i])

    if isinstance(nameRoster[i],int):
        if nameRoster[i]>90:
            print('The student got A')
        elif nameRoster[i]>80:
            print('The student got B')
        elif nameRoster[i]>70:
            print('The student got C')
        elif nameRoster[i]>60:
            print('The student got D')
        else:
            print('The student got failed')


print()

for item in nameRoster:
    if isinstance(item,str):
        print('The student is', item)

    if isinstance(item,int):
        if item>90:
            print('The student got A')
        elif item>80:
            print('The student got B')
        elif item>70:
            print('The student got C')
        elif item>60:
            print('The student got D')
        else:
            print('The student got failed')

print('\nwhile-loop test')
i=0
while i<len(nameRoster) :
    print(i)
    item = nameRoster[i]
    if isinstance(item, int):
        if item>90:
            print('A student got A')
        elif item>80:
            print('A student got B')
        elif item>70:
            print('A student got C')
        elif item>60:
            print('A student got D')
        else:
            print('A student got failed')

    i += 1 # i = i + 1

print('\nbreak test')
i=0
while True :
    print(i)
    if i>=len(nameRoster):
        break
    
    item = nameRoster[i]
    if isinstance(item, int):
        if item>90:
            print('A student got A')
        elif item>80:
            print('A student got B')
        elif item>70:
            print('A student got C')
        elif item>60:
            print('A student got D')
        else:
            print('A student got failed')

    i += 1

print('\ncontinue test')
i=0
while True :
    print(i)
    if i>=len(nameRoster):
        break
    
    item = nameRoster[i]
    i += 1 
    if isinstance(item, str):
        continue
    
    if item>90:
        print('A student got A')
    elif item>80:
        print('A student got B')
    elif item>70:
        print('A student got C')
    elif item>60:
        print('A student got D')
    else:
        print('A student got failed')
        
