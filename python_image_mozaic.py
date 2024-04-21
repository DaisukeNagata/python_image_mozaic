from moviepy.editor import VideoFileClip
import cv2  # Using OpenCV to apply mosaic effect
import numpy as np

# Read the video file
video_path = "/path/to/your/video/example.mp4"  # Updated path example
clip = VideoFileClip(video_path)

# Function to apply mosaic effect
def mosaic_effect(get_frame, t):
    frame = get_frame(t).copy()  # Copy the frame

    # First mosaic position
    x1_1, y1_1 = 100, 50  # Top-left corner of the mosaic
    x2_1, y2_1 = 150, 100  # Bottom-right corner of the mosaic
    mosaic_region_1 = frame[y1_1:y2_1, x1_1:x2_1]  # Region to be mosaiced
    mosaic_region_1 = cv2.resize(mosaic_region_1, (10, 10), interpolation=cv2.INTER_NEAREST)  # Apply mosaic effect
    mosaic_region_1 = cv2.resize(mosaic_region_1, (x2_1 - x1_1, y2_1 - y1_1), interpolation=cv2.INTER_NEAREST)  # Resize back to original size
    frame[y1_1:y2_1, x1_1:x2_1] = mosaic_region_1  # Put the mosaic region back into the frame

    # Second mosaic position
    x1_2, y1_2 = 300, 50  # Top-left corner of the second mosaic
    x2_2, y2_2 = 350, 100  # Bottom-right corner of the second mosaic
    mosaic_region_2 = frame[y1_2:y2_2, x1_2:x2_2]  # Second region to be mosaiced
    mosaic_region_2 = cv2.resize(mosaic_region_2, (10, 10), interpolation=cv2.INTER_NEAREST)  # Apply mosaic effect
    mosaic_region_2 = cv2.resize(mosaic_region_2, (x2_2 - x1_2, y2_2 - y1_2), interpolation=cv2.INTER_NEAREST)  # Resize back to original size
    frame[y1_2:y2_2, x1_2:x2_2] = mosaic_region_2  # Put the second mosaic region back into the frame

    return frame

# Create a clip with the mosaic effect
mosaic_clip = clip.fl(mosaic_effect)

# Output file
output_path = "/path/to/your/output/output_with_mosaic.mp4"  # Example output path
mosaic_clip.write_videofile(output_path, audio_codec='aac')  # Save with audio
