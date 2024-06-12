from PIL import Image, ImageEnhance

def adjust_saturation(image, saturation_factor):
    """
    Adjusts the saturation of an image.
    :param image: PIL Image object
    :param saturation_factor: float; < 1 decreases saturation, > 1 increases it
    :return: PIL Image object with adjusted saturation
    """
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(saturation_factor)

def adjust_brightness(image, brightness_factor):
    """
    Adjusts the brightness of an image.
    :param image: PIL Image object
    :param brightness_factor: float; < 1 makes the image darker, > 1 makes it brighter
    :return: PIL Image object with adjusted brightness
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness_factor)

def adjust_contrast(image, contrast_factor):
    """
    Adjusts the contrast of an image.
    :param image: PIL Image object
    :param contrast_factor: float; < 1 decreases contrast, > 1 increases it
    :return: PIL Image object with adjusted contrast
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast_factor)
