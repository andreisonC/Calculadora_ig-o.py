for i, x in enumerate(list(range(1000))):
    print(i, end='\r')


from asyncore import loop
from tqdm import tqdm
loop = tqdm(total=40000)
for k in range(40000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close


from tqdm.auto import tqdm
for i in tqdm(range(1000)):
    print(" ", end='\r')