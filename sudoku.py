import numpy as np

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    # turn the array into np.array
    puzzle  = np.array(puzzle)
    # numbers which can be in sudoku
    numbers = [1,2,3,4,5,6,7,8,9]
    columns = []
    squares = []
    # this cycle create te columns and suqares(block) our sudoku
    for i in range(len(puzzle)):
        columns.append(puzzle[:,i])
        block = puzzle[3*(i//3):3+3*(i//3), (i%3)*3:3+3*(i%3)]
        block.reshape(1, block.shape[0]*block.shape[1])
        squares.append(block)
    count_line = 0
    variation = []
    j = 0
    #this cycle fill the sudoku numbers
    while j < 100:
        count_line = 0
        for line in puzzle:
            count_columns = 0
            for element in line:
                if element == 0:
                    #this cycle goes over numbers and find all variation for zero position
                    for number in numbers:
                        if number not in columns[count_columns] and number not in squares[3*(count_line//3)+count_columns//3] and number not in line:
                            variation.append(number)
                    # if we have one variation replace the zero with this variation
                    if len(variation) == 1:
                        puzzle[count_line][count_columns] = variation[0]
                    variation = []
                count_columns +=1
            count_line+=1
        j+=1
        print(puzzle)
    return puzzle
