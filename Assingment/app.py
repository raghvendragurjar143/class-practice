import streamlit as st

# -------------------------------
# Title
# -------------------------------
st.title("🎉 Streamlit Widgets Demo")
st.header("Learn Streamlit Step by Step")
st.write("Welcome to Streamlit!")

# -------------------------------
# Text
# -------------------------------
st.subheader("1. Text Widgets")

name = st.text_input("Enter Your Name")
password = st.text_input("Enter Password", type="password")
about = st.text_area("About Yourself")

# -------------------------------
# Numbers
# -------------------------------
st.subheader("2. Number Widgets")

age = st.number_input("Enter Age", min_value=1, max_value=100)
salary = st.number_input("Enter Salary")

# -------------------------------
# Date & Time
# -------------------------------
st.subheader("3. Date & Time")

date = st.date_input("Select Date")
time = st.time_input("Select Time")

# -------------------------------
# Slider
# -------------------------------
st.subheader("4. Slider")

marks = st.slider("Select Marks", 0, 100)

# -------------------------------
# Checkbox
# -------------------------------
st.subheader("5. Checkbox")

python = st.checkbox("I Know Python")

# -------------------------------
# Radio Button
# -------------------------------
st.subheader("6. Radio Button")

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

# -------------------------------
# Selectbox
# -------------------------------
st.subheader("7. Selectbox")

city = st.selectbox(
    "Choose City",
    ["Delhi", "Noida", "Ghaziabad", "Agra"]
)

# -------------------------------
# Multiselect
# -------------------------------
st.subheader("8. Multiselect")

skills = st.multiselect(
    "Select Skills",
    ["Python", "Java", "C++", "SQL"]
)

# -------------------------------
# Color Picker
# -------------------------------
st.subheader("9. Color Picker")

color = st.color_picker("Choose Color")

# -------------------------------
# File Upload
# -------------------------------
st.subheader("10. File Uploader")

file = st.file_uploader("Upload File")

# -------------------------------
# Button
# -------------------------------
st.subheader("11. Button")

if st.button("Click Me"):
    st.success("Button Clicked Successfully!")

# -------------------------------
# Form
# -------------------------------
st.subheader("12. Form")

with st.form("Student Form"):

    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    mobile = st.text_input("Mobile Number")

    submit = st.form_submit_button("Submit")

if submit:
    st.success("Form Submitted")
    st.write("First Name:", fname)
    st.write("Last Name:", lname)
    st.write("Mobile:", mobile)

# -------------------------------
# Display Output
# -------------------------------
st.subheader("13. Output")

st.write("Name:", name)
st.write("Age:", age)
st.write("Salary:", salary)
st.write("Date:", date)
st.write("Time:", time)
st.write("Marks:", marks)
st.write("Python:", python)
st.write("Gender:", gender)
st.write("City:", city)
st.write("Skills:", skills)
st.write("Favorite Color:", color)

# -------------------------------
# Progress Bar
# -------------------------------
st.subheader("14. Progress Bar")

progress = st.progress(75)

# -------------------------------
# Spinner
# -------------------------------
st.subheader("15. Spinner")

with st.spinner("Loading..."):
    import time
    time.sleep(2)

st.success("Completed!")
