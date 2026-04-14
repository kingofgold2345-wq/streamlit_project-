import streamlit as st
import json
import os

# ---------- Setup ----------
st.set_page_config(page_title="Ultimate App", page_icon="🔥", layout="wide")

DATA_FILE = "users.json"

# ---------- Load / Save ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

users = load_data()

# ---------- Session ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ---------- UI Style ----------
st.markdown("""
<style>
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN ----------
if not st.session_state.logged_in:
    st.title("🔐 Login System")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    col1, col2 = st.columns(2)

    # LOGIN
    with col1:
        if st.button("Login"):
            for user in users:
                if user["username"] == username and user["password"] == password:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.success("✅ Logged in!")
                    st.rerun()
            st.error("❌ Wrong username or password")

    # REGISTER
    with col2:
        if st.button("Register"):
            if username and password:
                users.append({
                    "username": username,
                    "password": password,
                    "age": None,
                    "gender": None
                })
                save_data(users)
                st.success("🎉 Account created!")
            else:
                st.warning("⚠️ Fill all fields")

# ---------- MAIN APP ----------
else:
    st.sidebar.title("🔥 Menu")
    choice = st.sidebar.radio("Go to", ["Profile", "Dashboard", "Logout"])

    # PROFILE
    if choice == "Profile":
        st.title("👤 Your Profile")

        user = st.session_state.user

        age = st.slider("🎂 Age", 1, 100, user["age"] or 18)
        gender = st.selectbox("🚻 Gender", ["male", "female"])

        image = st.file_uploader("📸 Upload Image", type=["png", "jpg"])

        if st.button("💾 Save Profile"):
            user["age"] = age
            user["gender"] = gender

            save_data(users)
            st.success("Saved!")

            if image:
                st.image(image, width=150)

        # Smart message
        if user["age"]:
            if user["age"] < 18:
                st.info("📚 Learning phase!")
            elif user["age"] < 30:
                st.info("💪 Build your future!")
            else:
                st.info("🌟 Strong experience!")

    # DASHBOARD
    elif choice == "Dashboard":
        st.title("📊 Dashboard")

        total_users = len(users)
        males = sum(1 for u in users if u.get("gender") == "male")
        females = sum(1 for u in users if u.get("gender") == "female")

        col1, col2, col3 = st.columns(3)

        col1.metric("👥 Users", total_users)
        col2.metric("👦 Males", males)
        col3.metric("👧 Females", females)

        # Show all users
        st.subheader("📋 Users Data")
        st.write(users)

    # LOGOUT
    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()
        
        


