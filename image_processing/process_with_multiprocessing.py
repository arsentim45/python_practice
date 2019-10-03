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


def processing_worker(input_queue, result_queue):
    while True:
        try:
            image = result_queue.get()
            process_images(image)
        except queue.Empty:
            pass
        #result_queue.task_done()
        if input_queue.empty() and result_queue.empty():
            pass
            #return