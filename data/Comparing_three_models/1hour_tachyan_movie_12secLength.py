import cv2
import os

# Directory containing the JPEG images
image_dir = 'F:/1hr_tachyan'

# Desired length of the video in seconds
desired_length_seconds = 12

# Define the frame rate of the output video (frames per second)
frame_rate = 24

# Calculate the total number of frames needed
total_frames_desired = frame_rate * desired_length_seconds

# Get the list of JPEG files in the directory
image_files = [img for img in os.listdir(image_dir) if img.endswith(".jpg")]

# Sort the image files by name (assuming the naming convention is sequential)
image_files.sort()

# Calculate the stride for selecting frames
stride = len(image_files) // total_frames_desired

# Select frames with the calculated stride
selected_images = image_files[::stride]

# Determine the dimensions of the images
first_image = cv2.imread(os.path.join(image_dir, selected_images[0]))
height, width, _ = first_image.shape

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to change the codec based on your system and preferences
output_video = cv2.VideoWriter('C:/Users/samir/Desktop/1hr_Video.mp4', fourcc, frame_rate, (width, height))

# Keep track of the number of frames written to the video
frames_written = 0

# Iterate through each selected image and write it to the video
for image_file in selected_images:
    image_path = os.path.join(image_dir, image_file)
    frame = cv2.imread(image_path)
    output_video.write(frame)

    # Update the count of frames written
    frames_written += 1

    # Break the loop if we have written the desired number of frames
    if frames_written >= total_frames_desired:
        break

# Release the VideoWriter object
output_video.release()

print("Video creation complete.")
