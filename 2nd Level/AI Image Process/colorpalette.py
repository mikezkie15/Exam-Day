from PIL import Image
from collections import Counter
import webcolors

def generate_palette(image_path, num_colors):
    image = Image.open(image_path)

    if image.mode == 'RGBA':
        image = image.convert('RGB')

    pixels = Counter(image.getdata()) 

    color_counter = Counter(pixels)

    most_common = color_counter.most_common(num_colors)

    print(f"Top {num_colors} colors in the image:\n")

    for color, count in most_common:
        try:
            color_name = webcolors.rgb_to_name(color[:3])
        except ValueError:
            color_name = "N/A"
        print(f"Color: {color[:3]}, Count: {count}, Name: {color_name}")

# Define input image path
input_image_path = 'images.jpg'

# Number of colors to extract
num_colors_to_extract = 20

# Call the function
generate_palette(input_image_path, num_colors_to_extract)
