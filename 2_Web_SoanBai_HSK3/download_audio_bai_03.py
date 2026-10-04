# -*- coding: utf-8 -*-
import os, sys, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

AUDIO_FILES = {
    "03-1.mp3": "1bytyqpLa1RDY4npzYTezBKnRum0kjcgp",
    "03-2.mp3": "106MxYOJrmQJEF4w9E1gDa9D5xtlRopLx",
    "03-3.mp3": "1ZFMwbKOTYssxYkl0tBtySMx4giAL2Hk9",
    "03-4.mp3": "1N-z18dMS86JedUnIjTD7LevALkb8e_Uu",
    "03-5.mp3": "1yZSJdXGSgC1AIhmmSbEnvH4CqhDyTj7p"
}

target_dir = os.path.join("2_Web_SoanBai_HSK3", "audio_textbook", "Bai_03")
os.makedirs(target_dir, exist_ok=True)

for fname, file_id in AUDIO_FILES.items():
    dest = os.path.join(target_dir, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f"Already exists: {dest} ({os.path.getsize(dest)} bytes)")
        continue
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"Downloading {fname} from Google Drive...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(dest, 'wb') as f:
        f.write(data)
    print(f"Saved {dest} ({len(data)} bytes)")

print("\n✅ All Lesson 3 Textbook audio files downloaded successfully!")
