# 🪐 APOD Desktop Wallpaper - COMP 593 Final Project

This Python project downloads NASA's **Astronomy Picture of the Day (APOD)** for a given date and sets it as your Windows desktop background.  
It also saves the image and related metadata to a local SQLite database and avoids duplicate downloads by comparing image hashes.

---

## 🚀 Features

- Accepts a specific APOD date (YYYY-MM-DD) as a command-line argument
- Validates date format and range (not before 1995-06-16, not in the future)
- Fetches APOD info using NASA's official API
- Downloads HD image or video thumbnail
- Caches images locally with clean filenames
- Prevents duplicate downloads using SHA-256 hash
- Stores APOD title, explanation, path, and hash in a local SQLite database
- Sets the downloaded image as the desktop wallpaper (Windows only)

---

# Install dependencies if needed:

```bash
pip install requests
```

# For Usage

- Make a .env file, and add the API_KEY=<YOUR_API_KEY_HERE_FROM_NASA>

- Run the script: python apod_desktop.py [apod_date], [apod_date] being in the format YYYY-MM-DD
