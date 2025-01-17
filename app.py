import streamlit as st
from PyPDF2 import PdfReader
from pytesseract import image_to_string
from PIL import Image
import os

st.title("Social Media Content Analyzer")
st.subheader("Upload PDF or Image Files")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_image(file):
    image = Image.open(file)
    text = image_to_string(image)
    return text

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    else:
        extracted_text = extract_text_from_image(uploaded_file)

    st.write("Extracted Text:")
    st.text_area("", extracted_text, height=200)

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"


def suggest_improvements(text):
    suggestions = []
    if len(text.split()) < 50:
        suggestions.append("Consider adding more details to your content.")
    if not any(word.startswith("#") for word in text.split()):
        suggestions.append("Add relevant hashtags for better engagement.")
extracted_text=None

if extracted_text :
    sentiment = analyze_sentiment(extracted_text)
    st.write("Sentiment Analysis:", sentiment)

    suggestions = suggest_improvements(extracted_text)
    st.write("Engagement Suggestions:")
    for suggestion in suggestions:
        st.write("- ", suggestion)
