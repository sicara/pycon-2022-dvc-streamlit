import streamlit as st

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.write("### Installation and Usage")

    st.code("pip install streamlit", language="bash")
    st.code("streamlit run streamlit_demo.py", language="bash")
    st.code("import streamlit as st", language="python")

    st.write("### Display")

    st.code('st.write("Hello 👋")', language="python")
    st.code('st.latex("e^{i\pi} + 1 = 0")', language="python")
    st.code('st.markdown("**Mark**_down_")', language="python")

    st.write("### Display Media")
    st.code('st.image("https://http.cat/200")')
    st.code("st.audio(...)")
    st.code("st.video(...)")

with col_b:
    st.write("### Display data")
    st.code('st.json({"foo": "bar", "fu": "ba"})')
    st.code(
        """
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cathy"],
    "age": [20, 31, 42],
}).assign(older_than_30=lambda df: df.age > 30)

st.dataframe(df)
    """
    )
    st.code('st.metric("My metric", 42, 2)')

    st.write("### Interactive widgets")
    st.code(
        """
cat_or_dog = st.selectbox(
    label="Pick one",
    options=["cats", "dogs"],
)
st.write("You selected:", cat_or_dog)
    """
    )
    st.code(
        """
chosen_value = st.slider('Pick a number', 0, 100)
st.write("You selected:", chosen_value)
    """
    )
    st.code(
        """
img = st.file_uploader("Upload an image")
if img:
    st.image(img, caption="The pic you Uploaded !")
    """
    )
    st.code(
        """
img = st.camera_input("Take a picture")
if img:
    st.image(img, caption="The pic you just took !")
    """
    )

with col_c:
    st.write("### ⭐ Demo !")

    with st.expander("### ⭐ Demo (click to see the code)", expanded=False):
        st.code(
            """
st_code = st.text_area("Enter streamlit code:")
try:
    exec(st_code)
except Exception as e:
    st.error(f"Error: {e}")
        """
        )

    st_code = st.text_area(label="Enter streamlit code:", height=280)
    try:
        exec(st_code)
    except Exception as e:
        st.error(f"Error: {e}")
