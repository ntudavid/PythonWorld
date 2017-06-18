'''
   mazeSolver
   maze: row by col
   
'''

def mazeSolve(maze, direction, i, j):
    if(i==row-1 and j==col-1):
        maze[i][j]=direction
        return True
    else:
        if(maze[i][j]=='0'):
            maze[i][j]=direction
            if(j+1<=col-1): # check right >>>
                if(mazeSolve(maze, '>', i, j+1)):
                    return True
            if(i+1<=row-1): # check down VVV
                if(mazeSolve(maze, 'V', i+1, j)):
                    return True
            if(j-1>=0): # check left  <<<
                if(mazeSolve(maze, '<', i, j-1)):
                    return True
            if(i-1>=0): # check up ^^^
                if(mazeSolve(maze, '^', i-1, j)):
                    return True
            # try all directions but fail
            maze[i][j]='-'
            return False
        else:
            return False

# main()
row = 6
col = 6
maze = [['0', '0', '1', '0', '0', '1'],
        ['0', '1', '0', '0', '0', '1'],
        ['0', '0', '0', '1', '0', '0'],
        ['1', '0', '0', '0', '0', '1'],
        ['0', '0', '0', '1', '1', '0'],
        ['1', '1', '0', '0', '0', '0']]
print(maze)

if(mazeSolve(maze, '@', 0, 0)):
    print(maze)
else:
    print('No Way Out')
