from threading import Thread

import httpx,json
def bir():
    url1 = 'https://api.chucknorris.io/jokes/random'
    birinchi = httpx.get(url1)
    l = birinchi.json()
    with open('birinchi.json', 'w') as f:
        json.dump(l, f, indent=4)


def ikki():
    url2 = 'https://api.chucknorris.io/jokes/categories'
    ikkinchi = httpx.get(url2)
    l = ikkinchi.json()
    with open('ikkinchi.json', 'w') as f:
        json.dump(l, f, indent=4)


def uch():
    url3 = 'https://api.chucknorris.io/jokes/categories'
    uchinchi = httpx.get(url3)
    l = uchinchi.json()
    with open('uchinchi.json', 'w') as f:
        json.dump(l, f, indent=4)


def tort():
    url4 = 'https://api.chucknorris.io/jokes/search?query={query}'
    tortinchi = httpx.get(url4)
    l = tortinchi.json()
    with open('tort.json', 'w') as f:
        json.dump(l, f, indent=4)


def besh():
    url5 = 'https://api.chucknorris.io/jokes/random?category={category}'
    beshinchi = httpx.get(url5)
    l = beshinchi.json()
    with open('besh.json', 'w') as f:
        json.dump(l, f, indent=4)
oqim1 = Thread(target=bir(), daemon=True)
oqim2 = Thread(target=ikki(), daemon=True)
oqim3 = Thread(target=uch(), daemon=True)
oqim4 = Thread(target=tort(), daemon=True)
oqim5 = Thread(target=besh(), daemon=True)