
import streamlit as st
import cv2
import tensorflow as tf 
import numpy as np
from keras.models import load_model
from PIL import Image
import PIL

#model
model= load_model('frames.hdf5',compile=(False))

#body and functions of the app
def split_videos(name):
    vidcap = cv2.VideoCapture(name)
    success,frame = vidcap.read()
    count = 0
    frame_skip =1
    while success:
        success, frame = vidcap.read() # get next frame
        cv2.imwrite(r"C:\Users\Mushati\Desktop\ass\frame%d.jpg" % count, frame) 
        if count % frame_skip == 0: # analyse frames
            print('frame: {}'.format(count)) 
            pil_img = Image.fromarray(frame) # convert frames
            st.image(pil_img)
            
        if count > 20 :
            break
        count += 1
    processing()

def converting_vidd():
    x = tf.io.read_file('frame1.jpg')
    x = tf.io.decode_image(x,channels=3) 
    x = tf.image.resize(x,[299,299])
    x = tf.expand_dims(x, axis=0)
    x = tf.keras.applications.inception_v3.preprocess_input(x)
    return x
    
def predict(x):
    mod_pred = tf.keras.applications.inception_v3.decode_predictions(model.predict(x), top=1)
    return mod_pred
    
def main():
    
    st.title("INCEPTIONV3")
    vidio = None

    Search = st.text_input("Search for an object........here",)
    file_Uploade = st.file_uploader("Choose Video",type=(['avi','mp4']))
    if uploaded_video is not None: 
        vidio = file_Uploade.name
        with open(file, mode='wb') as f:
            f.write(file_Uploade.read()) 

        st.sidebar.markdown(f"""
        ### Files
        - {vidio}
        """,
        unsafe_allow_html=True) # display file name

        vidcap = cv2.VideoCapture(vid) # load video from disk
        cur_frame = 0
        success = True
        
    if st.button("detect"):
        convert_frames = creating_frames(vid)
        output = converting_vidd()
        results_final = predict(output)
    
        #st.success('The Output is {}'.format(output))
        st.success(results_final)

        
if __name__=='__main__':
    main()