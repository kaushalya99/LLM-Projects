from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

#Inititalize your image generation client
client=OpenAI(api_key=apikey)

single_img=dict(
       title="",
       text="",
       interval=None,
       img="",
    )

def generate_image(img_description, num_images):
    
    image_gallery=[]
    for i in range(num_images):
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=img_description,
            size="1792x1024",
            quality="standard",
            n=1
        )
        image_url = img_response.data[0].url
        new_image=single_img.copy()
        new_image["title"]=f"Image {i+1}"
        new_image["text"]=img_description
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery

st.set_page_config(page_title="Image Generator", page_icon="🎨", layout="wide")
st.title("🎨Image Generator Tool")

#create subheader

st.subheader("Generate Images with OpenAI's DALL-E")
img_description = st.text_input("🔍 Enter a description for the image you want to generate")
num_of_images = st.number_input("🖼️ Select the number of images to generate", min_value=1, max_value=5, value=1)

#Create a button to generate the image

if st.button("Generate Image"):
    generate_image=generate_image(img_description, num_of_images)
    
    carousel(items=generate_image,width=1)
    
