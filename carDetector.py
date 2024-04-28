import cv2

# Load the cascade classifier
car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')

# Function to detect cars and display the number of detected cars
def detect_cars():
    frame = cv2.imread('masked_parallelogram.jpg')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Add text to the image showing the number of cars
    text = f"Number of cars detected: {len(cars)}"
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imwrite('detected_cars.jpg', frame)
    
    if len(cars) >= 1:
        return True
    else:
        return False

#print(detect_cars())