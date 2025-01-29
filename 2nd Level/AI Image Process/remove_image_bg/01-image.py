from removebg import RemoveBg

# Initialize RemoveBg with your API key
api_key = 'oCqKHKmNbcxznXoXGyj9Jftb' 
removebg = RemoveBg(api_key, "error.log")

# Path of your image
input_image = 'C:\Users\Mike\Documents\Code project\Another one\AI Image Process\remove_image_bg\rolith.jpg'

# Remove background from the input image
removebg.remove_background_from_img_file(input_image, size="regular")

print("Code Executed Successfully ...")
