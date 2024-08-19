import streamlit as st
from inference.translate import translate_image
from PIL import Image


# Streamlit app
st.title("Image Upload and Processing")


# Streamlit function to upload an image from any device
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


# Submit button
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Only show if user wants to see
    if st.checkbox('Show Uploaded Image'):
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Submit button
    if st.button("Submit"):

        # Call the translate_image function
        processed_image = translate_image(image)
        
        # Display a success message
        st.success("Image processed successfully! , It's shape: {}".format(processed_image.shape) )
