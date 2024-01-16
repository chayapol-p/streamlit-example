import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

import yaml
from yaml.loader import SafeLoader

from views.landing import landing
from views.data_editor import data_editor
from views.my_dashboard import simple_dashboard
from views.data_reviewer import data_reviewer



st.set_page_config(layout="wide")

page_names_to_funcs = {
    "Home": landing,
    "Data Editor": data_editor,
    "Simple Dashboard": simple_dashboard
}


authenticator = stauth.Authenticate(
    dict(st.secrets.authentication['credentials']),
    st.secrets.authentication.cookie['name'],
    st.secrets.authentication.cookie['key'],
    st.secrets.authentication.cookie['expiry_days']
)





# expander = st.expander("Choose a demo")
# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()



authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:

    if st.session_state["name"] == "Admin":
        page_names_to_funcs = {
            "Home": landing,
            "Data Editor": data_editor,
            "Simple Dashboard": simple_dashboard,
            "Data Review": data_reviewer
        }
    else:
        page_names_to_funcs = {
            "Home": landing,
            "Data Editor": data_editor,
            "Simple Dashboard": simple_dashboard
        }
    
    with st.sidebar:

        st.header("Choose a demo")

        demo_name = option_menu(
            menu_title=None,  # required
            options=list(page_names_to_funcs.keys()),  # required
            icons=["house", "table", "graph-up"],  # optional
            menu_icon="menu-down",
            default_index=0,  # optional
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }
        )

    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{st.session_state["name"]}*')
    page_names_to_funcs[demo_name]()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
