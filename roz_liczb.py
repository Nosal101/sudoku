import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import pandas as pd
import cv2
from main import sudoku, description

# Przekształć listę obrazów do jednolitego rozmiaru
sudoku_resized = []
for img in sudoku:
    resized_img = cv2.resize(img, (28, 28))
    sudoku_resized.append(resized_img)

x_test = np.array(sudoku_resized)
# Przetwórz dane testowe tak, aby miały odpowiedni kształt (28x28x1)
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# Załaduj wytrenowany model
model = keras.models.load_model('model_do_cyfr.h5')

# Dokonaj predykcji na danych testowych
y_pred_test = model.predict(x_test)
y_pred_test = [np.argmax(i) for i in y_pred_test]

real_description = []
# Wyświtl zdjęcia wraz z predykcją
#for i in description:
#    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
#    plt.title(f"Predicted Label: {y_pred_test[i]}")
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    plt.show()
# Stwórz wektor wartosci pól
for i in range(81):
    for j in description:
        if i == j:
            real_description.append(y_pred_test[j])
    if i not in description:
        real_description.append(0)

# dostaje wektor gdzie 0 jest polem pustym a cyfry oznaczają predykcje numeru na danym polu
# Wszystko działa do tego momentu
