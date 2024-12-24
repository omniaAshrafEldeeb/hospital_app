import streamlit as st
def app():
    st.header("information you")


    with st.form("my_form"):
        user_id_n = st.text_input("Enter your user id")
        password_n = st.text_input("Enter password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            i = 0
            while ((user_id_n != "omnia" or password_n != 'o' )and i<5):
                
                if submitted and (user_id_n != "omnia" or password_n != 'o'):
                    st.write("Please enter correct user id and password")
                if i > 5 :
                    st.warning("Try later")
                    # Optionally, hide the "try later" message after a certain time
                    #st.experimental_rerun()
                    st.empty
                    break
                submitted = False
                i+=1
            if user_id_n == "omnia" or password_n == 'o':
                u = None
                st.write(f"hello {user_id_n}")
            #st.page_link(r"C:\Users\MF\Desktop\StreamlitProj2\Home.py", label="Page 1", icon="1️⃣")

            #st.switch_page("pages/Home.py")
