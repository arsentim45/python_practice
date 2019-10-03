warehouse_id = 22
import os
import glob


def count_images(product, previous_product):
    try:
        directory = os.path.join('/data/iwp/train_images/', str(warehouse_id), str(previous_product))
        images_count2 = len(glob.glob1(directory, "*.jpg"))
        images_count2 += len(glob.glob1(directory, "*.jpeg"))
    except:
        images_count2 = 0
    try:
        directory = os.path.join('/data/iwp/train_images/', str(warehouse_id), str(product))
        images_count = len(glob.glob1(directory, "*.jpg"))
        images_count += len(glob.glob1(directory, "*.jpeg"))
    except:
        images_count = 0
    return images_count2 + images_count


def directory_decorator(func):
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)

def path_creation(arg1, arg2):
    return os.path.join('/data/iwp/train_images/', str(arg1), str(arg2))

from functools import reduce

def count_images2(previous_product, product):
    def type_func(arg1, arg2):
        return len(glob.glob1(path_creation(warehouse_id,arg1[0]), arg1[1])) + \
               len(glob.glob1(path_creation(warehouse_id,arg2[0]), arg2[1]))
    return reduce(type_func, ([previous_product,"*.jpg"], [previous_product,"*.jpeg"])) + \
           reduce(type_func, ([product,"*.jpg"], [product,"*.jpeg"]))

if __name__ == '__main__':
    print(reduce(count_images2, [0,1]))