def data_reviewer():

    import streamlit as st
    import pandas as pd

    st.write("This is Data Reviewwer pages")

    df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": ["apple", "berry", "grapes"],
            "C": ["red", "blue", "green"]
        },
        columns=["A", "B", "C"])

    df2 = df.copy()
    df2.loc[0, 'C'] = 'green'
    df2.loc[2, 'B'] = 'guava'
    # New row to be added
    # new_row = {'A': 4, 'B': 'banana', 'C': 'yellow'}

    # Append the new row to the DataFrame
    # df2 = df2.append(new_row, ignore_index=True)

    compare = df.compare(df2, keep_shape=True).drop('other', level=1, axis=1)
    compare = compare.droplevel(1, axis=1).dropna(how='all')

    filtered = df.loc[compare.index]

    def color_cells(s, color):
        if pd.notna(s):
            return 'color:{0}; font-weight:bold'.format(color)
        else:
            return ''
      
    left, right = st.columns(2)

    with left:
        st.title("Existed Data")
        st.dataframe(df.style.apply(lambda x: compare.applymap(lambda c: color_cells(c, 'red')), axis=None))
    
    with right:
        st.title("Edited Data")
        st.dataframe(df2.style.apply(lambda x: compare.applymap(lambda c: color_cells(c, 'blue')), axis=None))
        st.button('Approve')