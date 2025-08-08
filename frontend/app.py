import streamlit as st

generate_jha = st.Page("generate_jha.py", title="Create JHA")

pg = st.navigation([generate_jha])
pg.run()
