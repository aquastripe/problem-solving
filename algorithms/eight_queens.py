COUNT_QUEENS = 0


def check(row, col, rows, cols, diag_1, diag_2):
    if row in rows or col in cols or (row + col) in diag_1 or (row - col) in diag_2:
        return False

    return True


def eight_queens(coords, row, rows, cols, diag_1, diag_2):
    if len(coords) == 8:
        print(coords)
        global COUNT_QUEENS
        COUNT_QUEENS += 1
        return

    for col in range(8):
        if check(row, col, rows, cols, diag_1, diag_2):
            coords.append((row, col))
            rows.add(row)
            cols.add(col)
            diag_1.add(row + col)
            diag_2.add(row - col)

            eight_queens(coords, row + 1, rows, cols, diag_1, diag_2)

            coords.pop()
            rows.remove(row)
            cols.remove(col)
            diag_1.remove(row + col)
            diag_2.remove(row - col)


def main():
    coords = []
    rows = set()
    cols = set()
    diag_1 = set()
    diag_2 = set()
    eight_queens(coords, 0, rows, cols, diag_1, diag_2)
    print(COUNT_QUEENS)


if __name__ == '__main__':
    main()
