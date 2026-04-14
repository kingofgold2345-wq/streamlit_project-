import streamlit as st

# Page config
st.set_page_config(page_title="Test App", page_icon="🎯")

# Title
st.title("🎯 Welcome App")

# Inputs
name = st.text_input("👤 ادخل اسمك")
age = st.number_input("🎂 ادخل عمرك", min_value=0, max_value=100, step=1)
gender = st.selectbox("🚻 اختر النوع", ("male", "female"))

# Button
if st.button("✨ عرض النتيجة"):
    if name == "":
        st.warning("⚠️ من فضلك ادخل اسمك")
    else:
        st.success(f"👋 اهلا بك {name}!")

        # Extra info
        st.write(f"🎂 عمرك: {age}")
        st.write(f"🚻 النوع: {gender}")

        # Fun effect
        st.balloons()
