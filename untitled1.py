import streamlit as st

st.set_page_config(
    page_title="Profile App",
    page_icon="👤",
    layout="centered"
)


st.markdown("""
    <h1 style='text-align: center;'>👤 Profile Builder</h1>
    <p style='text-align: center; color: gray;'>Create a clean profile in seconds</p>
""", unsafe_allow_html=True)

st.divider()


with st.container():
    st.subheader("📝 Your Details")

    name = st.text_input("Name")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=18)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])

    image = st.file_uploader("Upload Profile Image (optional)", type=["png", "jpg", "jpeg"])

create = st.button("🚀 Create Profile")


if create:

    if not name.strip():
        st.error("⚠️ Name cannot be empty")
    else:
        st.success("Profile created!")

        st.divider()

  
        col1, col2 = st.columns([1, 2])

        with col1:
            if image:
                st.image(image, width=140)
            else:
                st.image("https://cdn-icons-png.flaticon.com/512/847/847969.png", width=140)

        with col2:
            st.markdown(f"### {name}")
            st.write(f"🎂 Age: **{age}**")
            st.write(f"🚻 Gender: **{gender}**")

        st.divider()

      
        message = (
            "🧒 Focus on learning" if age < 18 else
            "💪 Perfect age to build your future" if age < 30 else
            "🌟 Strong experience stage"
        )

        st.info(message)

        st.snow()
        
        


