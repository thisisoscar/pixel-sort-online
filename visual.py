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


def colour_compare(a, b):
    if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]) or (a[0] == b[0] and a[1] == b[1] and a[2] > b[2]):
        return True
    return False

def bubble_sort(array):
    while True:
        for i in range(len(array)-1):
            this_ = array[i]
            next_ = array[i+1]
            if colour_compare(this_, next_):
                array[i], array[i+1] = array[i+1], array[i]
                yield array


'''def merge_sort(array):
    halfway = len(array) // 2
    l = array[:halfway]
    r = array[halfway:]

    if len(l) != 1:
        l = merge(l)
    if len(r) != 1:
        r = merge(r)
    
    merged = []
    while len(l) > 0 and len(r) > 0:
        if l < r:
            merged.append(l)
            l.pop(0)
        else:
            merged.append(r)
            r.pop(0)
    
    merged = merged + l + r'''


def get_sort_order(array):
    sort_order = []
    length = len(array)
    subarray_length = 0.5
    
    while subarray_length < length:
        subarray_length = int(subarray_length * 2)
        layer = []
        
        for i in range(0, length, subarray_length):
            start = i
            end = i + subarray_length
            
            if end <= length:
                layer.append([j for j in range(start, end)])
           
            else:
                layer.append([j for j in range(start, length)])
        
        sort_order.append(layer)
    
    return sort_order


def get_comparisons_list(array):
    array = array.copy()
    comparisons = []
    
    for layer in get_sort_order(array):
        for i in range(0, len(layer), 2):
            if i + 1 < len(layer):
                comparisons.append([layer[i], layer[i+1]])
    
    return comparisons


def shift(array, old_index, new_index):
    for i in range(old_index, new_index, -1):
        a = i
        b = i-1
        array[a], array[b] = array[b], array[a]
    
    return array


def merge_index_lists(array, a_indexes, b_indexes):
    array = array.copy()
    a_indexes = a_indexes.copy()
    b_indexes = b_indexes.copy()
    last_sorted_index = min(a_indexes[0], b_indexes[0])
    
    while len(a_indexes) > 0 and len(b_indexes) > 0:
        if colour_compare(array[a_indexes[0]], array[b_indexes[0]]):
            a_indexes.pop(0)
            last_sorted_index += 1
        
        else:
            array = shift(array, b_indexes[0], last_sorted_index)
            b_indexes.pop(0)
            a_indexes = [i+1 for i in a_indexes]
            last_sorted_index += 1
    
    return array


def in_place_merge(array):
    array = array.copy()
    comparisons = get_comparisons_list(array)
    
    for indexes in comparisons:
        array = merge_index_lists(array, indexes[0], indexes[1])
        
        yield array
    
    # so it doesnt crash when the sort is finished
    while True:
        yield array
    

location = input('Enter the directory of the image you want to see being sorted: ')
valid = False
while not valid:
    algorithm = input('Enter the sorting algorithm you want to see:\n[1] bubble\n[2] merge\n: ')
    if algorithm in ['1', '2']:
        valid = True
    else:
        print(algorithm, 'wasn\'t an option')

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
screen_width, screen_height = screen.get_size()
clock = pg.time.Clock()

image = Image.open(location).convert('RGB')
image_width, image_height = image.size

if algorithm == '1': # type: ignore
    sorter = bubble_sort(pil_to_list(image))
elif algorithm == '2': # type: ignore
    sorter = in_place_merge(pil_to_list(image))

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    draw_pil(image)
    
    image = pil_to_list(image)
    
    image = next(sorter) # type: ignore
    
    image = list_to_pil(image)

    pg.display.flip()
