from knotprot_download import get_proteins, download_link, setup_download_dir, time_it, create_thumbnail
from threading import Thread
from queue import Queue
from multiprocessing.pool import Pool
from concurrent.futures.process import ProcessPoolExecutor
from functools import partial
from pathlib import Path

def run_single(dir):
    proteins = get_proteins()
    #print(proteins)
    for protein in proteins:
        download_link(dir, protein)

## Multithreaded using Thread and worker

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            dir, prot = self.queue.get()
            try:
                download_link(dir, prot)
            finally:
                self.queue.task_done()

def workers(dir):
    proteins = get_proteins()
    # print(proteins)
    queue = Queue()
    for n in range(4):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for prot in proteins:
        queue.put((dir, prot))
        print("Added to queue: " + str(prot))
    queue.join()

########### Multithreaded using a Pool
### Only on UNIX systems ####
def multi_pool(dir):
    proteins = get_proteins()
    download = partial(download_link, dir)
    with Pool(4) as p:
        p.map(download, proteins)

##### Thumbnails ####

def thumbnails(dir):
    for image_path in Path(dir).iterdir():
        print(image_path)
        create_thumbnail( (256, 256), image_path)


def thumbnails_pool(dir):
    thumbnails_part = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor() as executor:
        executor.map(thumbnails_part, Path(dir).iterdir())

dir = setup_download_dir()
time_it(run_single, dir)
#time_it(workers, dir)
#time_it(multi_pool, dir)
print('thumbnails single')
time_it(thumbnails, dir)
print('thumbnails multi')
time_it(thumbnails_pool, dir)



