import cv2
import matplotlib.pyplot as plt
import numpy as np

# Wczytaj obraz w odcieniach szarości
img = cv2.imread('photo/sudoku1.png', 0)
desired_size = (400, 400)
img = cv2.resize(img, desired_size)
#Dokonaj Erozji
kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
#zmień na obraz binarny
_, thresh1 = cv2.threshold(erosion, 220, 255, cv2.THRESH_BINARY)
#Dokonaj Erozji
kernel2 = np.ones((2, 2), np.uint8)
erosion2 = cv2.erode(thresh1, kernel, iterations=1)
#znajdz kontury
contours, hierarchy = cv2.findContours(erosion2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Przygotuj obraz kolorowy, na którym narysujemy kontury na zielono
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# Iteruj przez kontury i sprawdź, czy są konturami nadrzędnymi
rectangle_contours=[]
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:  # Kontur nie ma konturu nadrzędnego (jest zewnętrzny)
        rectangle_contours.append(contours[i])
#narysuj kontury
cv2.drawContours(img_color, rectangle_contours,-1, (0, 255, 0), 3)
# Wyświetl obraz
cv2.imshow('Obraz z pokolorowanymi konturami', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

sudoku=[]
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:  # Kontur nie ma konturu nadrzędnego (jest zewnętrzny)
        # Znajdź prostokąt obejmujący kontur
        x, y, w, h = cv2.boundingRect(contours[i])
        # Wyciągnij fragment obrazu z prostokątem
        roi = img[y:y+h, x:x+w]
        sudoku.append(roi)
        #cv2.imshow("dupa",roi)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #print(roi.shape)


plt.imshow(sudoku[0])
plt.show()
#print(len(sudoku))


