import cv2
import streamlit as st
import numpy as np
from PIL import Image

def capture_video():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return


    st.title("Live Video Stream")
    video_container = st.empty()  

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            st.error("Error: Failed to capture frame.")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PIL Image for Streamlit
        image = Image.fromarray(frame_rgb)

        # Display the image in the Streamlit app
        video_container.image(image, use_container_width=True)  # Use the new parameter

        # Stop video capture if user presses 'q' on the keyboard
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()

# Start the video capture when the app is loaded
if __name__ == "__main__":
    capture_video()
