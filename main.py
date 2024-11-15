import inky
import os
import PIL
import random
import time



HOLD_TIMER_SEC = 360

SCRIPT_PATH = os.path.dirname(__file__)
IMAGE_CACHE_DIRECTORY = os.path.join(SCRIPT_PATH, 'images')
IMAGE_FILE_CACHE = []

CURRENT_IMAGE = ''



def get_image_cache_content() -> list:
    global IMAGE_CACHE_DIRECTORY
    cache_content = os.listdir(IMAGE_CACHE_DIRECTORY)
    
    print('Number of images in cache is', len(cache_content))
    print(cache_content)

    return cache_content


def select_random_image() -> PIL.Image:
    global IMAGE_FILE_CACHE
    image_pool = IMAGE_FILE_CACHE.copy()

    global CURRENT_IMAGE
    if CURRENT_IMAGE in image_pool: 
        image_pool.remove(CURRENT_IMAGE)

    random_image = random.choice(image_pool) 
    CURRENT_IMAGE = random_image
    
    global IMAGE_CACHE_DIRECTORY
    random_image_absolute_path = os.path.join(IMAGE_CACHE_DIRECTORY, random_image)

    img = PIL.Image.open(random_image_absolute_path)

    return img 


def scale_image(image, resolution) -> PIL.Image:
    scaled_image = image.resize(resolution)        

    return scaled_image


def select_border(image: PIL.Image) -> int:
    # TODO: Make logic to find best border color.

    return inky.BLACK


def display_new_image(display) -> None:
    selected_image = select_random_image()
    
    print('selected image', selected_image)

    image_to_display = scale_image(selected_image, display.resolution)

    print('scaled image', image_to_display)
    
    border_colour = select_border(image_to_display)
    
    display.set_border(border_colour)
    display.set_image(image_to_display)
    display.show()


def main() -> None:
    display = inky.auto()

    if display is None:
        print('Could not find compatible display! The program will exit.')
        exit()
    
    global IMAGE_FILE_CACHE
    IMAGE_FILE_CACHE = get_image_cache_content()

    while(True):
        display_new_image(display)

        print('Sleeping for', HOLD_TIMER_SEC, 'seconds.')

        time.sleep(HOLD_TIMER_SEC)


if __name__ == '__main__':
    main()

    print("Program end.")
