#importing required libraries

import streamlit as st
import pandas as pd
from io import StringIO 



#adding a file uploader

file = st.file_uploader("Please choose a file")

if file is not None:

    #To read file as bytes:

    bytes_data = file.getvalue()

    #st.write(bytes_data)



    #To convert to a string based IO:

    stringio = StringIO(file.getvalue().decode("utf-8"))

    #st.write(stringio)



    #To read file as string:

    string_data = stringio.read()

    #st.write(string_data)



    #Can be used wherever a "file-like" object is accepted:

    df= pd.read_csv(file)
    st.dataframe(df)
    #st.write(df)
    st.line_chart(df.iloc[0,:186])



#adding a file uploader to accept multiple CSV files

#uploaded_files = st.file_uploader("Please choose a CSV file", accept_multiple_files=True)

#for file in uploaded_files:

#    bytes_data = file.read()

#    st.write("File uploaded:", file.name)

#    st.write(bytes_data)
