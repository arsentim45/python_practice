import os
import queue
from urllib.request import urlopen

from common_utils.storage_functions import get_random_name
from initialization import download_dir

def download_image(image_url):
    with urlopen(image_url) as image:
        image_name = get_random_name()
        image_path = os.path.join(download_dir, image_name)
        with open(image_path, 'wb') as f:
            f.write(image.read())
    print(f'Downloaded {image_url} to {image_path}')
    return image_path


def downloading_worker(input_queue, result_queue):
    while True:
        try:
            url = input_queue.get()
        except queue.Empty:
            pass
        downloaded_path = download_image(url)
        result_queue.put_nowait(downloaded_path)
        if input_queue.empty():
            pass