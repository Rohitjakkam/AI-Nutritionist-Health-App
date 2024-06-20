### AI Nutritionist Health App
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from langsmith import traceable

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Function to load Google Gemini Pro Vision API And get response
@traceable # Auto-trace this function
def get_gemini_repsonse(input_prompt,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
        
        

##initialize our streamlit app

st.set_page_config(page_title="AI Nutritionist Health App")

st.header("AI Nutritionist Health App")
# input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the total calories and Proteins")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories and proteins, also provide the details of every food items with calories and protein intake
               is below format

               1. Item 1 - no of calories and no of proteins
               2. Item 2 - no of calories and no of proteins
               ----
               ----
        Finally you can also mention whether the food is healthy or not and also
        mention the 
        percentage split of the ratio of carbohydrates, fats, proteins, fibers, sugar and 
        other important things required in our diet 
        try to give some tips to imporve food or appreciate if the healthy food 


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)

