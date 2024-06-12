from PIL import Image

# Function to save in a list, sublists with white pixels coordinates, on black background [x, y]
def pixels_coordinates(image):
    coordinates = []
    with Image.open(image) as img:
        width, height = img.size
        img = img.convert('RGB')
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                if (r, g, b) != (0, 0, 0):  # Correct comparison with black
                    coordinates.append([x, y])

    return coordinates


# Function to save in lists all sublists with coordinates of adjacent pixels (horizontally, vertically and diagonally), using BFS algorithm for graphs
def adjacent_pixels(coordinates):
    edges = []

    while coordinates:
        queue = [coordinates.pop(0)] # First pixel for checking will be first from coordinates list, and in the same time delete it from coordinates
        adjacent_pairs = []

        while queue:
            x1, y1 = queue.pop(0) # x1 and y1 are coordinates from first piexl from queue, and in the same time delete it from queue
            adjacent_pairs.append([x1, y1]) # add it adjacent_pairs, like first pixel from the edge

            for i in reversed(range(len(coordinates))): # Reverese to don't mess up indexes
                x2, y2 = coordinates[i]
                if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1: # Check if pixels are adjacent
                    queue.append(coordinates.pop(i)) # If adjacent pixels, delete pixel from coordinates and add it to queue, to check further

        edges.append(adjacent_pairs)
    return edges


def get_upper_edge_pixels(pixel_list):

    for edge in pixel_list:
        # Sort the list first by x then by y
        pixel_list.sort(key=lambda p: (p[0], p[1]))

        # Function to check if the next pixel is a vertical continuation
        def is_continuous(current, next_pixel):
            return current[0] == next_pixel[0] and current[1] + 1 == next_pixel[1]

        # List to store the upper edge pixels
        upper_edge_pixels = []

        # Iterate through the pixel list
        for i in range(len(pixel_list) - 1):  # -1 because we'll look ahead by 1
            # If the next pixel is not continuous, or it is the last pixel in the sublist, add the current pixel
            if not is_continuous(pixel_list[i], pixel_list[i + 1]):
                upper_edge_pixels.append(pixel_list[i])

        # Always add the last pixel in the list because it has no next pixel to check against
        upper_edge_pixels.append(pixel_list[-1])

    return upper_edge_pixels

def sort_pixels_by_adjacency(pixels):
    if not pixels:
        return []

    # Function to calculate the square of the distance between two pixels
    def distance_sq(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    # Start with the first pixel
    sorted_pixels = [pixels[0]]
    remaining_pixels = set(tuple(pixel) for pixel in pixels[1:])

    # While there are unsorted pixels
    while remaining_pixels:
        last_pixel = sorted_pixels[-1]
        # Find the nearest next pixel (minimize the square of the distance)
        next_pixel = min(remaining_pixels, key=lambda p: distance_sq(p, last_pixel))
        sorted_pixels.append(list(next_pixel))
        remaining_pixels.remove(next_pixel)

    return sorted_pixels


def get_all_edges(pixel_list):
    # Initialize the list of edges and a set to track used x-coordinates
    edges = []
    used_x_coordinates = set()

    # Start with the first pixel in a new edge
    current_edge = [pixel_list[0]]
    used_x_coordinates.add(pixel_list[0][0])

    # Iterate through the pixel list starting from the second pixel
    for pixel in pixel_list[1:]:
        x, _ = pixel
        # Check if the x-coordinate has been used in the current edge
        if x in used_x_coordinates:
            # If used, start a new edge
            edges.append(current_edge)
            current_edge = [pixel]
            used_x_coordinates = {x}
        else:
            # If not used, add the pixel to the current edge
            current_edge.append(pixel)
            used_x_coordinates.add(x)

    # Add the last edge if it's not empty
    if current_edge:
        edges.append(current_edge)

    return edges