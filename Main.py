# Import python packages
import streamlit as st
import pandas as pd
import json
import spacy
 

VAGUE_WORDS = {
    "thing","stuff","kinda","sorta","maybe","approximately","around","somehow",
    "really","very","literally","basically","just","nice","cool","okay","ok",
    "like"  
}


def countable_words(text):
    return [t for t in text if t.is_alpha or t.is_digit]

def I1_Lexical_richness(text):
    """Returns the lexical richness of the text"""
    return len(countable_words(text)) / len(text)


def I2_Lexical_Precision(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    for t in doc:
        print(t.pos_, t.lemma_)


I2_Lexical_Precision("He read fast")


st.title(f"Streamlit App")
  
user = st.user
 

# Use an interactive slider to get user input
st.subheader(f"Welcome {user}")

 


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None: 

    DATA =  json.loads(uploaded_file.getvalue().decode("utf-8")) 
  
    for conv in DATA:
        st.write(conv["title"])
        for message in conv["messages"]:
            st.write(message["role"])
            st.write(message["content"])
  

 