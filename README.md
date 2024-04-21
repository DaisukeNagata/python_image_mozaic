# Intoroduce
The application allows you to set a mosaic area.

Here is a Python code snippet with comments that applies a mosaic effect to specific regions of a video.
It uses the VideoFileClip class from the MoviePy library to read a video file and the cv2 library (OpenCV) to perform image manipulations.
The code applies a mosaic effect to two different regions in the video frame and then saves the modified video with audio:




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
    
# Example

<div align="center">
<img src="https://github.com/DaisukeNagata/python_image_mozaic/assets/16457165/97ed101a-87e7-46a0-9e00-8f434d70a068">
</div>










