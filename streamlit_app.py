import streamlit as st

from landing import landing
from data_editor import data_editor
from my_dashboard import simple_dashboard

page_names_to_funcs = {
    "—": landing,
    "data_editor": data_editor,
    "simple_dashboard": simple_dashboard
}


demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()