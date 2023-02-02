def searchMatrix(matrix, target):
    left = 0
    right = len(matrix) - 1

    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    while (left <= right):
        row = (left+right)//2
        print(row)
        if (matrix[row][-1] < target):
            left += 1
        elif (matrix[row][-1] > target):
            right -= 1
        else:
            break

    left = 0
    right = len(matrix[0])

    while (left <= right):
        mid = (left+right)//2

        if (matrix[row][mid] < target):
            left += 1
        elif (matrix[row][mid] > target):
            right -= 1
        elif (matrix[row][mid] == target):
            return True

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 11

print(searchMatrix(matrix, target))
