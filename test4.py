import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

def detect_car(image_path):
    # Load and prepare image
    img = load_img(image_path, target_size=(224, 224))  # Resize image to 224x224 which is required by MobileNetV2
    img_array = img_to_array(img)  # Convert the image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    img_array = preprocess_input(img_array)  # Preprocess the image as required by MobileNetV2

    # Make predictions
    predictions = model.predict(img_array)
    # Decode predictions
    decoded_predictions = decode_predictions(predictions, top=10)[0]
    
    # Check for 'car' in predictions
    for entry in decoded_predictions:
        if 'car' in entry[1]:
            return True, entry[2]  # Return True and the probability

    return False, None  # No car found

# Example usage
image_path = 'masked_parallelogram.jpg'
has_car, probability = detect_car(image_path)
if has_car:
    print(f"Car detected with probability {probability}")
else:
    print("No car detected")
