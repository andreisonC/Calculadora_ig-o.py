from tqdm import tqdm 
import time
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)
