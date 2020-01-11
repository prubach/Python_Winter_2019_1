import logging
from concurrent.futures.process import ProcessPoolExecutor
from functools import partial
from pathlib import Path
from queue import Queue
from threading import Thread
from multiprocessing.pool import Pool

from knotprot_download import setup_download_dir, get_proteins, download_link, time_it, create_thumbnail

# Example based by code from:
# https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Run in a single Thread
def run_single():
    dir = setup_download_dir()
    proteins = get_proteins()
    for protein in proteins:
        download_link(dir, protein)

# Run using multiple Workers

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()


def workers():
    dir = setup_download_dir()
    proteins = get_proteins()
    queue = Queue()
    for x in range(4):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for protein in proteins:
            logger.info('Queueing {0}_{1}'.format(protein[0], protein[1]))
            queue.put((dir,protein))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()

# End of run using multiple Workers

# Using multiprocessing Pool

def multi_pool():
    dir = setup_download_dir()
    proteins = get_proteins()
    download = partial(download_link, dir)
    with Pool(8) as p:
        p.map(download, proteins)

def thumbnails():
    for image_path in Path('images').iterdir():
        create_thumbnail((128, 128), image_path)

def thumbnails_pool():
    thumbnail_128 = partial(create_thumbnail, (128, 128))
    with ProcessPoolExecutor() as executor:
        executor.map(thumbnail_128, Path('images').iterdir())

if __name__ == '__main__':
    #time_it(run_single)
    #time_it(workers)
    #time_it(multi_pool)
    time_it(thumbnails_pool)
