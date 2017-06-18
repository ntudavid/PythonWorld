'''
tutorial (2) - list

2016/06/14

David Hsu
'''

# empty list
L = []
print('L =>',L)
# append one (str) element 'david' : .append()
L.append('david')
print('L =>',L) # The list L contains 'david' now
L.append('johnny')
print('L =>',L)
# * means duplication for list
L2 = L*2
print('L2 =>',L2)
# access the element in the list
name = L[0] # the first element starts from index 0
print(name)
name2 = L2[3]
print(name2)
# length of the list ( the number of elements in the list): len(List) 
print('Length of L :',len(L))
print('Length of L2 :',len(L2))
# remove the specific element in the list : .remove()
L2.remove('johnny')
print('L2 after removing the element :', L2)
# pop the last element in the list : .pop()
nameLast = L2.pop()
print(nameLast)
print('L2 after .pop() :', L2)
# insert an element to specific index : .insert(index, element)
L.insert(1,'andy')
print('L after insertion :',L)
L.insert(-2,'michael') # - means reverse indext
print('L after insertion :',L)
L.insert(101,'john') # indext over length will be regard as .append()
print('L after insertion :',L)
L.insert(-101,'peter') # - means reverse indext
print('L after insertion :',L)
# sorting in list
L.sort()
print(L)
# adding different types of element to the list
L.append(3.141592)
L.insert(2,1234567)
print('L =', L)
# can not sort with unorderagble types of element
#L.sort()

# initialize a list 
nums = [0.0]*6
print('nums =', nums)
nums.append(2.453)
print('nums =', nums)
print('Length of nums is', len(nums))
# merge with another list : .extend(list)
nums.extend([3,1,4,1,5])
print('nums =', nums)
print('Length of nums is', len(nums))
print(type(nums[11]))
nums.append(-1.2345)
nums.sort()
print('List nums after sorting becomes',nums)
# extract sublist from the list
Lnums = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print('Length of Lnums is', len(Lnums))
print('Lnums =', Lnums)
subL = Lnums[6:10] # [ nums[6], nums[7], nums[8], nums[9]]
print('subL =', subL)
subL = Lnums[5:11:2] # index 5,7,9 (exclude 11)
print('subL =', subL)
subL = Lnums[11:5:-2] # index 11,9,7 (exclude 5)
print('subL =', subL)
# copy all element to another list
Lcopy = Lnums[:]
print('Lcopy =',Lcopy)
Lcopy = Lnums[::]
print('Lcopy =',Lcopy)
Lcopy = Lnums[::-1]
print('Lcopy =',Lcopy)



