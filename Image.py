import cv2

def edge_detection(image):

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)

    cv2.imwrite("final.png", edges)

