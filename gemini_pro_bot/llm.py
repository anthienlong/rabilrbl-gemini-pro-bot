import os
import google.generativeai as genai
from google.generativeai.types.safety_types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

load_dotenv()

# Disable all safety filters
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
}


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-1.5-pro-exp-0827", safety_settings=SAFETY_SETTINGS, system_instruction="Your name is Jarviss, you are a Pro Sales with 10 years as CEO, you have a strong skill in individual consulting and excel in creating reports, plans, and sales and marketing strategies.",
                             generation_config = {
                              "temperature": 1,
                              "top_p": 0.95,
                              "top_k": 64,
                              "max_output_tokens": 8192,
                                })
img_model = genai.GenerativeModel("gemini-1.5-flash", safety_settings=SAFETY_SETTINGS)
