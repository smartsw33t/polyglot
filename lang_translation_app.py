import streamlit as st
from mtranslate import translate
import pandas as pd
import os
import pyautogui

# read language dataset
df = pd.read_excel(os.path.join('data', 'language.xlsx'))
lang = df['Language'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.title("Language Translation app")
st.markdown("In < 40 lines of Python 🐍 code with Streamlit ! (https://www.streamlit.io/)")
st.markdown("Update data/language.xlsx if required based on your requirements!!")
clear = st.button("CLEAR")
inputtext = st.text_area("INPUT",height=200)
choice = st.sidebar.radio('SELECT LANGUAGE',langlist)

# clear function
def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)
    pyautogui.press("tab", interval=0.15)

# I/O
if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        st.text_area("TRANSLATED TEXT",output,height=200)
    except Exception as e:
        st.error(e)

# Clear I/O
if clear:
    Clear()
