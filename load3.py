for i, x in enumerate(list(range(100001))):
    print(i, end='\r')
from tqdm import tqdm
loop = tqdm(total = 5000, position=0, leave=False)
for k in range(5000):
    loop.set_description("Carregando... .format(k))")
    loop.update(1)
loop.close()