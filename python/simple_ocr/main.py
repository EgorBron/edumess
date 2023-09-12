import cv2
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(data_folder):
    data = []
    labels = []

    for filename in os.listdir(data_folder):
        if filename.endswith('.png'):
            image = cv2.imread(os.path.join(data_folder, filename), cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (50, 100))
            data.append(image)
            label = filename.split('_')[0]
            labels.append(label)

    return data, labels

data_folder = './dataset/'
data, labels = load_and_preprocess_data(data_folder)

data = [image.flatten() for image in data]

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# print(x_test, y_test)

model = SVC(kernel='linear')
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print(f"acc: {accuracy * 100:.2f}%")

new_image = cv2.imread('recog.png', cv2.IMREAD_GRAYSCALE)
new_image = cv2.resize(new_image, (100, 50))
new_image = new_image.flatten()

prediction = model.predict([new_image])
print(f"predict: {prediction[0]}")
