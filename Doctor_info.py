import streamlit as st
import pyodbc
import pandas as pd
from sqlalchemy import create_engine


def app():
    v1 ,v2=st.columns([3,12])
    with v2 : st.subheader("")
    v1 ,v2=st.columns([3,12])
    with v2: st.title("information about Doctors, 1433")
    v1 ,v2=st.columns([3,10])

    result4 =pd.read_csv('output_file_D.csv')
    for i, row in result4.iterrows():
        col1,col2 = st.columns([25,10])
        D_name = row['D_name']
        De_name = row['De_name']
        phone_number = row['phone_number']
        H_name = row['H_name']

        sentiment_mapping = ["one", "two", "three", "four", "five"]


        # Display the food details
        with col1:st.write(f" ***{D_name}***, Department: {De_name}, phone: {phone_number}, Hospital name: {H_name}")
                        # Use st.slider to get the rating
        with col2:selected = st.feedback("stars",key = f"feedback_{i}")
        if selected is not None:
            st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

        #with col2: rating = st.slider(f"Rate {D_name}", 0, 5, 0, key=f"slider_{i}")
        result4.at[i, 'rating'] = selected  # Update the rating in the DataFrame
        result4.to_csv('output_file_D.csv', index=False)  # Set index=False to not include the row index in the CSV

    # Show the DataFrame with the ratings
    on = st.toggle("Show Doctor Tables")

    if on:
        st.write("Doctor Ratings:")
        st.dataframe(result4)
