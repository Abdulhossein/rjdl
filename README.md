<div dir="rtl" align="right">
# rjdl - دانلودر رادیوجوان

`rjdl` یک کتابخانه‌ی ساده و سبک پایتون برای دریافت اطلاعات و دانلود فایل صوتی آهنگ‌ها و پادکست‌های RadioJavan است.

## نصب

```bash
git clone https://github.com/Abdulhossein/rjdl.git
cd rjdl
pip install .
```

## وابستگی‌ها

```bash
pip install -r requirements.txt
```

## استفاده

```python
from rjdl import get_song_info, download_audio

# دریافت اطلاعات آهنگ
url = "https://play.radiojavan.com/song/abcd1234"
info = get_song_info(url)
print(info)

# دانلود فایل صوتی
download_audio(url)
```

## خروجی نمونه تابع `get_song_info`:

```json
{
  "title": "Asheghaneh",
  "artist": "Ebi",
  "date": "2023-11-02",
  "cover": "https://host/path/to/cover.jpg",
  "lyrics": "متن ترانه",
  "hq": "https://host/highquality.m4a",
  "lq": "https://host/lowquality.m4a",
  "selected": "https://host/highquality.m4a"
}
```

## لایسنس

MIT

---
</div>
