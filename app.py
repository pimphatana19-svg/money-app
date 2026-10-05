import math
from collections import Counter
from datetime import datetime
import streamlit as st

# ==========================================
# 1. Page Configuration & Pastel Theme Design
# ==========================================
st.set_page_config(
    page_title="Savings & Store Manager App", page_icon="🌸", layout="centered"
)

# Custom CSS for Soft Pastel Pink Aesthetic (#FFF0F5)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: #FFFFFF;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #D87093 !important;
    }
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 10px;
        border-left: 4px solid #FFB6C1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 2. State Initialization
# ==========================================
if "savings" not in st.session_state:
    st.session_state.savings = {}

if "grocery_sales" not in st.session_state:
    st.session_state.grocery_sales = []

if "luxury_sales" not in st.session_state:
    st.session_state.luxury_sales = []

# ==========================================
# 3. Sidebar Navigation Menu
# ==========================================
st.sidebar.title("Navigation Menu")
menu = st.sidebar.radio(
    "Select Feature:",
    [
        "Savings Tracker System",
        "Grocery Store System",
        "Luxury Store System",
    ],
)

# ==========================================
# Feature 1: Savings Tracker System
# ==========================================
if menu == "Savings Tracker System":
    st.title("Savings Tracker System")

    tab1, tab2 = st.tabs(["Savings Summary", "Create Savings Goal"])

    with tab1:
        st.subheader("All Savings Goals")
        if not st.session_state.savings:
            st.info("No savings goal found. Please create one in the next tab.")
        else:
            for goal_name, data in st.session_state.savings.items():
                with st.expander(f"Goal: {goal_name}", expanded=True):
                    col1, col2 = st.columns(2)
                    col1.metric("Participants (n)", f"{data['n']} people")
                    col1.metric("Deposit per Person/Time (z)", f"{data['z']:,.2f} Baht")
                    col2.metric("Target Total (x)", f"{data['x']:,.2f} Baht")

                    days = math.ceil((data["x"] / (data["z"] * data["n"])) * data["w"])
                    col2.metric("Estimated Days to Complete", f"{days} Days")
                    st.caption(f"Members: {data['names']}")

    with tab2:
        st.subheader("New Savings Goal")
        acc_name = st.text_input("Goal Title:")
        n = st.number_input("Number of participants (n):", min_value=1, value=1)
        names = st.text_input("Member Names (separated by comma):")
        w = st.number_input("Deposit frequency in days (w) (e.g. 1 = Daily):", min_value=1, value=1)

        mode = st.radio(
            "Target Goal Type:",
            ["Define Total Target Amount (x)", "Define Target Days (y)"],
        )

        if mode == "Define Total Target Amount (x)":
            x = st.number_input("Total Target Amount (x) in Baht:", value=1000.0)
            z = x / n if n > 0 else 0
        else:
            y = st.number_input("Target Duration in Days (y):", value=30)
            z = st.number_input("Deposit per Person per Time (z) in Baht:", value=50.0)
            x = (y * z) * n

        if st.button("Save Savings Goal"):
            if acc_name:
                st.session_state.savings[acc_name] = {
                    "n": n,
                    "names": names,
                    "w": w,
                    "z": z,
                    "x": x,
                }
                st.success(f"Goal '{acc_name}' created successfully!")
                st.rerun()
            else:
                st.warning("Please enter a Goal Title.")

# ==========================================
# Feature 2 & 3: Grocery and Luxury Store System
# ==========================================
else:
    is_luxury = menu == "Luxury Store System"
    store_title = "Luxury Store Management" if is_luxury else "Grocery Store Management"
    sales_list = st.session_state.luxury_sales if is_luxury else st.session_state.grocery_sales

    st.title(store_title)

    tab1, tab2 = st.tabs(["Record Sales", "Analytics Dashboard"])

    with tab1:
        st.subheader("Add Sale Entry")
        col1, col2 = st.columns(2)
        date_val = col1.date_input("Date:", datetime.now())
        time_val = col2.number_input("Hour (0-23):", min_value=0, max_value=23, value=12)

        category = col1.text_input("Category:")
        product_name = col2.text_input("Product Name:")

        cost = col1.number_input("Cost (Baht):", min_value=0.0, value=10.0)
        price = col2.number_input("Price (Baht):", min_value=0.0, value=20.0)

        if st.button("Add Record"):
            if product_name:
                sales_list.append(
                    {
                        "date": str(date_val),
                        "time": time_val,
                        "category": category,
                        "product_name": product_name,
                        "cost": cost,
                        "price": price,
                    }
                )
                st.success("Sale entry recorded successfully!")
            else:
                st.warning("Please enter Product Name.")

        if sales_list:
            st.divider()
            st.subheader("Sales History Table")
            st.dataframe(sales_list, use_container_width=True)

    with tab2:
        st.subheader("Analytics Dashboard")
        if not sales_list:
            st.info("No sales data available. Add sales records in the first tab.")
        else:
            total_profit = sum(item["price"] - item["cost"] for item in sales_list)
            col1, col2 = st.columns(2)
            col1.metric("Total Profit", f"{total_profit:,.2f} Baht")

            times = [item["time"] for item in sales_list]
            peak_hour = Counter(times).most_common(1)[0][0]
            col2.metric("Peak Sales Hour", f"{peak_hour}:00 Hrs")

            products = [item["product_name"] for item in sales_list]
            top_p = Counter(products).most_common(1)[0]
            st.metric("Top Selling Product", f"{top_p[0]} ({top_p[1]} sold)")

            prices = sorted([item["price"] for item in sales_list])
            if is_luxury:
                n_p = len(prices)
                median = (
                    prices[n_p // 2]
                    if n_p % 2 != 0
                    else (prices[n_p // 2 - 1] + prices[n_p // 2]) / 2
                )
                st.metric("Median Purchase Price", f"{median:,.2f} Baht")

            st.write("### Inventory Restock Recommendations")
            top_stock = Counter(products).most_common(3)
            for rank, (p_name, count) in enumerate(top_stock, 1):
                st.write(f"- **Rank {rank}:** {p_name} ({count} sold)")
          
