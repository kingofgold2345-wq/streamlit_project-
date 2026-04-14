import streamlit as st

# Page setup
st.set_page_config(page_title="Smart Profile App", page_icon="🚀", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 Smart Profile App")
st.write("املأ البيانات واضغط عرض النتيجة")

# Sidebar
st.sidebar.header("⚙️ Settings")
show_effects = st.sidebar.checkbox("🎉 تشغيل المؤثرات", value=True)

# Inputs
name = st.text_input("👤 ادخل اسمك")
age = st.slider("🎂 اختر عمرك", 1, 100, 18)
gender = st.radio("🚻 النوع", ["male", "female"])

# Image upload
image = st.file_uploader("📸 ارفع صورتك (اختياري)", type=["png", "jpg", "jpeg"])

# Button
if st.button("✨ عرض النتيجة"):
    if not name:
        st.error("⚠️ لازم تكتب اسمك!")
    else:
        st.success(f"👋 اهلا يا {name}!")

        # Show image if uploaded
        if image:
            st.image(image, caption="صورتك", width=150)

        # Info
        st.write(f"🎂 عمرك: {age}")
        st.write(f"🚻 النوع: {gender}")

        # Smart message
        if age < 18:
            st.info("📚 انت في سن التعلم والتطوير!")
        elif age < 30:
            st.info("💪 وقت تبني مستقبلك!")
        else:
            st.info("🌟 خبرة جميلة ما شاء الله!")

        # Gender message
        if gender == "male":
            st.write("👦 منور يا بطل!")
        else:
            st.write("👧 منورة يا قمر!")

        # Effects
        if show_effects:
            st.balloons()

# Footer
st.markdown("---")
st.caption("Made by Malek 😎")
        
        


