import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="House Price Analyst Dashboard",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    data = pd.read_csv("jakarta_house_cleaning.csv")

    return data


data = load_data()


# =========================================================
# TITLE
# =========================================================

st.title("📊 House Price Analyst Dashboard")

st.write(
    "Interactive dashboard for exploring and analyzing the housing price dataset."
)

st.divider()


# =========================================================
# SIDEBAR FILTER
# =========================================================

st.sidebar.header("🔎 Data Filters")


# City filter
city_options = ["All"] + sorted(
    data["city"]
    .dropna()
    .unique()
    .tolist()
)

selected_city = st.sidebar.selectbox(
    "City",
    city_options
)


# District filter
if selected_city == "All":

    district_options = ["All"] + sorted(
        data["district"]
        .dropna()
        .unique()
        .tolist()
    )

else:

    district_options = ["All"] + sorted(
        data[
            data["city"] == selected_city
        ]["district"]
        .dropna()
        .unique()
        .tolist()
    )


selected_district = st.sidebar.selectbox(
    "District",
    district_options
)


# =========================================================
# APPLY FILTER
# =========================================================

filtered_data = data.copy()


if selected_city != "All":

    filtered_data = filtered_data[
        filtered_data["city"] == selected_city
    ]


if selected_district != "All":

    filtered_data = filtered_data[
        filtered_data["district"] == selected_district
    ]


# =========================================================
# FORMAT RUPIAH
# =========================================================

def format_rupiah_short(value):

    if value >= 1_000_000_000_000:
        return f"Rp {value / 1_000_000_000_000:.1f} Trillion"

    elif value >= 1_000_000_000:
        return f"Rp {value / 1_000_000_000:.1f} Billion"

    elif value >= 1_000_000:
        return f"Rp {value / 1_000_000:.1f} Million"

    elif value >= 1_000:
        return f"Rp {value / 1_000:.1f} Thousand"

    else:
        return f"Rp {value:,.0f}"

# =========================================================
# OVERVIEW
# =========================================================

st.header("🏠 Dataset Overview")


total_house = len(filtered_data)

average_price = filtered_data["price"].mean()

median_price = filtered_data["price"].median()

minimum_price = filtered_data["price"].min()

maximum_price = filtered_data["price"].max()


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "Number of Houses",
        f"{total_house:,}"
    )


with col2:

    st.metric(
        "Price Rate",
        format_rupiah_short(average_price)
    )


with col3:

    st.metric(
        "Median Price",
        format_rupiah_short(median_price)
    )


with col4:

    st.metric(
        "Minimum Price",
        format_rupiah_short(minimum_price)
    )


with col5:

    st.metric(
        "Maximum Price",
        format_rupiah_short(maximum_price)
    )


st.divider()


# =========================================================
# DATA PREVIEW
# =========================================================

st.header("📋 Data Preview")


st.dataframe(
    filtered_data.head(100),
    use_container_width=True
)


st.divider()


# =========================================================
# PRICE DISTRIBUTION
# =========================================================

st.header("💰 Housing Price Distribution")


fig = px.histogram(
    filtered_data,
    x="price",
    nbins=50,
    title="Housing Price Distribution"
)


fig.update_layout(
    xaxis_title="Price",
    yaxis_title="Number of Houses"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# PRICE BY CITY
# =========================================================

st.header("🏙️ Price by City")


city_summary = (
    filtered_data
    .groupby("city")["price"]
    .agg(
        average_price="mean",
        median_price="median",
        total_house="count"
    )
    .reset_index()
    .sort_values(
        "average_price",
        ascending=False
    )
)


fig = px.bar(
    city_summary,
    x="city",
    y="average_price",
    title="Average House Prices by City",
    hover_data=[
        "median_price",
        "total_house"
    ]
)


fig.update_layout(
    xaxis_title="City",
    yaxis_title="Price Rate"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# PRICE BY DISTRICT
# =========================================================

st.header("📍 Price by District")


district_summary = (
    filtered_data
    .groupby("district")["price"]
    .agg(
        average_price="mean",
        median_price="median",
        total_house="count"
    )
    .reset_index()
    .sort_values(
        "average_price",
        ascending=False
    )
)


# Ambil top 20 district
district_top = district_summary.head(20)


fig = px.bar(
    district_top,
    x="average_price",
    y="district",
    orientation="h",
    title="Top 20 Districts by Average Price",
    hover_data=[
        "median_price",
        "total_house"
    ]
)


fig.update_layout(
    xaxis_title="Price Rate",
    yaxis_title="District"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# BUILDING AREA VS PRICE
# =========================================================

st.header("🏠 Building Area vs Price")


fig = px.scatter(
    filtered_data,
    x="building_area",
    y="price",
    color="city",
    hover_data=[
        "district",
        "bed_rooms",
        "bath_rooms",
        "land_area"
    ],
    title="Correlation between Building Area and Price"
)


fig.update_layout(
    xaxis_title="Building Area",
    yaxis_title="Price"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# LAND AREA VS PRICE
# =========================================================

st.header("🌳 Land Area vs Price")


fig = px.scatter(
    filtered_data,
    x="land_area",
    y="price",
    color="city",
    hover_data=[
        "district",
        "bed_rooms",
        "bath_rooms",
        "building_area"
    ],
    title="Correlation between Building Area and Price"
)


fig.update_layout(
    xaxis_title="Land Area",
    yaxis_title="Price"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# BEDROOM ANALYSIS
# =========================================================

st.header("🛏️ Analysis of the Number of Bedrooms")


bedroom_summary = (
    filtered_data
    .groupby("bed_rooms")["price"]
    .agg(
        average_price="mean",
        median_price="median",
        total_house="count"
    )
    .reset_index()
)


fig = px.bar(
    bedroom_summary,
    x="bed_rooms",
    y="average_price",
    title="Average Price Based on Number of Bedrooms",
    hover_data=[
        "median_price",
        "total_house"
    ]
)


fig.update_layout(
    xaxis_title="Number of Bedrooms",
    yaxis_title="Price Rate"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# BATHROOM ANALYSIS
# =========================================================

st.header("🚿 Analysis of the Number of Bathrooms")


bathroom_summary = (
    filtered_data
    .groupby("bath_rooms")["price"]
    .agg(
        average_price="mean",
        median_price="median",
        total_house="count"
    )
    .reset_index()
)


fig = px.bar(
    bathroom_summary,
    x="bath_rooms",
    y="average_price",
    title="Average Price Based on Number of Bathrooms",
    hover_data=[
        "median_price",
        "total_house"
    ]
)


fig.update_layout(
    xaxis_title="Number of Bathrooms",
    yaxis_title="Price Rate"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# CARPORT ANALYSIS
# =========================================================

st.header("🚗 Analysis of Carport")


carport_summary = (
    filtered_data
    .groupby("carport")["price"]
    .agg(
        average_price="mean",
        median_price="median",
        total_house="count"
    )
    .reset_index()
)


fig = px.bar(
    carport_summary,
    x="carport",
    y="average_price",
    title="Average Price Based on Number of Carports",
    hover_data=[
        "median_price",
        "total_house"
    ]
)


fig.update_layout(
    xaxis_title="Number of Carports",
    yaxis_title="Price Rate"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# CORRELATION
# =========================================================

st.header("📈 Numerical Feature Correlation")


numeric_columns = [
    "price",
    "bed_rooms",
    "bath_rooms",
    "carport",
    "land_area",
    "building_area"
]


correlation = (
    filtered_data[numeric_columns]
    .corr()
)


fig = px.imshow(
    correlation,
    text_auto=".2f",
    title="Correlation Matrix"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =========================================================
# SUMMARY TABLE
# =========================================================

st.header("📊 Statistical Summary")


st.dataframe(
    filtered_data[
        numeric_columns
    ].describe().T,
    use_container_width=True
)


# =========================================================
# FOOTER
# =========================================================

st.sidebar.divider()

st.sidebar.caption(
    "House Price Analyst Dashboard"
)

st.sidebar.caption(
    "Built with Python, Pandas, Plotly & Streamlit"
)