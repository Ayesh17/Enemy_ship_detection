import os
import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense
import sklearn.model_selection
from sklearn.metrics import confusion_matrix, accuracy_score

# Folder structure
train_data_dir = 'train_data'
test_data_dir = 'test_data'

# Iterate over all CSV files in the train_data directory
csv_files = [f for f in os.listdir(train_data_dir) if f.endswith('.csv')]

def load_dataset():
    behavior_classes = ['BENIGN', 'RAM', 'BLOCK', 'HERD', 'CROSS', 'HEADON', 'OVERTAKE', 'STATIONARY']

    # Make predictions on all test files
    for behavior_class in behavior_classes:
        train_dir = os.path.join(train_data_dir, behavior_class)
        csv_files = [f for f in os.listdir(train_dir) if f.endswith('.csv')]
        for csv_file in csv_files:
            # Read the CSV files and concatenate them into a single DataFrame
            data = pd.concat([pd.read_csv(os.path.join(train_dir, f)) for f in csv_files])
    print("data", data)
    return data

def train_test_split(data, test_size=0.2):
  """Splits the dataset into train and test sets."""
  X = data.iloc[:, :-1]
  y = data.iloc[:, -1]
  X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=test_size)
  return X_train, X_test, y_train, y_test

def design_model(num_features):
    timesteps = 1
    model = Sequential()
    model.add(LSTM(32, input_shape=(timesteps, num_features)))
    model.add(Dense(8, activation='softmax'))
    return model

def test(X_test, y_test):
    predictions = model.predict(X_test)
    # print("predictions", predictions)

    # Calculate accuracy and confusion matrix
    true_labels = y_test
    print("true_len", len(true_labels))
    print("actual",true_labels)

    y_pred = np.argmax(predictions, axis=1)
    print("y_pred_len", len(y_pred))
    print("y_pred", y_pred)
    print()
    cm = confusion_matrix(true_labels, y_pred)
    print("Confusion", cm)
    acc = accuracy_score(true_labels, y_pred)
    print(acc)
    return 0


data = load_dataset()

# Split the dataset into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(data)

# Print the shapes of the train and test sets.
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)


# Convert the DataFrames to NumPy arrays.
X_train = X_train.to_numpy()
X_test = X_test.to_numpy()

# Reshape the arrays.
num_samples, num_features = X_train.shape
X_train = X_train.reshape(num_samples, 1, num_features)

num_samples, num_features = X_test.shape
X_test = X_test.reshape(num_samples, 1, num_features)

print("Shape_X_test",len(X_test))

# One-hot encode the target variable
y_one_hot = keras.utils.to_categorical(y_train, num_classes=8)


model = design_model(num_features)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_one_hot, epochs=1, batch_size=16)

acc = test(X_test, y_test)
