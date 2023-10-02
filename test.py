import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
import cv2
import os

# Ścieżki do folderów z zdjęciami
folder_paths = [
    'photo/Fnt/Sample0',
    'photo/Fnt/Sample1',
    'photo/Fnt/Sample2',
    'photo/Fnt/Sample3',
    'photo/Fnt/Sample4',
    'photo/Fnt/Sample5',
    'photo/Fnt/Sample6',
    'photo/Fnt/Sample7',
    'photo/Fnt/Sample8',
    'photo/Fnt/Sample9'
]

# Inicjalizacja listy na zdjęcia i etykiety
images = []
labels = []

# Przeglądanie folderów i wczytanie zdjęć
for folder_index, folder_path in enumerate(folder_paths):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            resized_img = cv2.resize(image, (28, 28))
            gray_image = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

            images.append(gray_image)
            labels.append(folder_index)

# Konwersja list na macierze numpy
X = np.array(images)
y = np.array(labels)

#Podzielenie na zbiór testowy i do trenowania
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Skalowanie danych
x_train_scaled = X_train / 255
x_test_scaled = X_test / 255


# Budowa modelu CNN
cnn = tf.keras.models.Sequential()
cnn.add(tf.keras.layers.Input(shape=(28, 28, 1)))
cnn.add(tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=256, kernel_size=(3, 3), activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=1200, activation='relu'))
cnn.add(tf.keras.layers.Dropout(0.2))
cnn.add(tf.keras.layers.BatchNormalization())
cnn.add(tf.keras.layers.Dense(units=600, activation='relu'))
cnn.add(tf.keras.layers.Dropout(0.1))
cnn.add(tf.keras.layers.BatchNormalization())
cnn.add(tf.keras.layers.Dense(units=300, activation='relu'))
cnn.add(tf.keras.layers.Dropout(0.05))
cnn.add(tf.keras.layers.BatchNormalization())
cnn.add(tf.keras.layers.Dense(10, activation='softmax'))

# Kompilacja modelu
cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
cnn.fit(x_train_scaled, y_train, batch_size=256, epochs=20, validation_data=(x_test_scaled, y_test))

# Zapisz wytrenowany model
cnn.save('model_do_cyfr.h5')