# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking 
# for n-queens problem or a graph coloring problem.

def issafe(arr,x,y,n):
    for row in range(x):
        if arr[row][y] == 1:
            return False
        
    row = x
    col = y
  
    while row>=0 and col>=0:
        if arr[row][col]==1:
            return False
        row-=1
        col-=1

    row = x
    col = y
    
    while row>=0 and col<n:
        if arr[row][col]==1:
            return False
        row-=1
        col+=1

    return True

def nQueen(arr,x,n):
    if x>=n:
        return True

    for col in range(n):
        if issafe(arr,x,col,n):
            arr[x][col]=1
            if nQueen(arr,x+1,n):
                return True
            arr[x][col] = 0

    return False


n = int(input("Enter number of Queens : "))
arr = [[0]*n for i in range(n)]
if n>3:
    if nQueen(arr,0,n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j],end=" ")
            print()
else:
    print("Solving N-Queens problem with less than 4 queens is impossible")

# Explanation:
# This code solves the N-Queens problem using a recursive backtracking algorithm. The N-Queens problem 
# is a classic puzzle that involves placing N queens on an N×N chessboard in such a way that no two queens threaten each other.

# The `issafe` function checks whether it is safe to place a queen at position `(x, y)` on the chessboard 
# represented by the 2D array `arr`. It takes the current row (`x`), column (`y`), and the size of the chessboard (`n`) as input. 

# The function first checks for any queens in the same column above the current position (`arr[row][y]`). 
# If there is a queen present, it means the position is unsafe, and it returns `False`.

# Then, it checks for any queens on the diagonals. It uses two while loops to traverse diagonally upwards on 
# both sides of the current position. If it encounters a queen on any of the diagonals (`arr[row][col]`), 
# it returns `False` indicating that the position is unsafe.

# If the function completes the loop without finding any conflicting queens, it means the position is safe, 
# and it returns `True`.

# The `nQueen` function is the main recursive function that solves the N-Queens problem. It takes the 
# chessboard array `arr`, the current row `x`, and the size of the chessboard `n` as input.

# If the current row `x` becomes equal to `n`, it means all the queens have been placed successfully, 
# and it returns `True` to indicate a valid solution.

# The function iterates over each column (`col`) in the current row and checks if it is safe to place a 
# queen at that position using the `issafe` function. If it is safe, it marks that position as 1 (placing a queen) 
# in the `arr` array and recursively calls `nQueen` with the next row (`x+1`). If `nQueen` returns `True`, 
# it means a valid solution has been found, and the function returns `True`.

# If placing a queen in the current position leads to an invalid solution, the function backtracks by setting 
# the position back to 0 (removing the queen) in the `arr` array and continues to the next column.

# If none of the columns in the current row allow a valid solution, the function returns `False` to indicate 
# that there is no valid solution for the given configuration.

# In the main block, the user is prompted to enter the number of queens (`n`). If `n` is greater than 3, 
# it initializes an empty `arr` array of size `n×n` and calls the `nQueen` function with the `arr`, 
# starting row 0 (`x=0`), and `n`. If a valid solution is found, it prints the chessboard configuration. 
# Otherwise, if `n` is less than or equal to 3, it prints a message indicating that solving the N-Queens 
# problem with less than 4 queens is impossible.

# The output will be the valid configuration of queens on the chessboard, represented by 1's, or the 
# message indicating that a solution is impossible.