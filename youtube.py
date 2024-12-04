from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def clean_url(url):
    if "?" in url:
        return url.split("?")[0]
    return url

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Your video was downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    video_url = clean_url(video_url)
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
