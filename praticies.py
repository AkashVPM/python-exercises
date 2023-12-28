# Given a Matrix, the task is to write a Python program that can sort its rows or columns
# on a measure of the number of values equal to its index number. For each row or column, 
# count occurrences of equality of index number with value. After computation of this count
# for each row or column, sort the matrix on basis of the count extracted for each row or column.

# Input : test_list = [[3, 1, 2, 5, 4], [0, 1, 2, 3, 4], [6, 5, 4, 3, 2], [0, 5, 4, 2]] 
# Output : [[6, 5, 4, 3, 2], [0, 5, 4, 2], [3, 1, 2, 5, 4], [0, 1, 2, 3, 4]

def sorted_list(row):
 
    return len([ele for idx, ele in enumerate(row) if ele == idx])

test_list = [[3, 1, 2, 5, 4], [0, 1, 2, 3, 4], [6, 5, 4, 3, 2], [0, 5, 4, 2]]
print(f"The input is {test_list}") 
test_list.sort(key=sorted_list)
print(f"The finial output is {test_list}")