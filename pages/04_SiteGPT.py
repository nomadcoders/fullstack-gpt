from langchain.document_loaders import SitemapLoader
import streamlit as st


@st.cache_data(show_spinner="Loading website...")
def load_website(url):
    loader = SitemapLoader(url)
    loader.requests_per_second = 5
    docs = loader.load()
    return docs


st.set_page_config(
    page_title="SiteGPT",
    page_icon="🖥️",
)


st.markdown(
    """
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)


with st.sidebar:
    url = st.text_input(
        "Write down a URL",
        placeholder="https://example.com",
    )


if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a Sitemap URL.")
    else:
        docs = load_website(url)
        st.write(docs)
