import streamlit as st

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

    # Display the Plotly graph using an IFrame
    st.write("Plotly Graph on Page 1:")
    
    # Provide the direct link to the Google Drive file
    google_drive_url = "https://drive.google.com/file/d/1chj9-22F3NPzwEOsonnAT5txamawookM/preview"
    
    # Use the iframe tag to display the external content
    st.write(f'<iframe src="{google_drive_url}" width="1000" height="600"></iframe>', unsafe_allow_html=True)
    
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
