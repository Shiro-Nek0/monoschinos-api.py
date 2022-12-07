# monoschinos-api.py
web scrapping api for monoschinos

Requires:
bs4, base64, requests, unidecode

Tested on Python 3.10.6

```python
import json
import monoschinos as mc

anime_name = "tensei shitara"

search = mc.search_anime(anime_name)[0]['url']

get_info = mc.get_info(search)

get_links = mc.get_player_links(get_info['episodes'][0]['url'])

print(get_info['title'])
print(f"Rating: {get_info['rating']}")
print(f"Genres {get_info['genres']}")

print(f"URL: {search}")

print(get_info['sinopsis'])

print(get_info['img'])

print(f"Episodes: {len(get_info['episodes'])}")

#print(json.dumps(get_links, indent=3))
```

Output:

```
Tensei shitara Ken Deshita
Rating: 4.9
['Acción', 'Fantasía']
URL: https://monoschinos2.com/anime/tensei-shitara-ken-deshita-sub-espanol
¡El héroe de Tensei shitara, Ken deshita, se diferencia del protagonista de otro mundo estándar en que se reencarna en una espada! Comenzando su búsqueda desovando en medio de un bosque plagado de bestias, se encuentra con una chica herida que huye frenéticamente para salvar su vida. agresores, la pareja se familiariza, y la niña se presenta como Fran. Ella tiene un pasado pesado, habiendo soportado la esclavitud y el maltrato de su tribu, los Gatos Negros. Como el héroe es incapaz de recordar el nombre de su vida pasada a partir de entonces, ¡Shishou y Fran se convierten en un equipo formidable que se embarca en misiones para liberar a los oprimidos y hacer justicia!
https://monoschinos2.com/assets/img/serie/portada/tensei-shitara-ken-deshita-1663803615.jpg
Episodes: 10
```
