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

# Save user info to Google Sheets
def save_user_info(name, email, favorite_food):
    sheet.append_row([name, email, favorite_food])

# Page Title and Styling
st.markdown(
    """
    <style>
    .main-title {
        color: #FF4B4B;
        font-family: 'Comic Sans MS', cursive;
        font-size: 50px;
        text-align: center;
    }
    .sub-title {
        color: #4BFF94;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
    }
    .description {
        color: #FFDA4B;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        font-size: 20px;
        margin-bottom: 50px;
    }
    .input-text {
        color: #4BFFEB;
        font-size: 18px;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True
)

# Header
st.markdown("<h1 class='main-title'>The Bite Club (TBC)</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-title'>Exclusive Food Content by @georgioelias and @jp_nassif</h2>", unsafe_allow_html=True)

# Description
st.markdown(
    "<p class='description'>Hungry for unique dishes? Follow us for some exclusive, mouth-watering food content! "
    "We're just getting started. Stay connected for more!</p>",
    unsafe_allow_html=True
)

# Instagram Links
st.markdown("<h3 class='sub-title'>Check out our Instagram:</h3>", unsafe_allow_html=True)
st.write("[Follow @georgioelias](https://instagram.com/georgioelias)")
st.write("[Follow @jp_nassif](https://instagram.com/jp_nassif)")

# User Information Form
st.markdown("<h3 class='sub-title'>Tell us more about you!</h3>", unsafe_allow_html=True)

with st.form(key='user_info_form'):
    name = st.text_input("Name", help="Enter your name")
    email = st.text_input("Email", help="Enter your email")
    favorite_food = st.text_input("Favorite Food", help="What's your favorite dish?")
    
    submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        if name and email and favorite_food:
            save_user_info(name, email, favorite_food)
            st.success(f"Thanks for sharing, {name}! Your info has been saved.")
        else:
            st.error("Please fill in all fields.")

# Add a footer with a cool call-to-action
st.markdown(
    """
    <style>
    .footer {
        color: #FF6B6B;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        font-size: 22px;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown("<p class='footer'>Stay tuned for more delicious updates! 🍔🍕🍣</p>", unsafe_allow_html=True)
