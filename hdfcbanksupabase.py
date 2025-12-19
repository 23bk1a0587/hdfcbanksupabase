import streamlit as st
import pandas as pd
from supabase import create_client
SUPABASE_URL="https://rghmycrqrdrcvstfudhd.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJnaG15Y3JxcmRyY3ZzdGZ1ZGhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDE4MDQsImV4cCI6MjA4MTYxNzgwNH0.uGRv5HHOrKcuxVpdxUpMUV2sH3UIe2ETQcbwH217dg4"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
st.title("HDFC BANK(supabase)")
menu=["REGISTER","VIEW"]
choice = st.sidebar.selectbox("menu",menu)
if choice == "REGISTER":
    name=st.text_input("enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users1").insert({
            "name": name,
            "age": age,
            "account": account,
            "balance":bal}).execute()
        st.success("user added successfully")
if choice == "VIEW":
    st.subheader("view users1")
    data = supabase.table("users1").select("*").execute()
    df = pd.DataFrame(data.data)
