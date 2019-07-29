"""
Grid and phrase
Max. Marks: 100
You are given an n*m grid which contains lower case English letters. How many times does the phrase "saba"
appear horizontally, vertically, and diagonally in the grid?

Input format

First line: Two integer n and m, where n denotes (1 <= n,m <= 100) the number of rows and m denotes the number of
columns in the grid
Next n lines: Each line must contain a string of length m which contains lower-case English letters only
Output format

Print the number of times the word “saba” appears in the grid.

SAMPLE INPUT
5 5
safer
amjad
babol
aaron
songs
SAMPLE OUTPUT
2
Explanation
The phrase "saba" must look one of thease shapes :

s
 	a
 	 	b
 	 	 	a


s	a	b	a





s
a
b
a


 	 	 	a
 	 	b
 	a
s

"""


def check_saba(n, m, grid):
    count = 0
    match = 'saba'
    for i_row, row in enumerate(grid):
        if match in row:
            count += 1
        if i_row < n - 3:   # check in column
            j = 0
            for j in range(m):
                temp = grid[i_row][j] + grid[i_row+1][j] + grid[i_row+2][j] + grid[i_row+3][j]
                print(temp)
                if temp == match:
                    count += 1
                if j < m-3:     # first diagonal
                    temp = grid[i_row][j] + grid[i_row + 1][j+1] + grid[i_row + 2][j+2] + grid[i_row + 3][j+3]
                    if temp == match:
                        count += 1
                if j > 2:       # Reverse Diagonal
                    temp = grid[i_row][j] + grid[i_row + 1][j-1] + grid[i_row + 2][j-2] + grid[i_row + 3][j-3]
                    if temp == match[::-1]:
                        count += 1
    return count


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    grid = []
    for i in range(n):
        grid.append(input().rstrip())
    print(check_saba(n, m, grid))