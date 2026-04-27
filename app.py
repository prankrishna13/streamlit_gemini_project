import streamlit as st 
from api_calling import note_generator , audio_transcription, quiz_generator
from PIL import Image
from google import genai 
 

st.markdown("<h1 style=' text-align: justify;  '>Your personal AI (MOON) <h1/> ", unsafe_allow_html=True)
# st.divider()
#st.caption("Illuminate your curiosity with Moon—your AI companion for coding, creativity, and cosmic insights.")


# side bar

with st.sidebar:
    st.logo("m.png")
    st.header("Control Panel")
    img = st.file_uploader(
        "Upload your photos",type=['jpg','png','jpeg'],
        accept_multiple_files=True
    )

    pil_list= []
    for i in img:
        pil_img = Image.open(i)
        pil_list.append(pil_img)


    # Image
    st.subheader("Your image")
    if img:
        if len(img)>3:
            st.error("upload only 3 photos")
        else:
            col = st.columns(len(img))
            for i,im in enumerate(img):
                with col[i]:
                     st.image(im)

    st.divider()

    option = st.selectbox("Difficultys",['Easy','Medium','Hard'],index=None)

    

    button = st.button("Upload",type="primary")   

 

#body------------------------------------------------------------------------------


if button:
    if not img:
        st.error("You must upload 1 photo")
    if not option:
        st.error("You mast select a difficult")


# for note
if img and option:

    with st.container(border=True):
         

         st.subheader("Your note")
         
         with st.spinner("AI is writing"):

              your_note = note_generator(pil_list)
              st.markdown(your_note)


#for audio

    with st.container(border=True):
        your_note= your_note.replace("#","")
        your_note= your_note.replace("*","")
        your_note= your_note.replace("-","")
        your_note= your_note.replace("'","")
        your_note= your_note.replace(",","")
        your_note= your_note.replace(":","")
        st.subheader("Audio ")

        with st.spinner("AI is writing"):
            au = audio_transcription(your_note)
            st.audio(au)        



# for quiz

    with st.container(border=True):
        st.subheader(f"Quiz with {option} Difficulty")
        with st.spinner("AI is writing"):
            try:
              qu = quiz_generator(pil_list, option)
              st.markdown(qu)
            except Exception as e:
                    st.error(f"Quiz Error: {e}")






st.text_input("",placeholder="Ask Moon (you can use it latter)")


# Footer 

# def add_footer():
#     footer_style = """
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #f1f1f1;
#         color: #555;
#         text-align: center;
#         padding: 1px;
#         font-size: 14px;
#         z-index: 100;
#     }
#     </style>
#     <div class="footer">
#         <p style='text-align: center;' >Made by Pran ❤️ using Streamlit</p>
#         <p style='text-align: center;' >Illuminate your curiosity with Moon—your AI companion for coding, creativity, and cosmic insights.</p>
#     </div>
#     """
#     st.markdown(footer_style, unsafe_allow_html=True)

# # ফুটার কল করা
# add_footer()
      

    
