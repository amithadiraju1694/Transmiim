
import numpy as np
from typing import List, Tuple, Optional, AnyStr
import nltk
nltk.download("stopwords")
nltk.download('punkt')

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re


def preprocess_text(sentence: AnyStr) -> AnyStr:
    sentence=sentence.lower().replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)

    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')

    tokens = tokenizer.tokenize(rem_num)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
    
    return_txt = " ".join(filtered_words)

    return return_txt

def image_to_np_arr(image) -> np.array:
    return np.array(image)

def process_extracted_text(raw_extrc_text: List[Tuple]) -> List[AnyStr]:
    
    output_texts = []
    for _, extr_text, _ in raw_extrc_text:
        # remove all numbers, special characters from a string
        prcsd_txt = preprocess_text(extr_text)

        if len(prcsd_txt) > 2: output_texts.append(prcsd_txt)
    
    return output_texts