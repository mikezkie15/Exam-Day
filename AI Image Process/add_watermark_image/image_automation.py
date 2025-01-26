from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_image_path, output_image_path, watermark_text):
    # Check if the file exists
    if not os.path.isfile(input_image_path):
        print(f"Error: The file {input_image_path} does not exist.")
        return
    
    # Open the input image
    img = Image.open(input_image_path)

    # Convert the image to RGB mode if it has an alpha channel
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Define watermark text and font
    font = ImageFont.truetype("arial.ttf", 36)  # Replace 'arial.ttf' with your font file

    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate text position for centering
    text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # Add watermark text to the image
    draw.text(text_position, watermark_text, fill=(255, 255, 255, 128), font=font)

    # Save the watermarked image as JPEG format
    img.save(output_image_path, quality=95)  # Adjust quality as needed

# Replace 'Screenshot_73.png_no_bg' and 'output_image_watermarked.jpg' with your file paths
input_image_path = 'C:\Users\Mike\Documents\Code project\Another one\AI Image Process\add_watermark_image\name.png'
output_image_path = 'output_image_watermarked.jpg'
watermark_text = 'Faisal Zamir'

# Perform adding watermark to the image
add_watermark(input_image_path, output_image_path, watermark_text)
