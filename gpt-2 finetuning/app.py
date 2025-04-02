import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_path = "gpt2-story-finetuned"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def generate_story(prompt, genre, max_length, temperature, top_p, repetition_penalty):
    input_text = f"A {genre} story: {prompt}\n"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id  # Ensures the story stops at a logical ending
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Layout
st.set_page_config(layout="wide")

# Sidebar (Left - Parameters)
st.sidebar.header("Story Parameters")
max_length = st.sidebar.slider("Story Length", min_value=100, max_value=1000, value=600)
temperature = st.sidebar.slider("Creativity Level (Temperature)", min_value=0.5, max_value=1.5, value=1.0)
top_p = st.sidebar.slider("Diversity Level (Top-p Sampling)", min_value=0.5, max_value=1.0, value=0.9)
repetition_penalty = st.sidebar.slider("Repetition Penalty", min_value=1.0, max_value=2.0, value=1.2)

# Main Content (Middle - Genre, Input, and Output)
st.title("AI Story Generator")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    genre = st.selectbox("Choose a genre:", ["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Horror"])
    prompt = st.text_area("Enter a prompt for your story:", "A scientist activates a machine that lets them see five minutes into the future, but something looks back.")
    
    if st.button("Generate Story"):
        story = generate_story(prompt, genre, max_length, temperature, top_p, repetition_penalty)
        st.subheader("Generated Story:")
        st.write(story)
        
        # Download button with UTF-8 encoding fix
        st.download_button(label="Download Story", 
                           data=story.encode("utf-8", "ignore"),  # Ignore problematic characters
                           file_name="generated_story.txt", 
                           mime="text/plain")
