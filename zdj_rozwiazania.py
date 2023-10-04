import matplotlib.pyplot as plt
from rozwiazanie_sudoku import matrix
import cv2
import numpy as np


folder_paths = [
    'photo/Fnt/Sample0/img001-00005.png',
    'photo/Fnt/Sample1/img002-00005.png',
    'photo/Fnt/Sample2/img003-00005.png',
    'photo/Fnt/Sample3/img004-00005.png',
    'photo/Fnt/Sample4/img005-00005.png',
    'photo/Fnt/Sample5/img006-00005.png',
    'photo/Fnt/Sample6/img007-00005.png',
    'photo/Fnt/Sample7/img008-00005.png',
    'photo/Fnt/Sample8/img009-00005.png',
    'photo/Fnt/Sample9/img010-00005.png'
]
sudoku_resized=[]
for i in range(len(folder_paths)):
    img = cv2.imread(folder_paths[i], 0)
    resized_img = cv2.resize(img, (28, 28))
    sudoku_resized.append(resized_img)

height, width = sudoku_resized[0].shape

big_image = np.zeros((9*height, 9*width), dtype=np.uint8)
for i in range(9):
    for j in range(9):
        y_start = i * width
        y_end = (i + 1) * width
        x_start = j * height
        x_end = (j + 1) * height
        number=matrix[i,j]
        big_image[y_start:y_end, x_start:x_end] = sudoku_resized[number]
cv2.imshow('Rozwiązane sudoku', big_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
