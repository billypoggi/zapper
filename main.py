import cv2
import os

def play_video(video_path):
    """
    Plays a video file from the given path.
    Press 'q' to quit the video playback.
    """
    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at '{video_path}'")
        return

    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # 1. Create a named window
    window_name = 'Video Player'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)

    # 2. Set the window to full screen
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                                                                                      
    # Get the video's frames per second (fps) to control playback speed
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_time = int(1000 / fps) # The wait time between frames in milliseconds

    print("Playing video... Press 'q' to quit.")

    # Read and display frames until the video is over or the user quits
    while cap.isOpened():
        # 'ret' is a boolean that is False if no frame was read (end of video)
        # 'frame' is the actual video frame (an image)
        ret, frame = cap.read()

        if ret:
            # Display the frame in a window named 'Video Player'
            cv2.imshow('Video Player', frame)

            # Wait for 'wait_time' milliseconds and check for key press
            # Press 'q' to exit the loop
            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break
        else:
            # End of video
            break

    # Release the VideoCapture object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
    print("Video finished.")

if __name__ == '__main__':
    while True:
    # Get the video file path from the user
        print ("Hello world")
        path = input("Enter the full path to the video file: ")
#       path = "./testvid.mp4" #("Enter the full path to the video file: ")
        play_video(path)
        print ("doneski")

# small final update
