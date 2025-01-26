from PIL import Image

# Define Paths and Dimensions
input_image_path = "rolith.jpg"
output_image_path = "resize.jpg"
desired_width = 200
desired_height = 200

# Open the Input Image
input_image = Image.open(input_image_path)

# Resize the image
input_image = input_image.resize((desired_width, desired_height))

# Save the resized image
input_image.save(output_image_path)

print("Code Executed Successfully ...")
