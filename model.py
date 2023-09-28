import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Importuj dane
train_data = pd.read_csv("photo/train.csv")
test_data = pd.read_csv("photo/test.csv")

# Przygotuj dane treningowe i testowe
x = train_data.drop('label', axis=1).values
y = train_data['label'].values
data = [i.reshape(28, 28) for i in x]
X = np.array(data)

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
cnn.fit(x_train_scaled, y_train, batch_size=256, epochs=15, validation_data=(x_test_scaled, y_test))

# Zapisz wytrenowany model
cnn.save('moj_wytrenowany_model.h5')