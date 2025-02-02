from PIL import ImageEnhance, Image


def adjust_brightness(input_image_path, out_image_path, factor):
    img = Image.open(input_image_path)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    enchancer = ImageEnhance.Brightness(img)
    enhanced_img = enchancer.enhance(factor)


    enhanced_img.save(out_image_path, format='JPEG', quality=95)

brightness_factor = 1.5

input_image_path = 'rolith.jpg'
output_image_path = 'enhanced.jpg'

adjust_brightness(input_image_path, output_image_path, brightness_factor)