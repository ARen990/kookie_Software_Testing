def gridChallenge(grid):
    # Convert each row to a sorted list of characters
    orderedGrid = [sorted(row) for row in grid]
    
    # Check if each column is sorted
    for i in range(len(orderedGrid[0])):
        column = [row[i] for row in orderedGrid]
        if column != sorted(column):
            return 'NO'
    
    return 'YES'