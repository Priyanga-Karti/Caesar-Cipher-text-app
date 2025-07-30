import streamlit as st

# Caesar Cipher Encryption Function
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result

# Custom CSS for Bloom Style
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: linear-gradient(to right, #fef9f4, #fdeeee);
        font-family: 'Trebuchet MS', sans-serif;
        color: #4b3832;
    }
    .stTextArea textarea {
        background-color: #fff7f0 !important;
        color: #4b3832 !important;
        border-radius: 12px;
        font-size: 16px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #f7a1c4;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ec699e;
        transform: scale(1.05);
    }
    .stSuccess {
        background-color: #fffafc;
        border-left: 5px solid #f08080;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
    }
    h1, h4 {
        text-align: center;
        color: #b04e6f;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("💐 Caesar Cipher Text Generator")

st.markdown("🌸")
st.write("Encrypt your lovely message with Caesar Cipher — now styled in a soft bloom theme!")

# User input
text_input = st.text_area("💌 Enter your message:", value="Hello Bloom World")
shift = st.slider("🔢 Select shift value:", min_value=1, max_value=25, value=3)

# Encrypt button
if st.button("✨ Encrypt"):
    encrypted_text = caesar_cipher(text_input, shift)
    st.success(f"🔒 **Encrypted Message:** {encrypted_text}")

    # Flower emojis
    st.markdown("""
    <div style="text-align:center; font-size:30px; margin-top:20px;"
    </div>
    """, unsafe_allow_html=True)

    # Floral animation (GIF)
    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZWV5ZDViczY0MWJ6OTg4OHdydmp3bHY0NmgwZXZlNHRkdXBzdWRlNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPgeKwsjc6VCOxq/giphy.gif" width="300" />
    </div>
    """, unsafe_allow_html=True)
