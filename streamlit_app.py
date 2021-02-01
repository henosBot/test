import streamlit as st

st.set_page_config(
    page_title='hi',
    page_icon='https://imgur.com/a/urHOoK3',
    layout='wide'
)

# st.title('hello')
# st.write('hi')
# sidebar = st.sidebar
# sidebar.title('hi again')
# inpt = st.text_input('Enter text here to display below')
# st.write(inpt)
def home():
    pass

def dashboard():
    pass

def contact_me():
    pass

def src_code():
    pass

# st.title('hello')
# st.write('hi')
sidebar = st.sidebar
# sidebar.title('hi again')
# inpt = st.text_input('Enter text here to display below')
# st.write(inpt)
sidebar.title('Navigation')
sidebar.header('Where do you want to go?')
if sidebar.button('Home'):
    home()
elif sidebar.button('Dashboard'):
    dashboard()
elif sidebar.button('Contact Me'):
    contact_me()
elif sidebar.button('Source Code'):
    src_code()
