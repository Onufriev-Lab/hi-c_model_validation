
import cv2
import os

# Directory containing the JPEG images
image_dir = 'C:/Users/samir/Desktop/movie/11hr_new_transcription'

#image_dir = 'C:/Users/samir/Desktop/selected_images'


# Define the frame rate of the output video (frames per second)
frame_rate = 24

# Get the list of JPEG files in the directory
image_files = [img for img in os.listdir(image_dir) if img.endswith(".jpg")]

# Sort the image files by name (assuming the naming convention is sequential)
image_files.sort()

# Select one image for every 100 files from the beginning
selected_images = image_files[::2]

# Determine the dimensions of the images
first_image = cv2.imread(os.path.join(image_dir, selected_images[0]))
height, width, _ = first_image.shape

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to change the codec based on your system and preferences
output_video = cv2.VideoWriter('C:/Users/samir/Desktop/1min_cpk_Video.mp4', fourcc, frame_rate, (width, height))

# Iterate through each selected image and write it to the video
counter = 0 
for image_file in selected_images:
    counter+=1
    if counter % 100 ==0:
        print("\n" ,counter)
    image_path = os.path.join(image_dir, image_file)
    frame = cv2.imread(image_path)
    output_video.write(frame)

# Release the VideoWriter object
output_video.release()

print("Video creation complete.")



# import cv2
# import os

# # Directory containing the JPEG images
# image_dir = 'F:/1hr_new/1hr_biological_time_new'

# # Define the frame rate of the output video (frames per second)
# frame_rate = 30

# # Get the list of JPEG files in the directory
# image_files = [img for img in os.listdir(image_dir) if img.endswith(".jpg")]

# # Sort the image files by name (assuming the naming convention is sequential)
# image_files.sort()

# # Determine the dimensions of the images
# img = cv2.imread(os.path.join(image_dir, image_files[0]))
# height, width, _ = img.shape

# # Reduce resolution to fit within 25MB limit
# max_width = 640
# max_height = 480
# if width > max_width or height > max_height:
#     scale = min(max_width / width, max_height / height)
#     width = int(width * scale)
#     height = int(height * scale)

# # Define the video codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to change the codec based on your system and preferences
# output_video = cv2.VideoWriter('C:/Users/samir/Desktop/output_Video.mp4', fourcc, frame_rate, (width, height))

# # Iterate through each image and write it to the video
# counter =0
# for image_file in image_files:
#     counter+=1
#     image_path = os.path.join(image_dir, image_file)
#     frame = cv2.imread(image_path)
#     frame = cv2.resize(frame, (width, height))  # Resize the frame if necessary
#     output_video.write(frame)

# # Release the VideoWriter object
# output_video.release()

# print("Video creation complete.")






