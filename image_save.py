import os
import time
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kale.settings')

django.setup()

from django.core.files import File
from django.http import HttpResponse

from basic_app.models import AllProductImages


def save_images_to_model():
    # Path to directory containing images
    image_dir_path = 'C:/Users/ulugbek/PycharmProjects/abba_kale/media/images_webp'

    # Get all files in the image directory
    files = os.listdir(image_dir_path)

    # Filter out non-image files
    image_files = [f for f in files if f.endswith('.webp')]
    arr = 0
    # Save each image file to the Product model
    for img_file in image_files:
        # Extract image name from file name
        img_name1 = os.path.splitext(img_file)[0]
        img_name = img_name1.split('_')[1]
        if img_name != '':
            img_name = img_name.split('_')[0]
            print(img_name)
            arr += 1
        elif img_name == '':
            img_name = img_name1.split('__')[1]
            img_name = img_name.split('_')[0]
            print(img_name)
            arr += 1

        product = AllProductImages(name=img_name)
        with open(os.path.join(image_dir_path, img_file), 'rb') as f:
            img_file_obj = File(f)
            product.image.save(img_file, img_file_obj, save=True)
    print(arr)

    # Return a success response
    return 'ok'


# save_images_to_model()

def get_image_name_and_path(name):
    product_images = AllProductImages.objects.filter(name=name)
    if product_images:
        return [(product_image.name, product_image.image.path) for product_image in product_images]
    else:
        return []


a = get_image_name_and_path('лейка gold')
img = [i[1] for i in a]
print(img)
