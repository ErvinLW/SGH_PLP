# STEAMLIT TEXT SUMMARISATION WITH T5 APP

# Import libraries
import torch
import streamlit as st
from PIL import Image
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Inserting SGH corporate logo
image = Image.open('SGH.png')

# Displaying the image on streamlit app and defining title settings
col1, col2, col3 = st.columns(3)
logo = col1.image(image, use_column_width=True)

st.title('Article Summarization Demo')
st.markdown('Using Finetuned T5 model for Abstractive Text Summarization')

# Define default parameters for T5 model
_num_beams = 4
_no_repeat_ngram_size = 2
_length_penalty = 3
_max_length = 300
_min_length = 50
_early_stopping = True

col1, col2, col3 = st.columns(3)
expander1 = col1.expander("Number of Beams")
expander1.write("""
Sets the number of possible word sequence "paths" to consider and picks the best one by average sequence probability.

Reduces the risk of missing out important words that could be missed if we only predict one word at a time. 
""")

expander2 = col2.expander("Length Penalty")
expander2.write("""
Controls how long a generated sentence can be. 

A length penalty of > 0 promotes longer sentences, while a length penalty of < 0 promotes shorter sentences.
""")

expander3 = col3.expander("Max Length")
expander3.write("""
The maximum length the generated text can have.

Recommended to keep between 300-450.
""")

col1, col2, col3 = st.columns(3)
_num_beams = col1.number_input("Number of Beams", value=_num_beams)
# _no_repeat_ngram_size = col2.number_input("no_repeat_ngram_size", value=_no_repeat_ngram_size)
_length_penalty = col2.number_input("Length Penalty", value=_length_penalty)
_max_length = col3.number_input("Max Length", value=_max_length)

text = st.text_area('Text Input') # Create a field for input text

def run_model(input_text):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    t5_model = T5ForConditionalGeneration.from_pretrained("./SGH_FinetunedT5Model") # Amend filepath accordingly
    t5_tokenizer = T5Tokenizer.from_pretrained("t5-base",  model_max_length=1000)

    # Tokenize and pre-process the input text
    input_text = str(input_text).replace('\n', '')
    input_text = ' '.join(input_text.split())
    input_tokenized = t5_tokenizer.encode(input_text, truncation=True ,return_tensors="pt").to(device)
    summary_task = torch.tensor([[21603, 10]]).to(device)
    input_tokenized = torch.cat([summary_task, input_tokenized], dim=-1).to(device)
    summary_ids = t5_model.generate(input_tokenized,
                                    num_beams=_num_beams,
                                    no_repeat_ngram_size=_no_repeat_ngram_size,
                                    length_penalty=_length_penalty,
                                    min_length=_min_length,
                                    max_length=_max_length,
                                    early_stopping=_early_stopping)
    output = [t5_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    st.write('Summary')
    st.success(output[0])

if st.button('Submit'):
    run_model(text)