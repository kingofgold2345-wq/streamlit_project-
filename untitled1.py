import streamlit as st

# ---------- PAGE ----------
st.set_page_config(page_title="Profile App", page_icon="👤", layout="centered")

# ---------- TITLE ----------
st.title("👤 Profile Creator")
st.caption("Simple clean Streamlit app")

st.divider()

# ---------- INPUTS ----------
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100, value=18)
gender = st.selectbox("Gender", ["Male", "Female"])

uploaded_file = st.file_uploader("Upload image (optional)", type=["png", "jpg", "jpeg"])

# ---------- BUTTON ----------
if st.button("Create Profile 🚀"):

    if name.strip() == "":
        st.error("Please enter your name")
    else:
        st.success("Profile created successfully!")

        # ---------- PROFILE CARD ----------
        st.subheader("📌 Profile Summary")

        col1, col2 = st.columns([1, 2])

        with col1:
            if uploaded_file:
                st.image(uploaded_file, width=120)
            else:
                st.image("https://cdn-icons-png.flaticon.com/512/847/847969.png", width=120)

        with col2:
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Gender:** {gender}")

        st.divider()

        # ---------- SMART MESSAGE ----------
        if age < 18:
            st.info("🧒 You are still young — focus on learning.")
        elif age < 30:
            st.info("💪 Great age to build your future.")
        else:
            st.info("🌟 You have strong experience!")

        st.balloons()
        
        


