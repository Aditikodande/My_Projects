
import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Define language codes for supported languages
LANGUAGES = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Italian': 'it',
    # Add more languages if needed
}

# Initialize the model and tokenizer
def get_model_and_tokenizer(source_lang_code, target_lang_code):
    model_name = f'Helsinki-NLP/opus-mt-{source_lang_code}-{target_lang_code}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Streamlit UI
st.title("Language Translation App")

# Select source and target languages (display language names)
source_language = st.selectbox('Select source language', list(LANGUAGES.keys()))
target_language = st.selectbox('Select target language', list(LANGUAGES.keys()))

# Input sentence for translation
sentence = st.text_area("Enter a sentence to translate:")

if sentence:
    # Get the language codes for source and target languages
    source_lang_code = LANGUAGES[source_language]
    target_lang_code = LANGUAGES[target_language]
    
    # Initialize the model and tokenizer
    model, tokenizer = get_model_and_tokenizer(source_lang_code, target_lang_code)

    # Tokenize and translate
    translated = model.generate(**tokenizer(sentence, return_tensors="pt", padding=True, truncation=True))
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    # Display the translated sentence
    st.write(f"Translated sentence: {translated_text}")
