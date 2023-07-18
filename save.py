import numpy as np

# Đường dẫn đến tệp CSV
csv_file = "path/to/output.csv"

import cv2
import numpy as np
from keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
import os
from pymilvus import connections, Collection
import csv

# Load pre-trained ResNet50 model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Function to extract features from a single frame
def extract_features(frame):
    # Preprocess the image
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0)
    frame = preprocess_input(frame)

    # Extract features using ResNet50 model
    features = model.predict(frame)
    return features.flatten()

# Path to the video directory
video_directory = "C:\\Users\\Raya\\Desktop\\ĐPT\\Car\\"

# List to store extracted features
features_list = []

# Process each video in the directory
for filename in os.listdir(video_directory):
    # Check if the file is a video file
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        # Construct the full path to the video file
        video_path = os.path.join(video_directory, filename)

        # Open the video file
        video = cv2.VideoCapture(video_path)

        # Read and process the first frame of the video
        ret, frame = video.read()

        # Extract features from the frame
        features = extract_features(frame)

        # Append features to the list
        features_list.append(features)

        # Release the video capture object
        video.release()

# Convert features_list to a NumPy array
features_array = np.array(features_list)

# Now you can use the features_array for further processing
print(features_array)

import csv

# Đường dẫn đến tệp CSV
csv_file = "C:/Users/Raya/Desktop/ĐPT/feature.csv"

# Ghi features_array và thông tin tương ứng vào tệp CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for filename, features in zip(os.listdir(video_directory), features_array):
        video_info = os.path.join(video_directory, filename)
        row = [video_info] + [str(feature) for feature in features]
        writer.writerow(row)
 
# fkajfjafafafsafasfaflajlfajgaghlrlhsnglk