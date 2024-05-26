import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove Background from your Image")
st.write(
    ":dog: Try uploading an image to magically remove the background. :grin:"
)

st.sidebar.write("## Upload and Download :gear:")

MAX_FILE_SIZE = 5*1024*1024 # 5 MB

# Download the fixed image

def convert_image(img):
  buf = BytesIO()
  img.save(buf, format="PNG")
  byte_img = buf.getvalue()
  return byte_img

# Upload an image

def fix_image(upload):
  image = Image.open(upload)
  col1.write("Original Image :camera:")
  col1.image(image)

  fixed = remove(image)
  col2.write("Fixed Image :wrench:")
  col2.image(fixed)
  st.sidebar.markdown("\n")
  st.sidebar.download_button("Download the Fixed Image", convert_image(fixed), "fixed.png", "image/png")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
  if my_upload.size > MAX_FILE_SIZE:
    st.error("The uploaded image is too large. Please upload an image smaller than 5 MB.")
  else:
    fix_image(upload=my_upload)
else:
  fix_image("./zenitsu.jpeg")