Spotify Tag Remover
Spotify Tag Remover is a simple utility built to clean up and standardize the metadata on audio files downloaded from Spotify or Spotify-based sources.

It automatically strips out the junk—like promotional text, website names, and platform-specific tagging—so your music library stays tidy and organized.

Features
The tool is designed to be straightforward and effective:

Cleans unwanted tags: It scrubs away platform names (like Spotify or Spotiflyer), website URLs, and unnecessary bracketed text or prefixes.

Format support: It works with common audio formats including MP3, FLAC, WAV, and M4A.

Batch processing: You can point it at an entire folder to clean multiple files at once.

Safe cleaning: While it removes the clutter, it carefully preserves the metadata you actually want, such as the Title, Artist, Album, and Track number.

Tech Stack
The project is written in Python. It relies primarily on the mutagen library to read and edit audio metadata, along with standard libraries for file and path handling.

Project Structure
Here is a quick look at how the files are organized:

Plaintext

spotify-tag-remover/
│
├── main.py              # Entry point
├── cleaner.py           # Core tag-cleaning logic
├── utils.py             # Helper functions
├── requirements.txt     # Dependencies
├── .gitignore
└── README.md
