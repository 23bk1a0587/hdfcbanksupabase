import streamlit as st
import pandas as pd
from supabase import create_client
#####supabase configuratoin####

SUPABASE_URL = "https://zrtcysjabwwnfxijxweo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpydGN5c2phYnd3bmZ4aWp4d2VvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDMzOTAsImV4cCI6MjA4MTYxOTM5MH0.0ySTS3nQVQQif_uNxkk7-olqTLeACLc0KA4rM9UqeeI"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#Streamlit UI
st.title("HDFC BANK (Supabase)")
###################################
menu = ["REGISTER","VIEW"]
choice = st.sidebar.selectbox("Menu",menu)
#REGISTER
#_--------------------
if choice == "REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        try:
            response = supabase.table("hdfcbank").insert({
                "balance": bal
                }).execute()
            print(response)
        except Exception as e:
            print(e)
            st.success("user added successfully")

        
#View Students
#--------------------------
if choice == "VIEW":
    st.subheader("view user")
    data = supabase.table("users").select("*")
    df = pd.DataFrame(data.data)
    st.dataframe(df)


