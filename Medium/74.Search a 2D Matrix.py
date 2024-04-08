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



# Solution:
# The solution is to use Binary Search, the same way one would do it on 1-D array

# Trick:
# A 2-d array can be represented into a 1-D array.
# Index of a element = no. of total columns in matrix * row postion of the element + column position of the element

# Example:
#     matrix = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]
# element 4 is on column 0(counting starts from 0), and row 1. There are 3 total columns(nC)
#  Let column postion be Cp, and row position be Rp
# So the index of element 4 = nC * Rp + Cp
# index 3(element = 4) = 3 * 1 + 0 = 3
# matrix(if viewed as 1-d array), 4 = matrix[3]
# To access a 2-D matrix, we can do the following:
# We need the row postion and column postion of an element to access it. 
# rowthpostion = idx // column
# columnthpostion = idx % column
# elem = matrix[row][column]



# test
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# side effect is True
print(searchMatrix(matrix, target))
