import streamlit as st

st.title("Setup solar display")

# Title of the box
st.subheader("Initial Setup")

# Text inputs for email, country, city
email = st.text_input("Email")
country = st.text_input("Country")
city = st.text_input("City")

# Button to submit the form
if st.button("Enter"):
    # Action to perform when the button is clicked
    st.write("Email:", email)
    st.write("Country:", country)
    st.write("City:", city)