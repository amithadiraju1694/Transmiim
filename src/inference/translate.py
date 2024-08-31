import streamlit as st

from inference.preprocess_image import (
    image_to_np_arr,
    process_extracted_text
)

import lorem
from typing import List, Tuple, Optional, AnyStr, Dict
import time

# Define your extract_filter_img function
def extract_filter_img(image, text_extractor) -> Dict:

    """
    1. Convert Image to numpy array
    2. Detect & Extract Text from Image - List of Tuples
    3. Process text , to filter out irrelevant text
    4. Classify only menu-related strings from detected text
    
    """
    
    progress_bar = st.progress(0)
    status_message = st.empty()

    functions_messages = [
        (image_to_np_arr, 'Converting Image to required format', 'Done Converting !'),
        (text_extractor.readtext, 'Extracting text from inp image', 'Done Extracting !'),
        (process_extracted_text, 'Clean Raw Extracted text', 'Done Cleaning !'),
        (classify_menu_text, 'Removing non-menu related text', 'Done removing !'),
    ]
    
    # Initialize variables
    result = image
    total_steps = len(functions_messages)
    ind_add_delays = [0, 2, 3, 4]

    # Loop through each function and execute it with status update
    for i, (func, start_message, end_message) in enumerate(functions_messages):
        status_message.write(start_message)

        if i in ind_add_delays:
            time.sleep(0.5)

        result = func(result)
        
        status_message.write(end_message)

        # Update the progress bar
        progress_bar.progress((i + 1) / total_steps)

        if i in ind_add_delays:
            time.sleep(0.5)

    return result


def transcribe_menu_model(menu_texts: List[AnyStr], text_summarizer = None) -> Dict:

    summarized_menu_items = {}

    for mi in menu_texts:
        # This will be replaced by a LLM model , to generate a 
        # meaningful summary
        if not text_summarizer:
            summarized_menu_items[mi] = lorem.sentence()
    
    return summarized_menu_items


def classify_menu_text(extrc_str: List[AnyStr]) -> List[AnyStr]:
    return extrc_str

