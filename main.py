import streamlit as st


def login_page():
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if check_login(username, password):  # You would define check_login based on your criteria
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state["user_name"] = username

            st.success("Logged in successfully for " + st.session_state.username + "!" )
            st.switch_page("pages/CreateAdd.py") # Adjust path as needed

        else:
            st.error("Invalid credentials")

def check_login(username, password):
    # Replace this with your actual login logic (database, API calls, etc.)
    return username == "admin" and password == "password"


login_page()
