from PIL import Image

def flipX(image):
    """
    Flips the image horizontally (left to right).
    :param image: PIL Image object
    :return: PIL Image object, horizontally flipped
    """
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def flipY(image):
    """
    Flips the image vertically (top to bottom).
    :param image: PIL Image object
    :return: PIL Image object, vertically flipped
    """
    return image.transpose(Image.FLIP_TOP_BOTTOM)
