from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def image_similarity(image_path1, image_path2):
    # Open and convert images to grayscale
    img1 = Image.open(image_path1).convert('L')
    img2 = Image.open(image_path2).convert('L')

    # Convert images to numpy arrays
    img1_arr = np.array(img1)
    img2_arr = np.array(img2)

    # Resize second image to match the first
    img2_arr = np.array(img2.resize(img1.size))

    # Calculate SSIM between two images
    similarity_index = ssim(img1_arr, img2_arr)

    # Display the images
    #"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].imshow(img1_arr, cmap=plt.cm.gray)
    axes[0].set_title('Image 1')
    axes[0].axis('off')
    
    axes[1].imshow(img2_arr, cmap=plt.cm.gray)
    axes[1].set_title('Image 2')
    axes[1].axis('off')
    
    plt.suptitle(f'SSIM: {similarity_index:.2f}')
    plt.show()
    #"""
    return similarity_index

# Example usage
image_path1 = 'mask_left_reg.jpg'
image_path2 = 'mask_left_use.jpg'
similarity = image_similarity(image_path1, image_path2)
print(f"Structural Similarity Index: {similarity:.2f}")
