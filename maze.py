grid = [[0,0,0],[0,1,0],[0,1,0]]


def search(x, y):
    if grid[x][y] == 2:
        print ('found at ',x, y)
        return True
    elif grid[x][y] == 1:
        print ('wall at ',x, y)
        return False
    elif grid[x][y] == 3:
        print ('visited at ',x, y)
        return False
 
    print ('visiting ',x, y)

    # mark as visited

    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False
search(0, 0)
