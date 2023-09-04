import streamlit as st
import pandas as pd
import plotly.express as px
# from streamlit.components.v1 import components

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

    # Display the Plotly graph using an IFrame
    st.write("Plotly Graph on Page 1:")
    
    # Provide the path to the local HTML file (assuming it's in the same directory)
    # local_html_path = "plotly_graph.html"
    
    # Use the components function to embed the HTML content
    st.components.v1.html(open("plotly_graph.html", 'r').read(), width=1000, height=600, scrolling=True)
    
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
