from PIL import Image
import numpy as np
import pygame as pg


def pil_to_list(image):
    image = image.convert('HSV')
    pixels = list(image.getdata())
    
    return pixels


def list_to_pil(array):
    array = np.array(array)
    array = array.reshape(image_height, image_width, 3)
    image = Image.fromarray(array.astype(np.uint8), 'HSV')

    return image


def draw_pil(image):
    pil_image = image.resize((screen_width, screen_height), resample=Image.FIXED).convert('RGB')
    pg_image = pg.image.frombuffer(pil_image.tobytes(), pil_image.size, pil_image.mode)
    screen.blit(pg_image, (0, 0))


def bubble_sort(array):
    while True:
        for i in range(len(array)-1):
            this_ = array[i]
            next_ = array[i+1]
            if this_[0] > next_[0] or (this_[0] == next_[0] and this_[1] > next_[1]) or (this_[0] == next_[0] and this_[1] == next_[1] and this_[2] > next_[2]):
                array[i], array[i+1] = array[i+1], array[i]
                yield array
    

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
screen_width, screen_height = screen.get_size()
clock = pg.time.Clock()

location = input('Enter the directory of the image you want to see being sorted: ')

image = Image.open(location).convert('RGB')
image_width, image_height = image.size

sorter = bubble_sort(pil_to_list(image))

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

    draw_pil(image)
    
    image = pil_to_list(image)
    
    image = next(sorter)
    
    image = list_to_pil(image)

    pg.display.flip()
