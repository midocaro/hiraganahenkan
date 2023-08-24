
import streamlit as st
from pykakasi import kakasi

def convert_to_hiragana(text):
    kakasi_obj = kakasi()
    kakasi_obj.setMode('J', 'H')
    conv = kakasi_obj.getConverter()
    return conv.do(text)

st.title('漢字変換アプリ')
user_input = st.text_input('漢字を含んだ文章を入力してください')
hiragana_text = convert_to_hiragana(user_input)
st.write('平仮名に変換された文章:', hiragana_text)
