import streamlit as st

# Page setup
st.set_page_config(page_title="My App", page_icon="👋")

st.title("👋 مرحباً بك")

# Inputs
name = st.text_input("ادخل اسمك")
age = st.number_input("ادخل عمرك", min_value=0, max_value=120, step=1)
gender = st.selectbox("ولد ولا بنت؟", ["male", "female"])

# Button
if st.button("عرض النتيجة"):
    
    if name.strip() == "":
        st.warning("❌ من فضلك اكتب اسمك")
    
    else:
        st.success(f"🎉 اهلا يا {name}")

        st.write("👤 الاسم:", name)
        st.write("🎂 العمر:", age)
        st.write("⚧ الجنس:", gender)

        # Correct indentation block 👇
        if age < 13:
            st.balloons()
        
        elif age < 25:
            st.info("🔥 شباب!")
            st.balloons()
        
        else:
            st.info("💼 شخص ناضج")
            st.snow()
