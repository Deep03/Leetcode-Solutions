# Solution/Trick:
# Using Binary Search on a non decreasing array
# Trick:
# idx = no of column * which row idx is + which column idx is
# eg:
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     index 3(element = 4) = 3(no of column) * 1(what row is the idx) + 0(which column is the idx)
# rowthpostion = idx // column
# columnthpostion = idx % column
# elem = matrix[row][column]


def searchMatrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])
    left = 0
    right = rows * columns - 1
    pivot_index = 0
    current_element = 0
    while left <= right:
        pivot_index = (left + right ) // 2
        # // and % by columns is basically to ensure that all numbers can be read
        # doesnt matter, can use rows if columns == rows
        current_element = matrix[pivot_index // columns][pivot_index % columns]
        if current_element == target:
            return True
        
        else:
            if current_element > target:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
        
    return False





# test
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# side effect is True
print(searchMatrix(matrix, target))
