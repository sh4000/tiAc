# transform an image to ASCII characters
# *as4h

import numpy as np
from skimage import io

def convert_image_to_ascii(image_file):
    image = io.imread(image_file)

    grayscale_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]
    threshold = 200

    output_str = ""
    for row in grayscale_image:
        for pixel in row:
            ascii_char = ascii_chars[int(pixel / threshold)]
            output_str += ascii_char
        output_str += "\n"
        
    with open("ascii_image.txt", "w") as text_file:
        text_file.write(output_str)

convert_image_to_ascii("test.jpg")
