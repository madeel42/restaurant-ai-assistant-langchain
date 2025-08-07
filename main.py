import streamlit as st
import  langchain_helper
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox(
    "Choose a Restaurant Name",("Pakistan","Mexico","Indian") )

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"])
    menu_item = response["menu_item"].split(",")
    st.write('**menu_item**')
    for item in menu_item:
        st.write("-",item)