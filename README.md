# sudoku
This code let you solve easy sudoku

This code use the brute force method for "zero" positions ("zero" positions means that there is no digit in this position) and fills only those positions where there is only one variation

This code have disadvantages, cause if we have more than one variation then code not find the solution
for example this sudoku will be solve 
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
and this not.
puzzle = [[0,1,0,0,5,3,0,4,6],
          [5,0,4,0,6,8,3,0,7],
          [0,0,6,4,0,2,0,0,5],
          [0,0,5,6,4,1,0,0,0],
          [4,0,0,2,0,5,9,6,0],
          [0,6,0,0,9,7,4,5,0],
          [6,5,0,0,0,9,0,3,4],
          [0,3,0,5,2,4,6,0,9],
          [0,4,9,0,0,6,5,8,2]]
