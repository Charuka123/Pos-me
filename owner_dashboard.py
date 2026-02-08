import streamlit as st
from supabase import create_client, Client
import pandas as pd

# --- SUPABASE CONFIG ---
URL = "https://qzucyezcphgwhmuzolqd.supabase.co"
KEY = "sb_publishable_8DoGUldXBlz5Na-qOF_Ezw_9cYdClgL" # Anon Key එක පාවිච්චි කරන්න
supabase: Client = create_client(URL, KEY)

st.set_page_config(page_title="Mr.Charu POS Dashboard", layout="wide")

st.title("📊 Mr.Charu POS - Live Owner Dashboard")
st.write("කඩේ සිදුවන විකුණුම් මෙතැනින් Live බලාගත හැක.")

# --- DATA FETCHING ---
try:
    # sales_summary ටේබල් එකෙන් දත්ත ගෙන්වා ගැනීම
    res = supabase.table("sales_summary").select("*").execute()
    data = res.data

    if data:
        df = pd.DataFrame(data)
        
        # මුළු ආදායම පෙන්වන කොටස
        total_revenue = df['total_amount'].sum()
        total_bills = len(df)
        
        col1, col2 = st.columns(2)
        col1.metric("මුළු ආදායම (Total Revenue)", f"Rs. {total_revenue:,.2f}")
        col2.metric("මුළු බිල්පත් ගණන (Total Bills)", total_bills)
        
        st.subheader("📝 විකුණුම් විස්තර")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("තවමත් කිසිදු විකුණුම් දත්තයක් ලැබී නැත.")

except Exception as e:
    st.error(f"Error connecting to Supabase: {e}")

# Refresh Button
if st.button('Update Data'):
    st.rerun()