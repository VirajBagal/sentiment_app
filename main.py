import requests
import streamlit as st
from PIL import Image
import json

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Sentiment Classification web app")


# displays a text input widget
text = st.text_input("Enter some text")


if st.button("Tell the sentiment"):
    if text is not None:
        files = {"text": text}
        # res = requests.post("http://0.0.0.0:8068/sentiment", data=json.dumps(files))
        # result = res.json()
        result = {"name": 'positive'}
        label = result.get("name")
        st.text(label)

