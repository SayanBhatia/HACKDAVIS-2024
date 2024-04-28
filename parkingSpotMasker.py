import cv2
import numpy as np

# Load the image


"""parking_spots = {
    6: np.array([[1953,505],[2241,543],[2395,299],[2081,234]]),
    13: np.array([[276,1102],[922,560],[1256,674],[420,1276]]),
    14: np.array([[420,1265],[1261,636],[1703,760],[745,1525]]),
    15: np.array([[1749,801],[2311,861],[1842,1724],[762,1696]]),
    16: np.array([[1787,1718],[2230,910],[2802,972],[2748,1707]])
}"""

parking_spots = {
    12: np.array([[848,812],[1238,942],[1598,931],[1163,683]]),
    9: np.array([[671,599],[876,746],[1112,739],[1003,595]])
}

def mask_parking_spot(image_path, output_path, spot_num):

    image = cv2.imread(image_path)

    points = parking_spots[spot_num]

    # Create a mask with the same dimensions as the image
    mask = np.zeros_like(image)

    # Fill the mask with the parallelogram
    cv2.fillPoly(mask, [points], (255, 255, 255))

    # Apply the mask to get the final image
    masked_image = cv2.bitwise_and(image, mask)

    # Show the masked image
    #cv2.imshow('Masked Image', masked_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Optionally, save the masked image

    from PIL import Image




    cv2.imwrite(output_path, masked_image)

    # Load the image
    image_path = output_path
    image = Image.open(image_path)

    # Convert the image to a numpy array
    image_np = np.array(image)

    # Find all non-black pixel indices
    non_black_pixels_mask = np.any(image_np != [0, 0, 0], axis=-1)

    # Find the bounding box of those pixels
    non_black_pixel_coords = np.argwhere(non_black_pixels_mask)
    y_min, x_min = non_black_pixel_coords.min(axis=0)
    y_max, x_max = non_black_pixel_coords.max(axis=0)

    # Use the bounding box to extract the non-black pixels area from the image
    cropped_image = image_np[y_min:y_max+1, x_min:x_max+1]

    # Save the cropped image
    cropped_image_path = output_path
    Image.fromarray(cropped_image).save(cropped_image_path)

    #cropped_image_path

mask_parking_spot("left_ref.jpg", "mask_left_reg.jpg", 9)
mask_parking_spot("left_use.jpg", "mask_left_use.jpg", 9)
#mask_parking_spot("no_cars.png", "no_ref.jpg", 14)

