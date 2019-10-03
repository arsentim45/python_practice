from time import time

from common_utils.storage_functions import get_download_dir
from database.constants_parser import name
from multiprocessing import Queue

start_time = time()
download_que = Queue()
processing_que = Queue()
download_dir = get_download_dir(name)