# Задание 3

import multiprocessing as mp
import grequests
import requests

from tqdm import tqdm
import datetime

# Добавить пограничные случаи и чтобы запускалось с панели админа
a = datetime.datetime.now()

for i in tqdm(range(8), unit_scale=125):
    urls = [f'https://www.youtube.com' for i in (range(125))]
    response = (grequests.get(url) for url in urls)
    res = grequests.map(response)
b = datetime.datetime.now()      
print(b-a)
print()
