class SudokuSolver:
    @staticmethod
    def solve_sudoku(board):
        """
        Recursively solves the Sudoku puzzle using backtracking.

        :param board: The Sudoku puzzle board.
        :return: True if a solution is found, False otherwise.
        """
        empty_cell = SudokuSolver.find_empty_cell(board)

        # Base case: if no empty cell is found, puzzle is solved
        if not empty_cell:
            return True

        row, col = empty_cell

        # Try numbers 1 to 9 in the empty cell
        for num in range(1, 10):
            if SudokuSolver.is_valid_move(board, row, col, num):
                # Place the valid number and recursively solve the puzzle
                board[row][col] = num
                if SudokuSolver.solve_sudoku(board):
                    return True
                # Undo the move if no solution is found
                board[row][col] = 0

        # No valid number found for the current cell, backtrack
        return False

    @staticmethod
    def find_empty_cell(board):
        """
        Finds the first empty cell in the Sudoku board.

        :param board: The Sudoku puzzle board.
        :return: A tuple containing the row and column indices of the empty cell, or None if no empty cell is found.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    @staticmethod
    def is_valid_move(board, row, col, num):
        """
        Checks if placing a number in a given cell is a valid move.

        :param board: The Sudoku puzzle board.
        :param row: The row index of the cell.
        :param col: The column index of the cell.
        :param num: The number to be placed in the cell.
        :return: True if the move is valid, False otherwise.
        """
        # Check if num is already present in the row or column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check if num is already present in the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        # Return True if the move is valid
        return True

    @staticmethod
    def print_board(board):
        """
        Prints the Sudoku puzzle board.

        :param board: The Sudoku puzzle board.
        """
        for row in board:
            print(" ".join(str(num) for num in row))

def main():
    # Initialize the Sudoku puzzle board
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Solve the Sudoku puzzle
    if SudokuSolver.solve_sudoku(board):
        # Print solved puzzle if solution exists
        print("TASK 04")
        print("Sudoku puzzle solved successfully!")
        SudokuSolver.print_board(board)
    else:
        # Print message if no solution exists
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
