import streamlit as st

generate_jha = st.Page("generate_jha.py", title="Create JHA")

# Setup for additional pages in the future, such as one for viewing saved JHAs
pg = st.navigation([generate_jha])
pg.run()
