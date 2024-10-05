import streamlit as st
import pandas as pd

table1 = pd.DataFrame({"column 1" : [1,2,3,4,5,6,7], "column 2":[11,12,13,14,15,16,17]})
st.markdown("""
<style>
    .main {
            background-color:white
        }            
</style>
""", unsafe_allow_html=True)

st.title("this is streamlist title")
st.header("this is header")
st.subheader("this is sub header")
st.text("this is a text")
st.markdown("**this is markdown**")
st.caption("this is caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"a":"1","b":"2"}
st.json(json)

code = """
    print("Hello world")
"""

st.code(code, language="python")

st.write("## H2")
st.metric(label="wind speed",value="120ms",delta="1.4ms")

st.table(table1)
st.dataframe(table1)

st.image("image.jpg")
st.audio("audio.mp3")
st.video("sample.mp4")

def change():
    print(st.session_state.checker, "changed")

status = st.checkbox("check this  !", value=True, on_change=change, key="checker")

# if status:
#     st.write("Hi")
# else:
#     pass

btn_radio = st.radio("which country?", options=("US","UK","France"))
print(btn_radio)

def btn_click():
    print("clicked")

btn = st.button("Click Me", on_click=btn_click)

select = st.selectbox("please select", options=("audi","mercedes","togg"))
print(select)

multiple_select = st.multiselect("please elect one or more item", ("USD","TL","EURO"))
print(multiple_select)

images = st.file_uploader("select a file", type=["jpg","png"], accept_multiple_files=True)

if images is not None:
    for image in images:
        st.image(image) 