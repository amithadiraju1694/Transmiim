import streamlit as st
from inference.preprocess_image import image_to_np_arr

# Define your translate_image function
def translate_image(image):
    
    # Dummy function to simulate image translation
    st.write("Image has been processed.")
    
    # Return processed image array or any other output
    return image_to_np_arr(image)