from parkingSpotMasker import mask_parking_spot
from fillParkingSpot import fill_parking_spots
from imageSimilarity import image_similarity
import numpy as np

"""
parking_spots = {
    6: np.array([[1953,505],[2241,543],[2395,299],[2081,234]]),
    13: np.array([[276,1102],[922,560],[1256,674],[420,1276]]),
    14: np.array([[420,1265],[1261,636],[1703,760],[745,1525]]),
    15: np.array([[1749,801],[2311,861],[1842,1724],[762,1696]]),
    16: np.array([[1787,1718],[2230,910],[2802,972],[2748,1707]])
}

"""
parking_spots = {
    12: np.array([[848,812],[1238,942],[1598,931],[1163,683]]),
}

taken_parking_spots = []
image_path = "med_cars.png"
for key in parking_spots:
    mask_parking_spot("no_cars.png", "no_ref.jpg", key)
    mask_parking_spot(image_path, "mask1.jpg", key)
    similarity = image_similarity("mask1.jpg", "no_ref.jpg")
    taken_parking_spots.append(similarity)
    #if detect_cars():
        #taken_parking_spots.append(key)
    #fill_parking_spot(key)

print(taken_parking_spots)
#fill_parking_spots(taken_parking_spots)


