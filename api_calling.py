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

    prompt = """Summarize the picture in note format at max 250 words,
      make sure to add necessay markdown to differentiat different section . explain in bangla"""

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

    prompt = f"Generate 5 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options and add correct answer also,after the quiz, language will be bangla"

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents= [img,prompt]
    )
    return response.text