from PIL import Image
import random
import os
import string

image_path = str(input("Enter the path to your image: "))
image_path = os.path.expanduser(image_path) # Expand the user home directory if ~ is used
image = Image.open(image_path)

small_image = image.resize((4, 4), Image.LANCZOS)

# Extract the directory, base name, and extension of the original image
directory, file_name = os.path.split(image_path)
base_name, ext = os.path.splitext(file_name)

new_file_name = f"{base_name}_small.jpg"
new_image_path = os.path.join(directory, new_file_name)
small_image.save(new_image_path)

char_list = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)

pixels = []

pixel_data = small_image.getdata()

for pixel in pixel_data:
    pixels.append(pixel)

pixels_sorted_by_brightness = sorted(pixels, key=lambda x: 0.299*x[0] + 0.587*x[1] + 0.114*x[2])

def generate_seed_from_rgb(rgb):
    seed = hash(rgb)
    random.seed(seed)
    return random.randint(0, len(char_list))

password = []

random_ints = [generate_seed_from_rgb(pixel) for pixel in pixels]
for el in random_ints:
    password.append(char_list[el])

password_string = ''.join(password)
print(f"Pixels array: {pixels}")
print(f"Pixels sorted by brightness: {pixels_sorted_by_brightness}")
print(f"Password array: {password}")
print(f"Password: {password_string}")
