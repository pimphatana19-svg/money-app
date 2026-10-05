import pandas as pd
import streamlit as st

# Set page layout and title
st.set_page_config(
    page_title="Store & Finance Management", page_icon="✨", layout="centered"
)

# Custom CSS with 'Prompt' Google Font & Minimal Aesthetic
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', sans-serif !important;
        background-color: #FAF9F6;
        color: #2D3748;
    }

    h1, h2, h3, h4 {
        font-family: 'Prompt', sans-serif !important;
        font-weight: 600 !important;
        color: #1A202C !important;
        text-align: center;
        letter-spacing: -0.5px;
    }

    .stButton>button {
        font-family: 'Prompt', sans-serif !important;
        background-color: #2D3748;
        color: #FFFFFF;
        border-radius: 12px;
        border: 1px solid #2D3748;
        font-weight: 500;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        width: 100%;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }

    .stButton>button:hover {
        background-color: #4A5568;
        color: #FFFFFF;
        border-color: #4A5568;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }

    div[data-testid="stMetricLabel"] {
        font-family: 'Prompt', sans-serif !important;
        color: #718096 !important;
        font-size: 0.9rem !important;
    }

    div[data-testid="stMetricValue"] {
        font-family: 'Prompt', sans-serif !important;
        color: #1A202C !important;
        font-weight: 600 !important;
    }

    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session States
if "page" not in st.session_state:
    st.session_state.page = "home"

if "grocery_items" not in st.session_state:
    st.session_state.grocery_items = [
        {
            "DD/MM/YY": "",
            "HH": 0,
            "ประเภทสินค้า": "",
            "ชนิดสินค้า": "",
            "ราคาทุน": 0.0,
            "ราคาขาย": 0.0,
        }
    ]

if "luxury_items" not in st.session_state:
    st.session_state.luxury_items = [
        {
            "DD/MM/YY": "",
            "HH": 0,
            "ประเภทสินค้า": "",
            "ชนิดสินค้า": "",
            "ราคาทุน": 0.0,
            "ราคาขาย": 0.0,
        }
    ]

if "grocery_submitted" not in st.session_state:
    st.session_state.grocery_submitted = False

if "luxury_submitted" not in st.session_state:
    st.session_state.luxury_submitted = False

if "extra_income" not in st.session_state:
    st.session_state.extra_income = 0.0

if "extra_expenses" not in st.session_state:
    st.session_state.extra_expenses = 0.0


# Helper function to switch pages
def go_to(page_name):
    st.session_state.page = page_name


# ==========================================
# หน้าที่ 1: HOME
# ==========================================
if st.session_state.page == "home":
    st.write(" ")
    st.title("หน้าหลัก (Home)")
    st.caption("ระบบจัดการร้านค้าและบัญชีรายรับ-รายจ่าย")
    st.write("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write(" ")
        if st.button("🛒  ร้านขายของชำ"):
            go_to("grocery")
            st.rerun()

        st.write(" ")
        if st.button("💎  ร้านขายของฟุ่มเฟือย"):
            go_to("luxury")
            st.rerun()

        st.write(" ")
        if st.button("💰  รายรับ-รายจ่าย"):
            go_to("finance")
            st.rerun()

# ==========================================
# หน้าที่ 2: ร้านขายของชำ
# ==========================================
elif st.session_state.page == "grocery":
    st.title("🛒 ร้านขายของชำ")

    if st.button("← กลับหน้าหลัก"):
        go_to("home")
        st.rerun()

    st.write("---")

    if not st.session_state.grocery_submitted:
        st.subheader("📝 กรอกรายการขายสินค้า")

        df_input = pd.DataFrame(st.session_state.grocery_items)
        edited_df = st.data_editor(
            df_input,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "DD/MM/YY": st.column_config.TextColumn(
                    "วันเดือนปี (DD/MM/YY)", default=""
                ),
                "HH": st.column_config.NumberColumn(
                    "เวลา (HH)", min_value=0, max_value=23, default=12
                ),
                "ประเภทสินค้า": st.column_config.TextColumn(
                    "ประเภทสินค้า", default=""
                ),
                "ชนิดสินค้า": st.column_config.TextColumn(
                    "ชนิดสินค้า", default=""
                ),
                "ราคาทุน": st.column_config.NumberColumn(
                    "ราคาทุน", min_value=0.0, default=0.0
                ),
                "ราคาขาย": st.column_config.NumberColumn(
                    "ราคาขาย", min_value=0.0, default=0.0
                ),
            },
        )

        st.write(" ")
        if st.button("Submit"):
            st.session_state.grocery_items = edited_df.to_dict("records")
            st.session_state.grocery_submitted = True
            st.rerun()

    else:
        st.subheader("📊 สรุปผลการประกอบการวันนี้")

        df = pd.DataFrame(st.session_state.grocery_items)

        df = df[
            (df["ชนิดสินค้า"].astype(str).str.strip() != "")
            | (df["ราคาขาย"] > 0)
        ]

        if df.empty:
            st.warning("ไม่มีข้อมูลการขายสำหรับสรุปผล")
        else:
            profit = (df["ราคาขาย"] - df["ราคาทุน"]).sum()
            avg_time = df["HH"].mean() if not df.empty else 0
            top_5 = df["ประเภทสินค้า"].value_counts().head(5)

            col_a, col_b = st.columns(2)
            col_a.metric("กำไรสุทธิ", f"{profit:,.2f} บาท")
            col_b.metric("เวลาที่ลูกค้าเข้าร้าน", f"{avg_time:.1f}:00 น.")

            st.write(" ")
            st.write("### 🏆 สินค้ายอดนิยม 5 อันดับแรก")
            if not top_5.empty:
                for rank, (cat, count) in enumerate(top_5.items(), 1):
                    st.write(
                        f"**อันดับที่ {rank}:** {cat} (ขายได้ {count} รายการ)"
                    )
            else:
                st.write("- ไม่มีข้อมูลประเภทสินค้า")

        st.write(" ")
        if st.button("🔄 กรอกรายการใหม่"):
            st.session_state.grocery_submitted = False
            st.rerun()

# ==========================================
# หน้าที่ 3: ร้านขายของฟุ่มเฟือย
# ==========================================
elif st.session_state.page == "luxury":
    st.title("💎 ร้านขายของฟุ่มเฟือย")

    if st.button("← กลับหน้าหลัก"):
        go_to("home")
        st.rerun()

    st.write("---")

    if not st.session_state.luxury_submitted:
        st.subheader("📝 กรอกรายการขายสินค้า")

        df_input = pd.DataFrame(st.session_state.luxury_items)
        edited_df = st.data_editor(
            df_input,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "DD/MM/YY": st.column_config.TextColumn(
                    "วันเดือนปี (DD/MM/YY)", default=""
                ),
                "HH": st.column_config.NumberColumn(
                    "เวลา (HH)", min_value=0, max_value=23, default=12
                ),
                "ประเภทสินค้า": st.column_config.TextColumn(
                    "ประเภทสินค้า", default=""
                ),
                "ชนิดสินค้า": st.column_config.TextColumn(
                    "ชนิดสินค้า", default=""
                ),
                "ราคาทุน": st.column_config.NumberColumn(
                    "ราคาทุน", min_value=0.0, default=0.0
                ),
                "ราคาขาย": st.column_config.NumberColumn(
                    "ราคาขาย", min_value=0.0, default=0.0
                ),
            },
        )

        st.write(" ")
        if st.button("Submit"):
            st.session_state.luxury_items = edited_df.to_dict("records")
            st.session_state.luxury_submitted = True
            st.rerun()

    else:
        st.subheader("📊 สรุปผลการประกอบการวันนี้")

        df = pd.DataFrame(st.session_state.luxury_items)

        df = df[
            (df["ชนิดสินค้า"].astype(str).str.strip() != "")
            | (df["ราคาขาย"] > 0)
        ]

        if df.empty:
            st.warning("ไม่มีข้อมูลการขายสำหรับสรุปผล")
        else:
            profit = (df["ราคาขาย"] - df["ราคาทุน"]).sum()
            avg_time = df["HH"].mean() if not df.empty else 0
            top_5 = df["ประเภทสินค้า"].value_counts().head(5)

            col_a, col_b = st.columns(2)
            col_a.metric("กำไรสุทธิ", f"{profit:,.2f} บาท")
            col_b.metric("เวลาที่ลูกค้าเข้าร้าน", f"{avg_time:.1f}:00 น.")

            st.write(" ")
            st.write("### 🏆 สินค้ายอดนิยม 5 อันดับแรก")
            if not top_5.empty:
                for rank, (cat, count) in enumerate(top_5.items(), 1):
                    st.write(
                        f"**อันดับที่ {rank}:** {cat} (ขายได้ {count} รายการ)"
                    )
            else:
                st.write("- ไม่มีข้อมูลประเภทสินค้า")

            st.write(" ")
            st.write("### 🏷️ ราคากลางที่ลูกค้าชอบซื้อ")
            cat_group = (
                df.groupby("ประเภทสินค้า")["ราคาขาย"]
                .mean()
                .reset_index()
            )
            for _, row in cat_group.iterrows():
                if str(row["ประเภทสินค้า"]).strip() != "":
                    st.write(
                        f"• **{row['ประเภทสินค้า']}:** {row['ราคาขาย']:,.2f} บาท/ชิ้น"
                    )

        st.write(" ")
        if st.button("🔄 กรอกรายการใหม่"):
            st.session_state.luxury_submitted = False
            st.rerun()

# ==========================================
# หน้าที่ 4: รายรับ-รายจ่าย
# ==========================================
elif st.session_state.page == "finance":
    st.title("💰 รายรับ-รายจ่าย")

    if st.button("← กลับหน้าหลัก"):
        go_to("home")
        st.rerun()

    st.write("---")

    df_g = pd.DataFrame(st.session_state.grocery_items)
    df_l = pd.DataFrame(st.session_state.luxury_items)

    sales_g = df_g["ราคาขาย"].sum() if "ราคาขาย" in df_g else 0.0
    sales_l = df_l["ราคาขาย"].sum() if "ราคาขาย" in df_l else 0.0
    auto_sales_revenue = sales_g + sales_l

    st.info(
        f"💵 ยอดขายสะสมจาก 2 ร้านค้า: **{auto_sales_revenue:,.2f} บาท**"
    )

    st.subheader("📝 กรอกข้อมูลรายรับและรายจ่าย")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.extra_income = st.number_input(
            "รายรับเพิ่มเติม", min_value=0.0, value=st.session_state.extra_income
        )

    with col2:
        st.session_state.extra_expenses = st.number_input(
            "รายจ่าย", min_value=0.0, value=st.session_state.extra_expenses
        )

    total_income = auto_sales_revenue + st.session_state.extra_income
    daily_income = total_income - st.session_state.extra_expenses

    st.write("---")
    st.subheader("📊 สรุปผลรายได้ประจำวัน")
    st.metric("รายได้ประจำวัน", f"{daily_income:,.2f} บาท")
