from roz_liczb import real_description
import numpy as np

# Tworzenie wektora
vector = real_description
# Sprawdzenie, czy liczba elementów jest odpowiednia do utworzenia macierzy 9x9
if len(vector) != 81:
    raise ValueError("Wektor musi zawierać dokładnie 81 elementów.")

# Odwrócenie wektora
reversed_vector = vector[::-1]

# Przekształcenie wektora na macierz 9x9
matrix = np.array(reversed_vector).reshape(9, 9)


#print(matrix)

def check_col(num, row, matrix):
    left = 0
    center = 0
    right = 0
    if row % 3 == 0:
        for i in range(9):
            if matrix[i, row] == num:
                left = 1
            if matrix[i, row + 1] == num:
                center = 1
            if matrix[i, row + 2] == num:
                right = 1
    if row % 3 == 1:
        for i in range(9):
            if matrix[i, row - 1] == num:
                left = 1
            if matrix[i, row] == num:
                center = 1
            if matrix[i, row + 1] == num:
                right = 1
    if row % 3 == 2:
        for i in range(9):
            if matrix[i, row - 2] == num:
                left = 1
            if matrix[i, row - 1] == num:
                center = 1
            if matrix[i, row] == num:
                right = 1
    return (left,center,right)


def check_row(num, col, matrix):
    up = 0
    center = 0
    down = 0
    if col % 3 == 0:
        for i in range(9):
            if matrix[col,i] == num:
                up = 1
            if matrix[col+1,i] == num:
                center = 1
            if matrix[col+2,i] == num:
                down = 1
    if col % 3 == 1:
        for i in range(9):
            if matrix[col-1,i] == num:
                up = 1
            if matrix[col,i] == num:
                center = 1
            if matrix[col+1,i] == num:
                down = 1
    if col % 3 == 2:
        for i in range(9):
            if matrix[col-2,i] == num:
                up = 1
            if matrix[col-1,i] == num:
                center = 1
            if matrix[col,i] == num:
                down = 1
    return (up,center,down)


def check_square(num, row, col, matrix):
    # Oblicz indeksy początku kwadratu 3x3, do którego należy dane pole
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Sprawdź, czy liczba występuje w kwadracie 3x3
    for i in range(3):
        for j in range(3):
            if matrix[start_row + i, start_col + j] == num:
                return 1

def mark_numbers_in_square(matrix, row, col):
    # Skopiuj macierz, aby nie zmieniać oryginalnej
    marked_matrix = np.copy(matrix)

    # Oblicz indeksy początku odpowiedniego kwadratu 3x3, do którego należy dane pole
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Lista na wszystkie liczby w kwadracie
    numbers_in_square = []

    # Przeszukaj kwadrat 3x3
    for i in range(3):
        for j in range(3):
            num = matrix[start_row + i, start_col + j]
            numbers_in_square.append(num)
            if num != 0:
                marked_matrix[start_row + i, start_col + j] = -1

    return marked_matrix[start_row:start_row+3, start_col:start_col+3], numbers_in_square

def count_zeros(matrix):
    count = 0
    for row in matrix:
        for num in row:
            if num == 0:
                count += 1
    return count

for g in range(100):
    # Numeruj po rzędach i kolumnach
    for row in range(9):
        for col in range(9):
            #Sprawdz czy dane pole jest puste
            if matrix[row, col] == 0:
                for i in range(10):
                    # Sprawdz czy w danym kwadracie,rzędzie,kolumnie nie występuje dana liczba
                    if check_square(i, row, col, matrix) == None:
                        if check_col(i, col, matrix)[col % 3] == 0:
                            if check_row(i, row, matrix)[row % 3] == 0:
                                # Zaznacz pola gdzie występująliczby i wypisz te liczby
                                marked_matrix,numbers_in_square = mark_numbers_in_square(matrix, row, col)
                                # Zaznacz pole gdzie występuje dana liczba
                                for num in range(3):
                                    if check_col(i, col, matrix)[num] == 1:
                                        marked_matrix[:, num] = -1
                                    if check_row(i, row, matrix)[num] == 1:
                                        marked_matrix[num, :] = -1
                                # Jeżeli zostało tylko jedno pole puste wpisz tam liczbe i
                                if count_zeros(marked_matrix) == 1:
                                    if matrix[row, col] == 0:
                                        matrix[row, col] = i
                                # jeżeli w danym rzędzie i kolumnie występują juz pozostałe cyry wpisz ostatnią
                                if matrix[row, col] == 0:
                                    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    lost_number = []
                                    row_values = matrix[row, :]
                                    col_values = matrix[:, col]
                                    col_values = col_values.reshape(-1, 1)
                                    combined_matrix = np.concatenate((row_values.reshape(1, -1), col_values.T), axis=1)
                                    for number in numbers:
                                        if number not in combined_matrix:
                                            lost_number.append(number)
                                    if len(lost_number) == 1:
                                        matrix[row, col] = lost_number[0]
                                # jeżeli w danym rzędzie brakuje 2 cyfr i jedna z nich występuje w innym kwadracie wpisz pozostałą liczbe
                                    for number in numbers:
                                        if number not in row_values:
                                            lost_number.append(number)


print(matrix)
#marked_matrix,numbers_in_square = mark_numbers_in_square(matrix, 2, 7)
#row_values = matrix[2, :]
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#lost_number = []
#for number in numbers:
#    if number not in row_values:
#        lost_number.append(number)
# Znajdź pozycje zer
#zero_positions = np.where(row_values == 0)
#if np.any(zero_positions):
#    zero_positions = np.array(zero_positions)
#    marked_matrix1, numbers_in_square1 = mark_numbers_in_square(matrix, 2, zero_positions[0])
#
#print(numbers_in_square)
#print(row_values)
#print(lost_number)
#print(zero_positions)
#print(numbers_in_square1)