import streamlit as st

from inference.translate import (
    extract_filter_img,
    transcribe_menu_model,
    load_models
)

from inference.config import DEBUG_MODE
from PIL import Image
import time

# Streamlit app
st.title("Image Upload and Processing")


# Using open source text detector, LLM for explaining items
text_extractor, \
    item_tokenizer,item_summarizer = load_models(item_summarizer = "google/flan-t5-large")

# Streamlit function to upload an image from any device
uploaded_file = st.file_uploader("Choose an image...",
                                 type=["jpg", "jpeg", "png"])


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

        msg1 = st.empty()
        msg1.write("Pre-processing and extracting text out of your image ....")
        st_filter = time.perf_counter()
        # Call the extract_filter_img function
        filtered_text = extract_filter_img(image, text_extractor)
        en_filter = time.perf_counter()
        
        msg2 = st.empty()
        msg2.write("All pre-processing done, transcribing your menu items now ....")
        st_trans_llm = time.perf_counter()
        translated_text_dict = transcribe_menu_model(menu_texts=filtered_text,
                                                     text_tokenizer=item_tokenizer,
                                                     text_summarizer=item_summarizer
                                                    )
        
        msg3 = st.empty()                                            
        msg3.write("Done transcribing ... ")
        en_trans_llm = time.perf_counter()

        msg1.empty(); msg2.empty(); msg3.empty()
        st.success("Image processed successfully! " )

        if DEBUG_MODE:
            filter_time_sec = en_filter - st_filter
            llm_time_sec = en_trans_llm - st_trans_llm
            total_time_sec = filter_time_sec + llm_time_sec
            
            st.write("Time took to extract and filter text {}".format(filter_time_sec))
            st.write("Time took to summarize by LLM {}".format(llm_time_sec))
            st.write('Overall time taken in seconds: {}'.format(total_time_sec))
        
        st.table(translated_text_dict)
        
