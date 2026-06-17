import streamlit as st
from backend import TrackingSystem

st.set_page_config(page_title="SwiftRoute - Tracker", layout="wide")

# Persistent State Management in Streamlit
if "system" not in st.session_state:
    st.session_state.system = TrackingSystem()
    # Pre-loading some dummy records for standard presentation visualization
    st.session_state.system.register_parcel("TRK-001", "Evans Kiprop", "Nairobi", 2)
    st.session_state.system.register_parcel("TRK-002", "Amara Okafor", "Mombasa", 1)
    st.session_state.system.register_parcel("TRK-003", "Brian Omondi", "Kisumu", 3)

sys = st.session_state.system

st.title("📦 SwiftRoute Parcel Delivery Tracking Dashboard")
st.caption("Strathmore University CAT 2 - Data Structures & Algorithms Project")
st.write("---")

# Layout Split
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Admin Operations")
    
    # Form to insert a package (CRUD: Create)
    with st.form("add_parcel_form", clear_on_submit=True):
        st.subheader("Register New Parcel")
        p_id = st.text_input("Tracking ID (Unique Key)")
        p_name = st.text_input("Customer Name")
        p_city = st.text_input("Destination City")
        p_priority = st.selectbox("Priority Tier", options=[1, 2, 3], 
                                  format_func=lambda x: {1: "1 - Urgent", 2: "2 - High", 3: "3 - Normal"}[x])
        submit = st.form_submit_button("Log Package")
        
        if submit:
            if p_id and p_name and p_city:
                if sys.find_by_id(p_id) is not None:
                    st.error("Error: Parcel ID already exists!")
                else:
                    sys.register_parcel(p_id, p_name, p_city, p_priority)
                    st.success(f"Parcel {p_id} safely logged to Hash Map & Queue!")
                    st.rerun()
            else:
                st.error("All entry fields are required.")
