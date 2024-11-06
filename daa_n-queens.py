def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            print_solution()
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    def print_solution():
        for r in range(n):
            row = ["Q" if board[r] == c else "." for c in range(n)]
            print(" ".join(row))
        print()

    board = [-1] * n
    backtrack(0, set(), set(), set())


# Example usage
n = int(input("Give n"))
solve_n_queens(n)
