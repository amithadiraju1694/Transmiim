import pandas as pd
import transformers
import torch
from transformers import AutoTokenizer

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="cpu",
)

dataset = pd.read_csv('/Users/amithadiraju/Desktop/Transmiim_Imgs/menu_item_exp_eng.csv',
                         header=0)

def make_prompt(dataset, context_indices, text_to_summarize):

    prompt = 'Given the item and its explanation like below-> '
    for index in context_indices:
        item = dataset.iloc[[index]]['item'].values[0]
        explanation = dataset.iloc[[index]]['explanation'].values[0]
        
        # The stop sequence '{summary}\n\n\n' is important for FLAN-T5. Other models may have their own preferred stop sequence.
        prompt += f"""
                    Item:
                        {item}

                    Explanation:
                        {explanation}


                    """
    
    
    prompt += "Explain the below item similarly-> "
    prompt += f"""
                    Item:
                        {text_to_summarize}

                    Explanation:
                    """
        
    return prompt

indices = [0,1,2]
text_to_summarize = "bisibella bath"

input_prompt = make_prompt(dataset = dataset,
                           context_indices=indices,
                           text_to_summarize=text_to_summarize
                           )


sequences = pipeline(
    input_prompt,
    do_sample=True,
    top_k=30,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=1024,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")