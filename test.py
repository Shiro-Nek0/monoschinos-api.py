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

print(json.dumps(get_links, indent=3))
