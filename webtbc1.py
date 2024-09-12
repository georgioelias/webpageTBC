import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Set up the Google Sheets API
credentials = st.secrets["gcp_service_account"]
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("TBC Ideas").sheet1  # Ensure this is the right spreadsheet name

# Save user info and answers to Google Sheets
def save_user_info(name, email, instagram_handle, favorite_food, q1, q2, q3, q4, q5):
    sheet.append_row([name, email, instagram_handle, favorite_food, q1, q2, q3, q4, q5])

# Page Title and Styling with Google Fonts and CSS for mobile-friendliness
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
    }
    .main-title {
        color: #FF4B4B;
        font-family: 'Roboto', sans-serif;
        font-size: 36px;
        text-align: center;
        margin-top: 20px;
    }
    .sub-title {
        color: #4BFF94;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        margin-bottom: 20px;
    }
    .description {
        color: #FFDA4B;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .input-text {
        color: #4BFFEB;
        font-size: 18px;
        font-family: 'Roboto', sans-serif;
    }
    .form-input {
        margin: 10px 0;
    }
    .form-label {
        font-weight: bold;
        font-size: 14px;
    }
    .footer {
        color: #FF6B6B;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 18px;
        margin-top: 30px;
    }
    @media only screen and (max-width: 600px) {
        .main-title {
            font-size: 28px;
        }
        .sub-title {
            font-size: 20px;
        }
        .description {
            font-size: 14px;
        }
    }
    </style>
    """, unsafe_allow_html=True
)

# Add the Logo
st.image("logo.png", width=150)  # Add the path to your logo image here

# Header
st.markdown("<h1 class='main-title'>The Bite Club (TBC)</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-title'>Exclusive Food Content by @georgioelias and @jp_nassif</h2>", unsafe_allow_html=True)

# Description
st.markdown(
    "<p class='description'>Hungry for unique dishes? Follow us for some exclusive, mouth-watering food content! "
    "We're just getting started. Stay connected for more!</p>",
    unsafe_allow_html=True
)

# Instagram Links with Icons
st.markdown("<h3 class='sub-title'>Check out our Instagram:</h3>", unsafe_allow_html=True)
st.write("[![Instagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png)](https://instagram.com/georgioelias) Follow @georgioelias")
st.write("[![Instagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png)](https://instagram.com/jp_nassif) Follow @jp_nassif")

# User Information Form
st.markdown("<h3 class='sub-title'>Join The Bite Club</h3>", unsafe_allow_html=True)

with st.form(key='user_info_form'):
    name = st.text_input("Full Name", help="Enter your name", key="name", class_="form-input")
    email = st.text_input("Email Address", help="Enter your email", key="email", class_="form-input")
    instagram_handle = st.text_input("Instagram Handle", help="Enter your Instagram username", key="instagram", class_="form-input")
    favorite_food = st.text_input("Favorite Food", help="What's your favorite dish?", key="favorite_food", class_="form-input")
    
    st.markdown("### Club Entry Questions")
    q1 = st.text_input("Why are you worthy of entering 'thebiteclub'?", key="q1", class_="form-input")
    q2 = st.text_input("What’s the most ridiculous food combination that you secretly love?", key="q2", class_="form-input")
    q3 = st.text_input("If 'thebiteclub' had a mascot, what would it be and why?", key="q3", class_="form-input")
    q4 = st.text_input("What secret food talent makes you stand out from the rest?", key="q4", class_="form-input")
    q5 = st.text_input("Which food item best represents your personality, and how would it make the club better?", key="q5", class_="form-input")
    
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if name and email and instagram_handle and favorite_food and q1 and q2 and q3 and q4 and q5:
            save_user_info(name, email, instagram_handle, favorite_food, q1, q2, q3, q4, q5)
            st.success(f"Thanks for joining, {name}! Your info has been saved.")
        else:
            st.error("Please fill in all fields.")

# Add a footer with a cool call-to-action
st.markdown(
    """
    <style>
    .footer {
        color: #FF6B6B;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 18px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown("<p class='footer'>Stay tuned for more delicious updates! 🍔🍕🍣</p>", unsafe_allow_html=True)
