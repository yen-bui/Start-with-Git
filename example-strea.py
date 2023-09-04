import streamlit as st
import pandas as pd
import plotly.express as px


# Create a function to display the Plotly graph
def display_plotly_graph():
    # Load the Plotly HTML file
    with open("plotly_graph.html", "r") as file:
        plotly_html = file.read()

    # Display the Plotly graph using st.write()
    st.write(plotly_html, unsafe_allow_html=True)

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

    # Display the Plotly graph on Page 1
    display_plotly_graph()

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
