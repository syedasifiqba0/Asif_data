import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Leopards Courier Service - Delivery Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LEOPARDS COLORS
# ============================================================

YELLOW = "#FFD400"
BLACK = "#111111"
DARK_BLACK = "#0B0B0B"
WHITE = "#FFFFFF"
LIGHT_BG = "#F5F5F5"
GRAY = "#666666"
LIGHT_GRAY = "#E5E5E5"


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       APP
       ======================================================== */

    .stApp {{
        background-color: {LIGHT_BG};
        color: {BLACK};
    }}

    .block-container {{
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }}


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {{
        background-color: {DARK_BLACK};
        border-right: 5px solid {YELLOW};
    }}

    section[data-testid="stSidebar"] > div {{
        background-color: {DARK_BLACK};
    }}

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {{
        color: {WHITE} !important;
    }}

    /* Sidebar selectbox */

    section[data-testid="stSidebar"] div[data-baseweb="select"] {{
        background-color: #1A1A1A !important;
        border: 1px solid #444444 !important;
        border-radius: 8px !important;
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] * {{
        color: {WHITE} !important;
    }}

    /* Selected tags */

    section[data-testid="stSidebar"] span[data-baseweb="tag"] {{
        background-color: {YELLOW} !important;
        color: {BLACK} !important;
        border-radius: 5px !important;
    }}

    section[data-testid="stSidebar"] span[data-baseweb="tag"] span {{
        color: {BLACK} !important;
    }}


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1, h2, h3 {{
        color: {BLACK} !important;
    }}

    h2 {{
        font-weight: 800 !important;
        border-bottom: 4px solid {YELLOW};
        padding-bottom: 8px;
    }}


    /* ========================================================
       KPI CARDS
       ======================================================== */

    div[data-testid="stMetric"] {{
        background-color: {WHITE} !important;
        border-radius: 12px !important;
        padding: 18px 20px !important;
        border-top: 6px solid {YELLOW} !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12) !important;
        min-height: 115px !important;
    }}

    div[data-testid="stMetric"]:hover {{
        box-shadow: 0 7px 20px rgba(0,0,0,0.20) !important;
        transform: translateY(-2px);
        transition: 0.2s ease;
    }}

    div[data-testid="stMetricLabel"] {{
        color: #555555 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }}

    div[data-testid="stMetricLabel"] p {{
        color: #555555 !important;
        font-weight: 700 !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {BLACK} !important;
        font-weight: 800 !important;
        font-size: 30px !important;
    }}

    div[data-testid="stMetricValue"] > div {{
        color: {BLACK} !important;
    }}


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    div[data-baseweb="input"] {{
        background-color: {WHITE} !important;
        border-radius: 8px !important;
    }}

    div[data-baseweb="input"] input {{
        color: {BLACK} !important;
    }}

    div[data-baseweb="input"]:focus-within {{
        border: 2px solid {YELLOW} !important;
        box-shadow: 0 0 0 1px {YELLOW} !important;
    }}


    /* ========================================================
       DATAFRAME
       ======================================================== */

    div[data-testid="stDataFrame"] {{
        border: 2px solid {YELLOW};
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
    }}


    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {{
        border: none !important;
        height: 3px !important;
        background-color: {YELLOW} !important;
    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    footer {{
        visibility: hidden;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.html(
    f"""
    <div style="
        background:{BLACK};
        padding:25px 30px;
        border-radius:14px;
        border-left:10px solid {YELLOW};
        margin-bottom:25px;
        box-shadow:0 5px 15px rgba(0,0,0,0.18);
    ">

        <div style="
            color:{YELLOW};
            font-size:32px;
            font-weight:800;
            line-height:1.2;
        ">
            📦 LEOPARDS COURIER SERVICE
        </div>

        <div style="
            color:{WHITE};
            font-size:19px;
            font-weight:500;
            margin-top:8px;
        ">
            Software Requirements & Delivery Management Dashboard
        </div>

        <div style="
            color:#CCCCCC;
            font-size:14px;
            margin-top:7px;
        ">
            Task status &nbsp;•&nbsp;
            Execution timeline &nbsp;•&nbsp;
            Domain-wise requirement tracking
        </div>

    </div>
    """
)


# ============================================================
# DATA
# ============================================================

data = [
    ["Navigator", "MBAG Hub-to-Hub SCREEN CHANGES", "Not Possible", "TBD", "is not practically possible to local navigator", ""],
    ["Navigator", "Requirement – Navigator Dashboard for Outbound / Inbound", "In Progress", "1st Sep 2026", "-", 17],
    ["Navigator", "Requirement – Single Scan Screen for Arrival & Inter Transfer (Master Code)", "QA", "TBD", "-", ""],
    ["Navigator", "Navigator hub to hub status changes", "Required Understanding", "TBD", "-", ""],
    ["Navigator", "Navigator Loading Screen Enhancement", "Required Understanding", "TBD", "-", ""],
    ["Navigator", "Auto Email Notification on Damage/Lost Etc Shipment Status in Navigator", "Required Understanding", "TBD", "-", ""],
    ["Navigator", "User Visibility in Check In / Check Out Entries", "Completed", "TBD", "-", 0],
    ["Navigator", "Prefix Validation Implementation in Navigator", "Required Understanding", "TBD", "-", ""],
    ["Navigator", "Request to Hide Hub-to-Hub Movement Status from Web Tracking", "Not Possible", "TBD", "Required change in LFS", ""],
    ["Navigator", "Destination Field Locking on All Forwarding screens", "In Progress", "1st Sep 2026", "-", 17],
    ["Navigator", "Auto Short Pieces Alert & Email Notification in Navigator", "Required Understanding", "TBD", "-", ""],
    ["Navigator", "Area Type Filter in Route Creation (Navigator)", "Completed", "TBD", "-", 0],
    ["Navigator", "Separate Gatepass Screen with Route Type and Division-Based Enhancements", "In Progress", "17-Aug-2026", "-", 2],
    ["Navigator", "HUB TO HUB MOVEMENT SHOWING ON WEB", "Not Possible", "TBD", "-", ""],
    ["Navigator", "Wrong Destination Dispatching on Navigator", "Required Understanding", "TBD", "NEED SOME STUDY CASES", ""],
    ["Navigator", "MBAG REFORWARD ISSUE", "Completed", "TBD", "-", 0],

    ["OMS 2.0", "Phase 2 changes of Delivery sheet made", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "LMD CHANGES", "Not Possible", "TBD", "LMD Application Task", ""],
    ["OMS 2.0", "Exception Handling of LMD Assigned Shipments", "Not Possible", "TBD", "LMD Application Task", ""],
    ["OMS 2.0", "Monthly QSR Summary Changes", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "Delivery Sheet Format Standardization", "In Progress", "31-Aug-2026", "-", ""],
    ["OMS 2.0", "POD Screen Enhancements", "In Progress", "25-Sep-2026", "-", ""],
    ["OMS 2.0", "Arrival Correction Issue", "In Progress", "30-Sep-2026", "New Feature", ""],
    ["OMS 2.0", "Pcs Handling", "In Progress", "30-Sep-2026", "New Feature", ""],
    ["OMS 2.0", "Multiple Sheet Selection Required", "In Progress", "30-Sep-2026", "(NEW FEATURE) Required proper understanding of the task", ""],
    ["OMS 2.0", "Run Sheet Opening Issue", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "Future Assigning Option in OMS 2.0", "In Progress", "15-Sep-2026", "(NEW FEATURE) Required proper understanding of the task", ""],
    ["OMS 2.0", "During Self Collection delivery updates, an option should be available to upload images", "In Progress", "20-Sep-2026", "(NEW FEATURE) Required proper understanding of the task", ""],
    ["OMS 2.0", "Reason & Tracking Enhancement", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "Issue with Self-Collection Shipment After Delivery Verification Deletion", "Pending", "TBD", "-", ""],
    ["OMS 2.0", "Development Request for Friday/Saturday Close Undelivered Reason Validation", "In Progress", "31-Aug-2026", "(NEW FEATURE) Required proper understanding of the task", ""],
    ["OMS 2.0", "Debriefing Report migrate to OMS 2.0", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "proof of delivery migrate to OMS 2.0", "Pending", "25-Aug-2026", "OLD OMS to NEW OMS", ""],
    ["OMS 2.0", "Terminal status bypass report migrate to OMS 2.0", "Pending", "25-Aug-2026", "OLD OMS to NEW OMS", ""],
    ["OMS 2.0", "Balance Sheet migrate to OMS 2.0", "Pending", "25-Aug-2026", "OLD OMS to NEW OMS", ""],
    ["OMS 2.0", "Mobile Delivery Summary migrate to OMS 2.0", "Pending", "25-Aug-2026", "OLD OMS to NEW OMS", ""],
    ["OMS 2.0", "Return location update form", "Pending", "25-Aug-2026", "OLD OMS to NEW OMS", ""],
    ["OMS 2.0", "Shipper Advice BYPASS", "Completed", "TBD", "-", 0],
    ["OMS 2.0", "Shipper Advice status, Operations team can reassigned/ In-Transfer", "UAT", "TBD", "-", ""],
    ["OMS 2.0", "ADD FILTER ON OVERALL SUMMARY", "Required Understanding", "TBD", "-", ""],
    ["OMS 2.0", "Enhancement Request for Delivery Set 2.0 ? Route Configuration & Reporting", "Not Possible", "TBD", "This task belongs to NAVIGATOR", ""],
    ["OMS 2.0", "Business Requirement Document (BRD) Digital Delivery Verification & Re-Pick Process OMS 2.0 & LMD Application", "Required Understanding", "15-Sep-2026", "(NEW FEATURE) Required proper understanding of the task", ""],
    ["OMS 2.0", "Monthly QSR BUG", "Completed", "TBD", "-", 0],

    ["Power BI", "BI REPORT TEMPLATE", "In Progress", "31-Aug-2026", "-", 17],
    ["ESHIP", "ESHIP DASH BOARD", "Pending", "TBD", "-", ""],

    ["VOMS", "Route Creation – Route Type", "Pending", "TBD", "-", ""],
    ["VOMS", "Vehicle Creation – Prefix Option", "Pending", "TBD", "-", ""],
    ["VOMS", "Vehicle Number Correction After Checkout", "Pending", "TBD", "-", ""],
    ["VOMS", "Route Status Filter", "Pending", "TBD", "-", ""],
    ["VOMS", "Gate Pass Division", "Pending", "TBD", "-", ""],
    ["VOMS", "Route Filtering Based on Selected Location", "Pending", "TBD", "-", ""],
    ["VOMS", "Inbound & Outbound Report Layout", "Pending", "TBD", "-", ""],
    ["VOMS", "Route Segregation in Reports", "Pending", "TBD", "-", ""],
    ["VOMS", 'Rename "Target Vehicle"', "Pending", "TBD", "-", ""],
    ["VOMS", "Alarm Screen Validation", "Pending", "TBD", "-", ""],
    ["VOMS", "Trip Tracking Screen", "Pending", "TBD", "-", ""],
    ["VOMS", "Vehicle Filtering During Gatepass Creation", "Pending", "TBD", "-", ""],
    ["VOMS", "Duplicate Vehicle Registration Validation", "Pending", "TBD", "-", ""],

    ["LMD App & PORTAL ISSUE", "Order Creation Form", "Required Understanding", "TBD", "-", ""],
    ["LMD App & PORTAL ISSUE", "city locking mechanism", "Required Understanding", "TBD", "-", ""],

    ["Ecom", "City Table Automation for Destination Changes", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Re-Attempt KPI Development", "In Progress", "31 Aug 2026", "Responsible Team: BI Tech", 17],
    ["Ecom", "DV Deletion Process Automation in LFS", "QA", "18 Aug 2026", "Responsible Team: Tech", 2],
    ["Ecom", "Shipment Sequencing Mapping Logic – E-Commerce (With/Without Prefix)", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "HUB Pending Report Enhancement for SLA Monitoring & Loss Control", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Final Status Automation for HUB Pending Report", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Operations Forecasting, Capacity & Predictive Analytics Dashboard", "In Progress", "31 Aug 2026", "Responsible Team: BI Tech", ""],
    ["Ecom", "Live Leopard Performance Report & Dashboard – OMS 2.0", "In Progress", "31 Aug 2026", "Responsible Team: BI Tech", 17],
    ["Ecom", "LMD Return Handling – Shipper Integration Enhancements", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Misrouting Control and Resolution", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Cash Portal Enhancement Requirements", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "LMD Enhancement – Add Supporting Screenshot via Gallery", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "POD Visibility Issue on LFS", "Completed", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "BRD – Customer Communication & Call Management System", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Validation Without Arrival and RC Assignment", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Journey Close – UAT Readiness", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "DV Status Locking Mechanism for Short CN", "In Progress", "TBD", "Responsible Team: Tech", ""],
    ["Ecom", "Aging Record at the Time of Processing – OMS", "In Progress", "TBD", "Responsible Team: Tech", ""],
]


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(
    data,
    columns=[
        "Software",
        "Email Subject",
        "Status",
        "Expected Timeline",
        "IT Remarks",
        "Days"
    ]
)


# ============================================================
# DATA CLEANING
# ============================================================

df["Days"] = pd.to_numeric(
    df["Days"],
    errors="coerce"
).fillna(0)

df["Expected Timeline"] = (
    df["Expected Timeline"]
    .astype(str)
    .str.strip()
)

df["Software"] = (
    df["Software"]
    .astype(str)
    .str.strip()
)

df["Status"] = (
    df["Status"]
    .astype(str)
    .str.strip()
)


# ============================================================
# SIDEBAR BRANDING
# ============================================================

st.html(
    f"""
    <div style="
        text-align:center;
        padding:8px 5px 20px 5px;
        border-bottom:2px solid {YELLOW};
        margin-bottom:20px;
    ">

        <div style="
            color:{YELLOW};
            font-size:25px;
            font-weight:800;
        ">
            📦 LEOPARDS
        </div>

        <div style="
            color:{WHITE};
            font-size:13px;
            margin-top:5px;
        ">
            Delivery Management
        </div>

    </div>
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "### 🔎 Dashboard Filters"
)

software_filter = st.sidebar.multiselect(
    "Software / Domain",
    sorted(df["Software"].unique()),
    default=sorted(df["Software"].unique())
)

status_filter = st.sidebar.multiselect(
    "Status",
    sorted(df["Status"].unique()),
    default=sorted(df["Status"].unique())
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    df["Software"].isin(software_filter)
    & df["Status"].isin(status_filter)
].copy()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_tasks = len(filtered_df)

total_domains = filtered_df[
    "Software"
].nunique()

total_days = filtered_df[
    "Days"
].sum()

tbd_tasks = (
    filtered_df["Expected Timeline"]
    .str.upper()
    .eq("TBD")
    .sum()
)

completed_tasks = (
    filtered_df["Status"]
    .str.lower()
    .eq("completed")
    .sum()
)

in_progress_tasks = (
    filtered_df["Status"]
    .str.lower()
    .eq("in progress")
    .sum()
)


# ============================================================
# SUMMARY TITLE
# ============================================================

st.markdown("## 📌 Overall Summary")


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "📋 Total Tasks",
    total_tasks
)

col2.metric(
    "🏢 Total Domains",
    total_domains
)

col3.metric(
    "⏱️ Total Days",
    int(total_days)
)

col4.metric(
    "⚠️ TBD Timeline",
    tbd_tasks
)

col5.metric(
    "✅ Completed",
    completed_tasks
)

col6.metric(
    "🔄 In Progress",
    in_progress_tasks
)


# ============================================================
# PLOTLY THEME
# ============================================================

def apply_leopards_theme(fig):

    fig.update_layout(

        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,

        font=dict(
            color=BLACK,
            family="Arial"
        ),

        title_font=dict(
            color=BLACK,
            size=20,
            family="Arial"
        ),

        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        ),

        xaxis=dict(
            showgrid=False,
            linecolor=BLACK,
            tickfont=dict(
                color=BLACK
            ),
            title_font=dict(
                color=BLACK
            )
        ),

        yaxis=dict(
            gridcolor=LIGHT_GRAY,
            linecolor=BLACK,
            tickfont=dict(
                color=BLACK
            ),
            title_font=dict(
                color=BLACK
            )
        )
    )

    fig.update_traces(
        marker_color=YELLOW,
        marker_line_color=BLACK,
        marker_line_width=1,
        textfont_color=BLACK
    )

    return fig


# ============================================================
# CHART 1
# ============================================================

st.markdown("## 🏢 Tasks by Software / Domain")

software_summary = (
    filtered_df
    .groupby("Software")
    .size()
    .reset_index(name="Tasks")
    .sort_values(
        "Tasks",
        ascending=False
    )
)

fig_software = px.bar(
    software_summary,
    x="Software",
    y="Tasks",
    text="Tasks",
    title="Number of Tasks by Software"
)

fig_software = apply_leopards_theme(
    fig_software
)

fig_software.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_software,
    use_container_width=True
)


# ============================================================
# CHART 2
# ============================================================

st.markdown("## 📊 Status Distribution")

status_summary = (
    filtered_df
    .groupby("Status")
    .size()
    .reset_index(name="Tasks")
    .sort_values(
        "Tasks",
        ascending=False
    )
)

fig_status = px.bar(
    status_summary,
    x="Status",
    y="Tasks",
    text="Tasks",
    title="Task Status Distribution"
)

fig_status = apply_leopards_theme(
    fig_status
)

fig_status.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_status,
    use_container_width=True
)


# ============================================================
# CHART 3
# ============================================================

st.markdown("## 📅 Expected Timeline")

timeline_summary = (
    filtered_df
    .groupby("Expected Timeline")
    .size()
    .reset_index(name="Tasks")
    .sort_values(
        "Tasks",
        ascending=False
    )
)

fig_timeline = px.bar(
    timeline_summary,
    x="Expected Timeline",
    y="Tasks",
    text="Tasks",
    title="Tasks by Expected Timeline"
)

fig_timeline = apply_leopards_theme(
    fig_timeline
)

fig_timeline.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_timeline,
    use_container_width=True
)


# ============================================================
# CHART 4
# ============================================================

st.markdown("## ⏱️ Execution Days by Software")

days_summary = (
    filtered_df
    .groupby("Software")["Days"]
    .sum()
    .reset_index()
    .sort_values(
        "Days",
        ascending=False
    )
)

fig_days = px.bar(
    days_summary,
    x="Software",
    y="Days",
    text="Days",
    title="Total Execution Days by Software"
)

fig_days = apply_leopards_theme(
    fig_days
)

fig_days.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_days,
    use_container_width=True
)


# ============================================================
# DOMAIN SUMMARY
# ============================================================

st.markdown("## 📋 Domain Summary")

domain_summary = (
    filtered_df
    .groupby("Software")
    .agg(
        Total_Tasks=(
            "Email Subject",
            "count"
        ),

        Total_Days=(
            "Days",
            "sum"
        ),

        Completed=(
            "Status",
            lambda x:
            (
                x.str.lower()
                == "completed"
            ).sum()
        ),

        In_Progress=(
            "Status",
            lambda x:
            (
                x.str.lower()
                == "in progress"
            ).sum()
        ),

        TBD_Timeline=(
            "Expected Timeline",
            lambda x:
            (
                x.str.upper()
                == "TBD"
            ).sum()
        )
    )
    .reset_index()
    .sort_values(
        "Total_Tasks",
        ascending=False
    )
)

st.dataframe(
    domain_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TBD TASKS
# ============================================================

st.markdown("## ⚠️ Tasks with TBD Expected Timeline")

tbd_df = filtered_df[
    filtered_df["Expected Timeline"]
    .str.upper()
    .eq("TBD")
].copy()

st.html(
    f"""
    <div style="
        background:{BLACK};
        color:{WHITE};
        padding:14px 18px;
        border-radius:8px;
        border-left:7px solid {YELLOW};
        margin-bottom:12px;
    ">
        <span style="
            color:{YELLOW};
            font-weight:800;
        ">
            Total TBD Tasks:
        </span>

        <span style="
            font-size:20px;
            font-weight:700;
            margin-left:8px;
        ">
            {len(tbd_df)}
        </span>
    </div>
    """
)

st.dataframe(
    tbd_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DETAILED TASK TRACKER
# ============================================================

st.markdown("## 📑 Detailed Task Tracker")

search = st.text_input(
    "🔎 Search Email Subject",
    placeholder="Type a task name or keyword..."
)

if search:

    search_df = filtered_df[
        filtered_df["Email Subject"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ].copy()

else:

    search_df = filtered_df.copy()


st.html(
    f"""
    <div style="
        background:{WHITE};
        padding:10px 15px;
        border-radius:8px;
        border-left:5px solid {YELLOW};
        margin-bottom:10px;
        color:{BLACK};
    ">
        Showing <b>{len(search_df)}</b> task(s)
    </div>
    """
)

st.dataframe(
    search_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.html(
    f"""
    <div style="
        background:{BLACK};
        padding:15px;
        border-radius:8px;
        text-align:center;
        margin-top:20px;
    ">

        <span style="
            color:{YELLOW};
            font-weight:800;
        ">
            📦 LEOPARDS COURIER SERVICE
        </span>

        <span style="
            color:{WHITE};
            margin-left:10px;
        ">
            | Software Requirements & Delivery Management Dashboard
        </span>

    </div>
    """
)
