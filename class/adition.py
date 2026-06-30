import streamlit as st
st.set_page_config(page_title="numberaddition",page_icon="➕",layout="centered")
st.title(" addition of two number by raghvendra gurjar")
st.caption("enter two number and it will return addition of them")


form=st.form("add_form")
num1=form.number_input("first number")
num2=form.number_input("second number")
submitted=form.form_submit_button("calculate sum")


if submitted:
    result=num1+num2
    st.divider()
    st.metric(label="result",value=result)

    for i in range(1,12):
        st.write("2x",i,"=")

        ##
        import streamlit as st

st.set_page_config(
    page_title="Addition Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Addition Calculator")
st.divider()

with st.form("my_form"):

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter First Number")

    with col2:
        num2 = st.number_input("Enter Second Number")

    submitted = st.form_submit_button("➕ Calculate")

if submitted:
    result = num1 + num2
    st.success(f"✅ Sum = {result}")
    st.balloons()
    st.color_picker("chose color")

    #app banana shikh rahe h 