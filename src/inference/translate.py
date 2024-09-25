import streamlit as st

from inference.preprocess_image import (
    image_to_np_arr,
    process_extracted_text
)

from inference.config import INSTRUCTION_PROMPT, DEVICE
from typing import List, Tuple, Optional, AnyStr, Dict
from transformers import T5Tokenizer, T5ForConditionalGeneration
import easyocr
import time

use_gpu = True
if DEVICE == 'cpu': use_gpu = False


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

    progress_bar.empty()
    status_message.empty()
    return result


def transcribe_menu_model(menu_texts: List[AnyStr],
                          text_summarizer = None,
                          text_tokenizer = None) -> Dict:

    summarized_menu_items = {}

    for mi in menu_texts:
        if not text_summarizer:
            raise NotImplementedError(""" """)
        
        else:
            prompt_item = INSTRUCTION_PROMPT + " " + mi + """


"""
            input_ids = text_tokenizer(prompt_item, return_tensors="pt").input_ids
            
            outputs = text_summarizer.generate(input_ids,
                                               max_new_tokens = 512
                                               )
            
            summarized_menu_items[mi] = text_tokenizer.decode(
                outputs[0],
                skip_special_tokens = True
                )
    
    return summarized_menu_items

def load_models(item_summarizer: AnyStr) -> Tuple:
    text_extractor = easyocr.Reader(['en'],
                                    gpu = use_gpu
                                    )
    tokenizer = T5Tokenizer.from_pretrained(item_summarizer)
    model = T5ForConditionalGeneration.from_pretrained(item_summarizer)

    return (text_extractor, tokenizer, model)

def classify_menu_text(extrc_str: List[AnyStr]) -> List[AnyStr]:
    return extrc_str

