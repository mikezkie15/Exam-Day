from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_image_path, output_image_path, watermark_text):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_image_path):
            raise FileNotFoundError(f"The file {input_image_path} does not exist.")
        
        # Open the input image
        with Image.open(input_image_path) as img:
            # Convert to RGB if the image has an alpha channel
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            draw = ImageDraw.Draw(img)
            
            # Attempt to load a font; use default if 'arial.ttf' is not found
            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except IOError:
                # Use Pillow's default font if specified font isn't available
                font = ImageFont.load_default()
                print("Warning: 'arial.ttf' not found. Using default font.")
            
            # Calculate text size and position
            text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
            
            # Use RGB color (light gray) without alpha for JPEG compatibility
            draw.text(text_position, watermark_text, fill=(200, 200, 200), font=font)
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
            
            # Save the image with appropriate format based on extension
            img.save(output_image_path, quality=95)
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = 'images.jpeg'
output_image_path = 'output_image_watermarked.jpg'
watermark_text = 'Faisal Zamir'

add_watermark(input_image_path, output_image_path, watermark_text)