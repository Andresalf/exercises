'''
Input:
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
Output:
1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
'''

def spiral_copy(matrix):
    result = []
    n = get_num_of_spirals(matrix)
    for i in range(n):
        result.extend(get_numbers_from_spiral(matrix, i))
    
    return result
    
def get_num_of_spirals(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    max_row_partitions = rows // 2 + rows % 2
    max_column_partitions = columns // 2 + columns % 2
    
    return min(max_row_partitions, max_column_partitions)
    

def get_numbers_from_spiral(matrix, offset):
    result = []
    rows = len(matrix)
    columns = len(matrix[0])
    
    # get upper row
    i = offset
    j = offset 
    while j <= columns - 1 - offset:
        result.append(matrix[i][j])
        j += 1
        
    # get right column
    i += 1
    j = columns - 1 - offset
    while i <= rows - 1 - offset:
        result.append(matrix[i][j])
        i += 1
        
    # get lower row
    i = rows - 1 - offset
    j -= 1
    while j >= offset:
        result.append(matrix[i][j])
        j -= 1
    
    # get left column
    i -= 1
    j = offset
    while i >= offset + 1:
        result.append(matrix[i][j])
        i -= 1
        
    return result
    

mat = [[1, 2, 3, 4, 5] \
        , [6, 7, 8, 9, 10] \
        , [11, 12, 13, 14, 15] \
        , [16, 17, 18, 19, 20]
        , [21, 22, 23, 24, 25]]
        
print(spiral_copy(mat))