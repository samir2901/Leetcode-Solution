def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] < 0):
                count += 1
    return count

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(countNegatives([[3,2],[1,0]]))
print(countNegatives([[1,-1],[-1,-1]]))
print(countNegatives([[-1]]))
