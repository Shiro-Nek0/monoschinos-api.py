from bs4 import BeautifulSoup
from base64 import b64decode
from requests import get

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"


def request_content(url):
    r = get(url, timeout=30, headers={"User-Agent": useragent})
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_recent():
    animes = {}
    soup = request_content("https://monoschinos2.com/")

    recents = soup.find_all("div", {"class": "row row-cols-5"})

    for link in recents:
        titles = link.find_all("h2", {"class": "animetitles"})
        for title in titles:
            print(title.text)


def get_player_links(url):
    video_urls = {}
    soup = request_content(url)

    players = soup.find_all("p", {"class": "play-video"})
    for player in players:
        encoded_link = player.get("data-player")
        decoded_link = b64decode(encoded_link).decode("utf-8")
        decoded_link = decoded_link[decoded_link.find("url=")+4:]
        video_urls[player.text] = (
            {"url": decoded_link}
        )
    return video_urls


def search_anime(query, page=None):
    anime_result = []

    if (page != None):
        query += "?p={page}"

    soup = request_content(f"https://monoschinos2.com/buscar?q={query}")

    single = soup.find_all("div", {"class": "col-md-4 col-lg-2 col-6"})
    for s in single:
        title = s.find("h3", {"class": "seristitles"}).text
        info = s.find("span", {"class": "seriesinfo"}).text
        img = s.find("img", {"class": "animemainimg"}).get("src")
        url = s.find("a").get("href")
        anime_result.append({
            "title": title,
            "info": info,
            "img": img,
            "url": url
        })

    return anime_result

def get_seasonal(page=None):
    animes = {}
    page_url = "https://monoschinos2.com/emision"

    if (page != None):
        page_url += f"?p={page}"

    soup = request_content(page_url)

    recents = soup.find_all("div", {"class": "col-md-4 col-lg-2 col-6"})

    for list in recents:
        title = list.find("h3", {"class": "seristitles"}).text
        info = list.find("span", {"class": "seriesinfo"}).text
        img = list.find("img", {"class": "lozad"}).get("data-src")
        url = list.find("a").get("href")
        animes[title] = {
            "info": info,
            "img": img,
            "url": url
        }
    return animes

def get_daily():
    whole_week = {}
    
    page_url = "https://monoschinos2.com/calendario"
    soup = request_content(page_url)
    week = soup.find_all("div", {"class": "accordionItem close"})
    for day in week:
        day_name = day.find("h1", {"class": "accordionItemHeading"}).text.replace(" ", "").lower()
        anime_list = day.find_all("div", {"class": "series"})
        single_day = {}
        for anime in anime_list:
            tags_arr = []

            title = anime.find("div", {"class": "serisdtls"}).find("h3").text
            sinopsis = anime.find("div", {"class": "serisdtls"}).find("p").text
            episode = anime.find("div", {"class": "serisdtls"}).find("h4").text
            img = anime.find("img", {"class": "lozad"}).get("data-src")
            url = anime.find("a").get("href")
            tags = anime.find_all('button')
            for tag in tags:
                tags_arr.append(tag.text)

            single_day[title] = {
                "sinopsis": sinopsis,
                "episode": episode,
                "img": img,
                "url": url,
                "tags": tags_arr
            }
        whole_week[day_name] = single_day

    return whole_week

def get_info(url):
    info = {}
    episodes = []
    genres_arr = []
    soup = request_content(url)
    all = soup.find("div", {"class": "heromain"})
    info["title"] = all.find("h1", {"class": "mobh1"}).text
    info["sinopsis"] = all.find("p", {"class": "textComplete"}).text.replace(" Ver menos", "")
    info["img"] = all.find("div", {"class": "herobg"}).find("img").get("src")
    info["rating"] = all.find("div", {"class": "chapterpic"}).find("p").text
    info["release_date"] = all.find_all("ol", {"class": "breadcrumb"})[1].find("li", {"class": "breadcrumb-item"}).text
    genres = all.find_all("ol", {"class": "breadcrumb"})[0].find_all("li", {"class": "breadcrumb-item"})

    for genre in genres:
        genres_arr.append(genre.text)

    info["genres"] = genres_arr

    episode_list = soup.find_all("div", {"class": "col-item"})
    for episode in episode_list:
        name = episode.find("p", {"class": "animetitles"}).text
        img = episode.find("img", {"class": "lozad animeimghv"}).get("data-src")
        url = episode.find("a").get("href")
        episodes.append({
            "name": name[:-1],
            "url": url,
            "thumbnail": img
        })
    info["episodes"] = episodes
    return info