
import os
import re
import json
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def get_song_info(url: str, quality: str = "hq") -> dict:
    resp = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10)
    real_url = resp.url

    page = requests.get(real_url, headers=HEADERS, timeout=10)
    if page.status_code != 200:
        raise ValueError("صفحه یافت نشد یا با خطا مواجه شد.")

    soup = BeautifulSoup(page.text, 'html.parser')
    json_data = None
    for script in soup.find_all("script"):
        if script.get("id") == "__NEXT_DATA__" and script.string:
            json_data = json.loads(script.string)
            break

    if not json_data:
        raise ValueError("اطلاعات آهنگ قابل دریافت نیست.")

    props = json_data["props"]["pageProps"]
    media = props.get("media") or props.get("podcast")

    if isinstance(media, list):
        media = media[0]

    return {
        "title": media.get("song") or media.get("title", ""),
        "artist": media.get("artist") or media.get("podcast_artist", ""),
        "date": media.get("created_at", ""),
        "cover": media.get("photo") or media.get("coverPhoto"),
        "lyrics": media.get("lyric", ""),
        "hq": media.get("hq_link"),
        "lq": media.get("lq_link"),
        "selected": media.get(f"{quality}_link")
    }

def download_audio(url: str, output_path: str = None):
    info = get_song_info(url)
    link = info.get("selected")

    if not link:
        raise ValueError("لینک دانلود پیدا نشد.")

    filename = sanitize_filename(f"{info['artist']} - {info['title']}.m4a")
    path = output_path or filename

    response = requests.get(link, headers=HEADERS)
    with open(path, "wb") as f:
        f.write(response.content)

    return path
