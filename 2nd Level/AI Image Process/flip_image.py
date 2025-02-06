from PIL import Image

def flip_image(input_image_path,flip_direction):
    img = Image.open(input_image_path)
    
    flip_horizontal = img.transpose(flip_direction)

    flip_horizontal.save('fliped_horizontal.jpg')

input_image_path = 'stock.jpg'
flip_direction = Image.FLIP_LEFT_RIGHT #Image.FLIP_LEFT_RIGHT == horizontal
                                        #Image.FLIP_TOP_BOTTOM == vertical


flip_image(input_image_path,flip_direction)