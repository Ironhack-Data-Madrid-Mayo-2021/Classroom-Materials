import streamlit as st
from predictor import predict_entry

info = dict()

info["mean_radius"] = st.slider("Radio del nódulo", 2, 10, 1)
info["mean_area"] = st.slider("Radio del nódulo", 6, 50, 3)

st.text(info)

pred = predict_entry(info)
st.success(pred)
