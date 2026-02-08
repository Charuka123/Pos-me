import streamlit as st
from supabase import create_client
import pandas as pd

# --- CONFIG (ඔයාගේ Keys මෙතනට පේස්ට් කරන්න) ---
URL = "https://qzucyezcphgwhmuzolqd.supabase.co"
KEY = "sb_publishable_8DoGUldXBlz5Na-qOF_Ezw_9cYdClgL" # මෙතන ANON KEY එක පාවිච්චි කිරීම වඩාත් සුදුසුයි
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Owner Dashboard", layout="wide")
st.title("👑 Charu ERP - Real-time Owner Dashboard")

try:
    # Sales දත්ත ලබා ගැනීම
    res = supabase.table("sales_summary").select("*").execute()
    
    # දත්ත තිබේදැයි පරීක්ෂා කිරීම (මෙය වැදගත්!)
    if res.data:
        df = pd.DataFrame(res.data)
        
        # Summary Metrics
        total_revenue = df['total_amount'].sum()
        st.metric("Total Revenue (All Time)", f"Rs. {total_revenue:,.2f}")
        
        # Transactions Table
        st.subheader("විකුණුම් ලේඛනය (Sales Log)")
        st.dataframe(df.sort_values(by='bill_date', ascending=False), use_container_width=True)
    else:
        st.info("දත්ත කිසිවක් හමු නොවීය. විකුණුම් සිදු කළ පසු මෙතැන දිස් වනු ඇත.")

except Exception as e:
    st.error(f"Database එකට සම්බන්ධ වීමේ ගැටලුවක්: {e}")