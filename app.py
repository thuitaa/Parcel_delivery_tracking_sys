try:
    import streamlit as st
except ImportError:
    raise ImportError("The 'streamlit' package is required to run this app. Install it with: pip install streamlit")

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
    st.write("---")
    st.subheader("Dispatch Management")
    if st.button("🚀 Dequeue & Deliver Next Parcel", use_container_width=True):
        delivered = sys.process_next_delivery()
        if delivered:
            st.balloons()
            st.success(f"Successfully processed and delivered: **{delivered.parcel_id}** bound for **{delivered.city}**!")
            st.rerun()
        else:
            st.warning("The delivery queue is completely empty.")

with col2:
    st.header("System Lookup & Insights")
    
    # Tab views for sorting and searching metrics
    tab1, tab2, tab3 = st.tabs(["🔍 Track & Search", "📋 Priority Sorted Queue", "🗄️ Full Master Ledger"])
    
    with tab1:
        st.subheader("Instant ID Tracking (Hash Map Lookup)")
        search_id = st.text_input("Enter exact Tracking ID:")
        if search_id:
            res = sys.find_by_id(search_id)
            if res:
                st.info(f"**Status:** {res.status} | **Client:** {res.name} | **Destination:** {res.city} | **Priority:** {res.priority}")
            else:
                st.error("No record matches that tracking token.")
                
        st.write("---")
        st.subheader("Broad Criteria Exploration (Linear Search)")
        s_query = st.text_input("Search parameter (Name/City):")
        s_type = st.radio("Search Category", options=["name", "city"])
        if s_query:
            all_items = sys.get_all_parcels()
            from backend import linear_search_parcels
            matches = linear_search_parcels(all_items, s_query, s_type)
            if matches:
                for m in matches:
                    st.warning(f"📌 **{m.parcel_id}** — {m.name} ({m.city}) | Status: {m.status}")
            else:
                st.text("No matching context records located.")

    with tab2:
        st.subheader("Next-in-line Queue View (Quick Sorted)")
        sorted_queue = sys.get_priority_sorted_queue()
        if sorted_queue:
            for i, p in enumerate(sorted_queue):
                if p.status != "Delivered":
                    st.write(f"**{i+1}. [{p.parcel_id}]** Priority {p.priority} ➡️ {p.name} ({p.city}) — Status: `{p.status}`")
        else:
            st.write("No items pending delivery transit cycles.")

    with tab3:
        st.subheader("Global Centralized Database Matrix")
        all_records = sys.get_all_parcels()
        if all_records:
            display_data = [{"ID": r.parcel_id, "Customer": r.name, "Destination": r.city, "Priority": r.priority, "Status": r.status} for r in all_records]
            st.table(display_data)
        else:
            st.text("System database memory register contains zero logs.")