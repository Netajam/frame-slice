import sys
import os
from slice_scene import slice_scene
from slice_interval import slice_interval

def process_videos_in_folder(mode, folder_path, output_folder, param):
    # Get all video files in the folder
    video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        video_name, _ = os.path.splitext(video_file)  # Get the video name without extension
        prefix = f"{video_name}_"
        
        if mode == 'interval':
            slice_interval(video_path, output_folder, int(param), prefix)
        elif mode == 'scene':
            slice_scene(video_path, output_folder, param, prefix)
        else:
            print(f"Invalid mode. Choose 'interval' or 'scene' for video: {video_file}")
            sys.exit(1)

def main():
    if len(sys.argv) != 5:
        print("Usage: python frame_slice.py <mode> <folder_path> <output_folder> <threshold_or_interval>")
        print("Modes: interval, scene")
        sys.exit(1)

    mode = sys.argv[1]
    folder_path = sys.argv[2]
    output_folder = sys.argv[3]
    param = float(sys.argv[4])

    # Check if the provided folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The provided folder path '{folder_path}' is not a valid directory.")
        sys.exit(1)
    
    process_videos_in_folder(mode, folder_path, output_folder, param)
 
if __name__ == '__main__':
    main()