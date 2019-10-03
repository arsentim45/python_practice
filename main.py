import time

from threading import Thread
from multiprocessing import Process

from database.constants_parser import search_url, subscription_key, size, name, count
from initialization import download_que, processing_que, start_time
from server.echo_server import echo_server
from image_downloading.download_with_threads import downloading_worker
from image_processing.process_with_multiprocessing import processing_worker


def main():
    processes = 10
    downloading_process = Thread(target=downloading_worker, args=(download_que, processing_que, ))
    downloading_process.daemon = True
    downloading_process.start()
    procesing_process = Process(target=processing_worker, args=(download_que, processing_que, ))
    procesing_process.daemon = True
    procesing_process.start()
    echo_server(download_que)

    execution_time = round(time.time() - start_time, 3)
    print(f'It took {execution_time} seconds to download and process {count} {"cats"} images')


if __name__ == '__main__':
    main()