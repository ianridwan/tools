import streamlit as st
import pandas as pd
import pyperclip
    # Custom CSS to modify the textarea width and height
custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
          width: 100px;
        }
    </style>
    '''
st.title("Delimiter")
st.markdown(custom_css, unsafe_allow_html=True)
txt= st.text_area("copy here")
count_data = txt.count("\n")
# st.write(f'Jumlah {len(txt)} karakter.')
st.write(f'Jumlah {count_data} Data.')
delimiter=st.text_input("Delimiter",value=",")
if txt:
    df = txt.replace("\n",delimiter)
else:
    df=""
txt= st.text_area("Result",value=df)
if df!="":
    pyperclip.copy(df)
    st.warning('Berhasil Copy', icon="⚠️")
