# ThreadPool
import concurrent.futures


def worker():
    print("Worker Thread Running")


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
