import os
import platform
from PIL import Image
import streamlit as st

def CreateAdvertisement():
    
    imgCnt = 0
    num_columns = 3 
    user_values = []

    st.sidebar.page_link('pages/CreateAdd.py', label='Cretate Advertisement')
    if "user_name" in st.session_state:
        retrieved_name = st.session_state["user_name"]

    #st.title("Create Advertisement - Welcome " + retrieved_name)

    save_folder = "uploaded_images/" + retrieved_name
    if not os.path.exists(save_folder):
        os.makedirs(save_folder ,exist_ok=True)


    # Create a text area with a label and a default value
    user_input = st.text_area(
        "Enter your content here:",
        "",
        height=100  # Optional: set the height of the text area
    )

    nodeName = platform.node()

    if nodeName.find("MacBook") != -1 or nodeName.find("Windows") != -1:
        

        uploaded_files = st.file_uploader("Upload an image", 
                                        type=["jpg", "jpeg", "png"],         
                                        accept_multiple_files=True,
                                        label_visibility="collapsed")
        
        
        if uploaded_files is not None:
            
            if imgCnt < 7:         

                if len(uploaded_files) + imgCnt > 7:
                    st.warning("You have uploaded more than 7 images. Only the first 7 will be displayed.")
                    files_to_display = uploaded_files[:7]
                else:
                    files_to_display = uploaded_files
                
                st.write("Small Image:")
                
                columns = st.columns(num_columns)

                #for uploaded_file in files_to_display:
                for i, uploaded_file in enumerate(uploaded_files):
                    with columns[i % num_columns]:  # Place image in the correct column
                        
                        st.image(uploaded_file,
                                caption=f"{uploaded_file.name}", 
                                use_container_width=False, 
                                width=200)     
                        
                        file_path = os.path.join(save_folder, uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        
                        imgCnt += 1
                        user_values.append(os.path.join(save_folder, uploaded_file.name))
                        if imgCnt == 7:
                            break
        
        
        if 'counter' not in st.session_state:
            st.session_state.counter = 0
            st.session_state.valData = "" 
            st.session_state.a = "" 


        def Save_data():
            st.session_state.counter += 1
            for item in user_values:
                st.session_state.a = st.session_state.a + " --- " + item
            st.session_state.valData = user_input 


        submit_button = st.button("Save Data", on_click=Save_data)
        st.write(f"Counter: {st.session_state.counter} --- " 
                 + st.session_state.valData + "------" 
                 + st.session_state.a)



        #with st.form("CreateAdvertisementForm"):
        #    submit_button = st.form_submit_button("Create Content")

    else:
        
        camera_picture = st.camera_input("Take a picture")
        if camera_picture:
            st.image(camera_picture, caption="Picture from camera")
    
    
        




CreateAdvertisement()