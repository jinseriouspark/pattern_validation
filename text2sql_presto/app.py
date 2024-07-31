import streamlit as st
from streamlit import config
import make_db
#import text2sql
import sql_training


# 페이지 설정
#st.set_page_config(page_title='text2sql', layout = 'wide')

PAGES = {
    'Excel to DataBase': make_db,
    'SQL Training' : sql_training,
#    'Text2SQL' : text2sql
}

st.sidebar.title('메뉴')
selection = st.sidebar.radio('Go to', list(PAGES.keys()))

page = PAGES[selection]
page.app()
