import streamlit as st
from inference.translate import extract_filter_img, transcribe_menu_model
from PIL import Image
import easyocr
import time 

# Streamlit app
st.title("Image Upload and Processing")


# Using open source text detector & extractor
text_extractor = easyocr.Reader(['en'], gpu=False)

# Streamlit function to upload an image from any device
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

DEBUG_MODE = True


# Submit button
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Only show if user wants to see
    if st.checkbox('Show Uploaded Image'):
        st.image(image,
                 caption='Uploaded Image',
                 use_column_width=True)

    # Submit button
    if st.button("Submit"):

        
        st_filter = time.perf_counter()
        # Call the extract_filter_img function
        filtered_text = extract_filter_img(image, text_extractor)
        en_filter = time.perf_counter()

        st_trans_llm = time.perf_counter()
        translated_text_dict = transcribe_menu_model(menu_texts=filtered_text)
        en_trans_llm = time.perf_counter()

        st.success("Image processed successfully! " )

        if DEBUG_MODE:
            filter_time_sec = en_filter - st_filter
            llm_time_sec = en_trans_llm - st_trans_llm
            total_time_sec = filter_time_sec + llm_time_sec
            
            st.write("Time took to extract and filter text {}".format(filter_time_sec))
            st.write("Time took to summarize by LLM {}".format(llm_time_sec))
            st.write('Overall time taken in seconds: {}'.format(total_time_sec))
        
        st.table(translated_text_dict)
        
