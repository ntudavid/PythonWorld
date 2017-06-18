try:
    f = open('test.txt','r+')
except Exception:
    print('File can not be found. Create one!')
    f = open('test.txt','w')

f.write('This is a test.')
f.close()
