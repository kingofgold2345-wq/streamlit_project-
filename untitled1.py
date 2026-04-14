import streamlit as st


st.set_page_config(page_title="Test App", page_icon="🎯")


st.title("🎯 Welcome App")


name = st.text_input("👤 ادخل اسمك")
age = st.number_input("🎂 ادخل عمرك", min_value=0, max_value=100, step=1)
gender = st.selectbox("🚻 اختر النوع", ("male", "female"))


if st.button("✨ عرض النتيجة"):
    if name == "":
        st.warning("⚠️ من فضلك ادخل اسمك")
    else:
        st.success(f"👋 اهلا بك {name}!")

        
        st.write(f"🎂 عمرك: {age}")
        st.write(f"🚻 النوع: {gender}")

        
        st.balloons()
        st.snow()
        
        


