from PIL import Image

def crop_image(input_image_path, output_image_path, crop_box):
    # Open the image
    img = Image.open(input_image_path)

    # Crop the image with the specified crop box (left, right, lower)
    cropped_img = img.crop(crop_box)

    # Convert the image to RGB mode if it has an alpha channel
    if img.mode == 'RGBA'
        cropped_img = cropped_img.convert('RGB')

    # Save the cropped image as JPEG format
    cropped_img.save(output_image_path, quality =95) # Adjust quality as needed

# replace 'input_image.png' and 'cropped_image.png' with your file path
input_image_path = 'Mike Sordilla.png'
output_image_path = 'cropped_image.jpg'

# Define the crop box coordinates (left, upper, right, lower)
crop_box = (100, 100, 400, 400 )

# Perform the image cropping
crop_image(input_image_path, output_image_path, crop_box)