import serial
import base64
import time
import re  # Import the regular expression module

# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase initialization
# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'\Users\bythe\Desktop\hackdavis\Python\howimetyourmotherboard-328fb-firebase-adminsdk-lhdr0-fd9eb2c8cc.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://howimetyourmotherboard-328fb-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('server/saving-data/fireblog')
print(ref.get())
users_ref = ref.child('imagedata')

# Serial port configuration
serial_port = 'COM3'  # Change this to match your serial port
baud_rate = 115200

# Open serial port
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Read data from serial
        line = ser.readline().decode().strip()
        
        # Check if line is the start marker
        if line == "<START_IMAGE>":
            image_data = ""
            # Read lines until the end marker is found
            while True:
                line = ser.readline().decode().strip()
                if line == "<END_IMAGE>":
                    break
                else:
                    image_data += line
            
            # Save the base64-encoded image data
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"image_{timestamp}.txt"
            filenamedecoded = f"image_{timestamp}.jpg"

            # Decoded base64 image that will be stored locally
            image_bytes = base64.b64decode(image_data)
            
            with open(filename, "w") as f:
                f.write(image_data)
                print(f"Base64-encoded image data saved as {filename}")

            with open(filenamedecoded, "wb") as f:
                f.write(image_bytes)
                print(f"Decoded Base64 image data saved as {filenamedecoded}")

            # Sanitize the filename using regular expression
            sanitized_filename = re.sub(r'[^\w\-]', '_', filename)

            users_ref.set({
                f'image_{sanitized_filename}': {  # Use sanitized filename as the key
                    'base_64encoded': image_data,  # No need for curly braces for variable values
                },
            })

finally:
    # Close serial port
    ser.close()
