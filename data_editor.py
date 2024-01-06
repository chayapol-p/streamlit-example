def data_editor():
    import streamlit as st
    import pandas as pd
    
    st.title("Data Editor")

    country_list = ('Australia', 'Thailand', 'USA')
    country = st.selectbox(
        'Please select your country?',
        country_list,
        index=None,
        placeholder='Please Select Country'
    )

    factory_type = [['A', 'B', 'C'], ['ก', 'ข', 'ค'], ['a', 'b', 'c']]

    town = st.selectbox(
        'Please select your Factory Type?',
        factory_type[country_list.index(country)] if country else (),
        index=None,
        placeholder='Please Select Country First' if not country else "",
        disabled=country is None,
    )

    if town:
        from streamlit_gsheets import GSheetsConnection

        # Create a connection object.
        conn = st.connection("gsheets", type=GSheetsConnection)

        df = conn.read()
        # df = pd.DataFrame({'Factoryname': ['A', 'B'], 'Electrical consuming(kW)': [26, 70]})
        edited_df = st.data_editor(df, num_rows="dynamic")
        # max_elec_consm = edited_df.loc[edited_df["Electrical consuming(kW)"].idxmax()]["Factoryname"]
        # st.markdown(f"The most Factory consumed is **{max_elec_consm}** 🎈")

