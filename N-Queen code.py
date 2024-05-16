def valid(r, c, queens):
    if not queens:  # If there are no queens placed yet, it is always valid
        return True
    for i in queens:
        # Check if the new queen conflicts with any existing queen
        if i[0] == r or i[1] == c or i[0] - i[1] == r - c or i[0] + i[1] == r + c:
            return False
    return True

def solve(r, queens):
    global res
    n = len(queens)
    if n == N:
        res.append(queens[:])  # Using queens[:] to create a copy of the queens list
        return

    for j in range(N):
        if valid(r, j, queens):
            queens.append((r, j))
            solve(r + 1, queens)
            queens.pop()

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard: "))  # Prompting the user for input
    res = []

    solve(0, [])  # Solve the N-Queens problem starting from the first row and an empty queens list

    print("Number of solutions:", len(res))  # Print the number of solutions
   
    for solution in res:
        # Create a grid of size N*N and initialize all cells with '.'
        grid = [['.' for _ in range(N)] for _ in range(N)]

        # Place queens on the grid based on the current solution
        for i, j in solution:
            grid[i][j] = 'Q'

        # Print the grid
        for row in grid:
            print(' '.join(row))
        print()
