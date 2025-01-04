import yt_dlp
import os


def download_youtube_to_mp3(youtube_url, output_folder="downloads"):
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

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        mp3_file_path = ydl.prepare_filename(info).replace(".webm", ".mp3")

    print(f"MP3 file saved as: {mp3_file_path}")


youtube_url = input("Enter link from yt: ")
download_youtube_to_mp3(youtube_url)