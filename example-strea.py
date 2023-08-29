import streamlit as st

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

# Create a navigation menu
pages = {
    "Page 1": page1,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()
