import monoschinos as mc
import os

query = input("Search: ")

search = mc.search_anime(query)

for i,anime  in enumerate(search):
    print(f"[{i}] {anime['title']}")

index = int(input("Select: "))
anime = mc.get_info(search[index]["url"])

for i,ep in enumerate(anime["episodes"]):
    print(f"[{i}] {ep['name']}")

index = int(input("Select: "))
ep = anime["episodes"][index]["url"]

servers = mc.get_player_links(ep)

for i,server in enumerate(servers):
    print(f"[{i}] {server['name']}")
    
while True:
    index = int(input("Select: "))
    server = servers[index]["url"]

    os.system(f"START {server}")