import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize the plot
fig, ax = plt.subplots()

# Define the dimensions
horizontal_spaces = 9  # Number of spaces in the horizontal row
vertical_spaces = 9  # Number of spaces in the vertical column
space_width = 1
space_height = 2

# Function to draw a parking space
def draw_space(x, y, orientation='horizontal', color='white'):
    if orientation == 'vertical':
        rect = patches.Rectangle((x, y), space_height, space_width, linewidth=1, edgecolor='black', facecolor=color)
    else:
        rect = patches.Rectangle((x, y), space_width, space_height, linewidth=1, edgecolor='black', facecolor=color)
    ax.add_patch(rect)

# Create the L-shaped parking lot with default color
def create_parking_lot():
    # Draw the horizontal row of spaces at the top
    for j in range(horizontal_spaces):
        draw_space(j * space_width, vertical_spaces * space_height)
    
    # Draw the vertical column of spaces to the right, oriented horizontally
    for i in range(vertical_spaces):
        draw_space(horizontal_spaces * space_width, i * space_height, orientation='vertical')

# Function to fill specific parking spots with red
def fill_parking_spots(spot_numbers):
    # Recreate parking lot to clear previous fills
    create_parking_lot()
    total_spots = horizontal_spaces + vertical_spaces
    for spot_number in spot_numbers:
        if spot_number <= horizontal_spaces:
            # Horizontal spots (adjust for 0-indexing)
            x, y = (spot_number - 1) * space_width, vertical_spaces * space_height
            draw_space(x, y, color='red')
        elif spot_number <= total_spots:
            # Vertical spots, oriented horizontally (adjust for 0-indexing)
            x, y = horizontal_spaces * space_width, (spot_number - horizontal_spaces - 1) * space_height
            draw_space(x, y, 'vertical', color='red')

    # Set the limits of the plot to encompass the entire L-shape
    ax.set_xlim(0, (horizontal_spaces + 1) * space_width)
    ax.set_ylim(0, (vertical_spaces + 1) * space_height)

    # Set aspect of the plot to be equal
    ax.set_aspect('equal')

    # Turn off the axes
    plt.axis('off')

    # Show the plot
    plt.show()

# Example usage: Fill multiple spots with red
fill_parking_spots([9])
