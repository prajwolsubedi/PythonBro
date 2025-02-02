import os
import vlc
import time
import threading

# Specify the folder containing videos
folder_path = r"C:\Users\Prajwol\Desktop\100DaysPythonh\27"

# Get a list of all .mp4 files in the folder
mp4_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.mp4')]

# Check if any .mp4 files are present
if not mp4_files:
    print("No MP4 files found in the directory.")
    exit()

# Initialize VLC player
player = vlc.MediaPlayer()

# Set playback speed
player.set_rate(2.0)

# Function to handle user input for skipping videos
def monitor_input(skip_flag):
    while True:
        user_input = input("Press 's' to skip the current video: ").strip().lower()
        if user_input == 's':
            skip_flag['skip'] = True

# Start a separate thread to listen for user input
skip_flag = {'skip': False}
input_thread = threading.Thread(target=monitor_input, args=(skip_flag,), daemon=True)
input_thread.start()

# Play each file
for video in mp4_files:
    print(f"Playing: {video}")
    media = vlc.Media(video)
    player.set_media(media)
    player.play()

    # Wait until the current video ends or skip is triggered
    time.sleep(2)  # Give the player time to start
    while player.is_playing():
        if skip_flag['skip']:
            print("Skipping the current video...")
            skip_flag['skip'] = False
            break
        time.sleep(1)

print("Finished playing all videos.")
