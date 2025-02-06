from PIL import Image


def rotated_image(input_image_path,image_rotation):
    img = Image.open(input_image_path)

    rotated_image = img.rotate(image_rotation)

    if rotated_image.mode == 'RGBA':
        rotated_image = rotated_image.convert('RGB')

    rotated_image.save('rotated_image.jpg')

image_used = 'images.jpg'
image_rotation = 240

rotated_image(image_used,image_rotation)