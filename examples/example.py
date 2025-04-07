from rjdl import get_song_info, download_audio

# URL of a song from RadioJavan
url = "https://play.radiojavan.com/song/abcd1234"

# Get song information
info = get_song_info(url)
print("🎵 Title:", info["title"])
print("🎤 Artist:", info["artist"])
print("🗓 Date:", info["date"])
print("🎧 HQ Link:", info["hq"])

# Download the audio file
filename = download_audio(url)
print("✅ File saved as:", filename)
