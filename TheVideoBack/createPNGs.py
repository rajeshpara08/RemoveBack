import cv2

# Function to extract frames from video and save as PNG images
def extract_frames(video_path, output_dir, fps=24):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    # Set frame rate for extraction
    if fps <= 0 or fps > frame_rate:
        fps = frame_rate

    # Calculate frame interval
    interval = int(frame_rate / fps)

    # Initialize frame counter
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Check if it's time to extract frame based on interval
        if frame_count % interval == 0:
            # Save frame as PNG image
            frame_filename = f"{output_dir}/frame_{frame_count}.png"
            cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release video capture object
    cap.release()

    print(f"Frames extracted: {frame_count} / {total_frames}")

# Example usage
video_path = "E:/RemoveBack/TheVideoBack/Video/Input/Benefits.mp4"
output_dir = "E:/RemoveBack/TheVideoBack/Video/Output"
extract_frames(video_path, output_dir)
