import os
import subprocess

# Specify the folder containing videos
folder_path = r"C:\Users\Prajwol\Desktop\100DaysPythonh\27"

# Get a list of all .mp4 files in the folder
mp4_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.mp4')]

# Check if any .mp4 files are present
if not mp4_files:
    print("No MP4 files found in the directory.")
    exit()

# VLC executable path (update this if VLC is installed in a different location)
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

# Add command-line arguments to maintain window size and play videos sequentially
vlc_command = [
    vlc_path,
    "--playlist-enqueue",      # Enqueue all files into a playlist
    "--no-qt-privacy-ask",     # Suppress privacy prompts
    "--no-qt-error-dialogs",   # Suppress error dialogs
    "--loop"                   # Loop the playlist (optional, remove if not needed)
] + mp4_files

# Launch VLC with the playlist
print("Playing all videos in VLC...")
subprocess.run(vlc_command)
