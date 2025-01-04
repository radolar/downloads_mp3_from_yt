import yt_dlp
import os

def download_youtube_to_mp3(youtube_urls, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    # Loop through each URL in the list
    for youtube_url in youtube_urls:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                mp3_file_path = ydl.prepare_filename(info).replace(".webm", ".mp3")
            print(f"MP3 file saved as: {mp3_file_path}")
        except Exception as e:
            print(f"Failed to download {youtube_url}: {e}")

# Example usage
youtube_urls = [
    "https://www.youtube.com/watch?v=example1",
    "https://www.youtube.com/watch?v=example2",
    "https://www.youtube.com/watch?v=example3"
]
download_youtube_to_mp3(youtube_urls)