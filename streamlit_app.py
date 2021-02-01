import streamlit as st

st.set_page_config(
    page_title='test',
    page_icon='https://imgur.com/a/urHOoK3',
    layout='wide'
)

# st.title('hello')
# st.write('hi')
# sidebar = st.sidebar
# sidebar.title('hi again')
inpt = st.text_input('Enter text here to display below')
st.write(inpt)
