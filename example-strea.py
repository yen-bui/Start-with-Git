import streamlit as st

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

    # Display the Plotly graph using an IFrame
    st.write("Plotly Graph on Page 1:")
    
    # Provide the URL to the raw GitHub content of your HTML file
    github_raw_url = "https://raw.githubusercontent.com/yen-bui/Start-with-Git/main/plotly_graph.html"
    
    # Use the IFrame component to display the external HTML content
    st.components.v1.html(f'<iframe src="{github_raw_url}" width="1000" height="600"></iframe>', width=1000, height=600, scrolling=True)
    
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
