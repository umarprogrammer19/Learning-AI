import numpy as np

# 9x9 Sudoku board
s = np.array(
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
)

# Valid set for Sudoku (numbers must be exactly 1 to 9)
VALID = set(range(1, 10))


def is_valid_sudoku(board):
    # Check each row
    for row in board:
        # Convert row to set and compare with VALID
        # Ensures:
        # - No duplicates
        # - All numbers from 1 to 9 are present
        if set(row) != VALID:
            return False

    # Check each column
    for column in board.T:
        # board.T gives transpose → columns become rows
        if set(column) != VALID:
            return False

    # Check each 3x3 sub-grid
    for i in range(0, 9, 3):  # row start indices: 0, 3, 6
        for j in range(0, 9, 3):  # column start indices: 0, 3, 6

            # Extract 3x3 box
            subgrid = board[i : i + 3, j : j + 3]

            # Flatten converts 2D → 1D for easy set comparison
            if set(subgrid.flatten()) != VALID:
                return False

    # If all checks pass, Sudoku is valid
    return True


print(is_valid_sudoku(s))
