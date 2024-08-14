import cv2
import os
from tkinter import filedialog
import streamlit as st

st.title("Selfie App")

# Ensure the camera is initiated only once
if "camera" not in st.session_state:
    st.session_state["camera"] = cv2.VideoCapture(0)

FRAME_WINDOW = st.image([])

image, frame = st.session_state["camera"].read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
FRAME_WINDOW.image([frame])


# Button to take a picture
if st.button("Take picture", key="take_picture"):
    image, frame = st.session_state["camera"].read()
    if image:
        # Ask user for a photo name using Streamlit's text input
        photo_name = st.text_input("Enter the photo name:")

        # Display the image in the Streamlit app
        st.image(frame, channels="BGR", caption=photo_name)

        # Ask for the directory to save the image
        save_file = filedialog.askdirectory(title="Select folder to save the photo")
        save_path = os.path.join(save_file, f"{photo_name}.png")

        # Save the image using OpenCV
        cv2.imwrite(save_path, frame)
        st.success(f"Photo saved at: {save_path}")
    else:
        st.error("Failed to capture image")

# Button to turn off the camera
if st.button("Turn off", key="turn_off"):
    st.session_state["camera"].release()
    cv2.destroyAllWindows()
    st.success("Camera turned off.")
