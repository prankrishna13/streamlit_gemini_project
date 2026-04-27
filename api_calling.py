from google import genai
from dotenv import load_dotenv
import os
import streamlit as st 
import io
from gtts import gTTS 

# loading the environment

load_dotenv()

my_api_key= os.getenv("GEMINI_API_KEY")

# initializing a clint

client = genai.Client(api_key = my_api_key)



# note genaretor

def note_generator(img):

    prompt = """You are an expert IELTS Tutor. Analyze the uploaded image(s) and generate a comprehensive study note in English.
The note must include:
1. Summary: A brief overview of the content in English, followed by a 2-line summary in Bengali.
2. Key Vocabulary: Extract 5-8 academic words. For each word, provide:
   - Meaning in English
   - Meaning in Bengali
   - A sample sentence related to IELTS.
3. Grammar & Structure: Highlight any complex sentence structures found in the text (like Passive Voice or Conditionals) and explain them briefly.
4. Tips: Give one IELTS-specific tip (Reading or Writing) based on this content.

Use clear Markdown headings and bullet points."""

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents= [img,prompt]
    )
    return response.text

# Audio genaretor
def audio_transcription(text):
    speech = gTTS(text,lang='bn',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(img,difficulty):

    prompt = f"Based on the provided image(s), create an IELTS-style practice quiz. The difficulty level is: {difficulty}.
The quiz should contain:
1. 3 Multiple Choice Questions (MCQs) focusing on the main ideas.
2. 2 'Fill in the blanks' using words from the text to test vocabulary.
3. 1 'True/False/Not Given' question to practice IELTS Reading logic.

Instructions:
- Write the questions and options in English.
- After each question, provide a 'Hint' in Bengali to help the student think.
- At the very bottom, provide an 'Answer Key' with brief explanations in both English and Bengali."

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents= [img,prompt]
    )
    return response.text
