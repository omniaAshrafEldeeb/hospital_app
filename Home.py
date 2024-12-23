import streamlit as st

def app():

    # Example Streamlit content
    col1, col2 = st.columns([2,6])
    with col2 :st.title("Hello to our App")
    v1 ,v2=st.columns([3,10])
    with v2 : st.header("")
    v1 ,v2, v3=st.columns([1,1,1])
    with v2 :st.markdown("***We wish you complete health.*** ")
    with v3 : st.image("doctors and health workers.png", width=200)

    #print('okay')


    