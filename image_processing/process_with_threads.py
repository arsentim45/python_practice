import queue
from PIL import Image, ImageDraw
from database.constants_parser import size


def process_images(image_path):
    img = Image.open(image_path)
    img = img.resize(size, Image.ANTIALIAS)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), 'cats', (0, 0, 0))
    print(f'RESIZING and DRAWING {image_path}')
    img.save(image_path)
    #q2.task_done()

def procesing_images(num ,q2):
    while True:
        try:
            image_path = q2.get(timeout=0.5)
            print(image_path)
        except queue.Empty:
            return
        process_images(image_path)
        q2.task_done()