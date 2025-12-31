import streamlit as st
import os
from model import translate_text

# Configure the page
st.set_page_config(
    page_title="GlobalSpeak | AI Translator",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS for modern aesthetics
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a40 100%);
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #2e2e42;
        color: #fff;
        border-radius: 10px;
        border: 1px solid #4a4a6a;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #2e2e42;
        color: white;
        border-radius: 8px;
        border: 1px solid #4a4a6a;
    }
    .stButton > button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(75, 108, 183, 0.4);
    }
    .success-box {
        padding: 20px;
        background-color: #2a2a40;
        border-left: 5px solid #4b6cb7;
        border-radius: 5px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        background: -webkit-linear-gradient(#eee, #aaa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load languages
@st.cache_data
def load_languages():
    languages = {}
    file_path = os.path.join(os.path.dirname(__file__), 'dataset', 'languages.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if ' - ' in line:
                    parts = line.strip().split(' - ')
                    if len(parts) == 2:
                        name, code = parts
                        languages[name] = code
    return languages

# Load languages
lang_map = load_languages()
# Extend with common code reverse lookup if needed or just use names list
lang_names = list(lang_map.keys())

# Header
st.title("🌍 GlobalSpeak Translator")
st.markdown("### Break Language Barriers Instantly")

# Layout
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("From Language", options=["Auto Detect"] + lang_names, index=0)

with col2:
    # Default to English or second in list
    default_index = list(lang_names).index("English") if "English" in lang_names else 0
    target_lang_name = st.selectbox("To Language", options=lang_names, index=default_index)

# Input Area
text_input = st.text_area("Enter text to translate:", height=150, placeholder="Type something here...")

# Translate Button
if st.button("Translate Text ✨"):
    if text_input:
        
        # Determine Source Code
        source_code = 'auto'
        if source_lang_name != "Auto Detect":
            source_code = lang_map[source_lang_name]
            
        # Determine Target Code
        target_code = lang_map[target_lang_name]
        
        with st.spinner('Translating...'):
            translated_text = translate_text(text_input, source_code, target_code)
            
        if "Error:" in translated_text:
            st.error(translated_text)
        else:
            st.markdown(f"""
            <div class="success-box">
                <h4 style="margin-top:0; color: #aaa;">Translation ({target_lang_name}):</h4>
                <p style="font-size: 1.2em; line-height: 1.6;">{translated_text}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Optional: Copy button or other features could go here
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.caption("🚀 Powered by Google Translator & Deep Translator | Developed for AI Learning")
