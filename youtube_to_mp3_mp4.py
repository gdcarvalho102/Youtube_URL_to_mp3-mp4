import os
os.system('pip install pytube')
import tkinter as tk
from tkinter import ttk
from pytube import YouTube



def download_media():
    url = url_entry.get()
    media_type = media_combobox.get().lower()
    output_folder = output_entry.get()

    if not output_folder:
        output_folder = os.path.join(os.path.expanduser('~'), 'Downloads', 'media')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    yt = YouTube(url)

    if media_type == 'audio':
        stream = yt.streams.filter(only_audio=True).first()
    elif media_type == 'video':
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    else:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

    stream.download(output_folder)
    result_label.config(text="Media downloaded successfully!")

# Create main application window
root = tk.Tk()
root.title("Media Downloader")

# URL entry
url_label = ttk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Media type selection
media_label = ttk.Label(root, text="Media Type:")
media_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

media_combobox = ttk.Combobox(root, values=["Audio", "Video", "Both"], state="readonly")
media_combobox.current(0)
media_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Output folder entry
output_label = ttk.Label(root, text="Output Folder:")
output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

output_entry = ttk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Download button
download_button = ttk.Button(root, text="Download", command=download_media)
download_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
