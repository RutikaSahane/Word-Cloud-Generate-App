from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import streamlit as st 
import pandas as pd
from io import BytesIO

# Set page configuration
st.set_page_config(layout="wide")

# Background image CSS
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGrYwwrm__IvbiPWDYBlHgi1ldc0rkGFh9uQ&s");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
'''

# Load the CSS in Streamlit
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    "<h1 style='color: #181616;'> Word Cloud Generate App</h1>",
    unsafe_allow_html=True
)


st.markdown(
    "<h3 style='color:#FFFFFF;'>Enter text to generate a word cloud. Adjust settings as needed and click **Generate**.</h3>",
    unsafe_allow_html=True
)




#input text
text = st.text_area("Enter the Text Here")

# Size options
st.sidebar.header("Word Cloud Settings")
width = st.sidebar.slider("Width", 400, 1000, 800)  # Width of the word cloud image
height = st.sidebar.slider("Height", 200, 800, 400)  # Height of the word cloud image
max_font_size = st.sidebar.slider("Max Font Size", 10, 150, 50)  # Maximum font size
background_color = st.sidebar.color_picker("Background Color", "#ffffff")  # Background color picker



#generate wordcloud
if st.button("Generate Word Cloud"):
    
    wordcloud = WordCloud(width=width,height=height,margin=0,max_font_size=max_font_size,background_color=background_color).generate(text)


    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud ,interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
    
    
    #Saving the image
    buffer = BytesIO()
    wordcloud.to_image().save(buffer,format="PNG")
    buffer.seek(0)
    
    #download the image
    st.download_button(
        label="Download Image",
        data=buffer,file_name="word_cloud.png",
        mime="image/png"
    )
 
    