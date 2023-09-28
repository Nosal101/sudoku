import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import pandas as pd

# Załaduj wytrenowany model
model = keras.models.load_model('moj_wytrenowany_model.h5')

# Przykład wczytywania danych testowych
test_data = pd.read_csv("photo/test.csv")
x_test = test_data.values  # Wczytaj dane testowe

# Przetwórz dane testowe tak, aby miały odpowiedni kształt (28x28x1)
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# Dokonaj predykcji na danych testowych
y_pred_test = model.predict(x_test)
y_pred_test = [np.argmax(i) for i in y_pred_test]

# Wyświetl przykładowe wyniki
#plt.figure(figsize=(9, 12))
#for i in range(12):
#    plt.subplot(4, 3, i + 1)
#    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
#    plt.title(f"Predicted Label: {y_pred_test[i]}")
#    plt.axis("off")
#plt.show()

plt.imshow(x_test[21].reshape(28, 28), cmap='gray')
plt.title(f"Predicted Label: {y_pred_test[21]}")
plt.show()