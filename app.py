import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Indian Census Data Visualization (2001–2011)")

# Load dataset
df = pd.read_csv("Indian census")  # replace with your merged file

# Calculate growth rate if not already present
if "Growth_rate" not in df.columns:
    df['Growth_rate'] = ((df['Population in 2011'] - df['Population in 2001'])
                         / df['Population in 2001']) * 100

# Sidebar filter
states = df['state'].unique()
selected_state = st.sidebar.selectbox("Select a State", states)

# Filter dataframe
filtered_df = df[df['state'] == selected_state]


# Plotly scatter mapbox
fig = px.scatter_map(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Population in 2011",
    color="Growth_rate",
    hover_name="District",
    hover_data=["state", "Population in 2001", "Population in 2011", "Growth_rate"],
    zoom=4,
    size_max=35,
    map_style="carto-positron",
    width=1200,
    height=700
)

# Show chart in Streamlit
st.plotly_chart(fig)

# --- Bar Chart Visualization ---
st.subheader(f"Population Growth Rate by District in {selected_state}")
fig_bar = px.bar( filtered_df.sort_values("Growth_rate", ascending=False).head(10),
                  x="District",
                  y="Growth_rate",
                  color="Growth_rate",
                  color_continuous_scale="Viridis",
                  title=f"Growth Rate Comparison for Districts in {selected_state}" )

st.plotly_chart(fig_bar)

# Extra: Top 10 districts by growth rate
st.subheader(f"Top 10 Districts by Growth Rate in {selected_state}")
top10 = filtered_df.sort_values("Growth_rate", ascending=False).head(10)
st.dataframe(top10[['District', 'Growth_rate']])

# --- Cross-State Comparison ---
st.subheader("Cross-State Growth Rate Comparison")

state_growth = df.groupby("state").apply(
    lambda x: ((x["Population in 2011"].sum() - x["Population in 2001"].sum())
               / x["Population in 2001"].sum()) * 100
).reset_index(name="Growth_rate")

fig_state_bar = px.bar(
    state_growth.sort_values("Growth_rate", ascending=False),
    x="state",
    y="Growth_rate",
    color="Growth_rate",
    color_continuous_scale="Viridis",
    title="Population Growth Rate by State (2001–2011)"
)
st.plotly_chart(fig_state_bar)

# line chart for state wise population trend

st.subheader("Population Trend (2001 vs 2011)")
trend_df = df.groupby("state")[["Population in 2001", "Population in 2011"]].sum().reset_index()
fig_line = px.line(
    trend_df.melt(id_vars="state", var_name="Year", value_name="Population"),
    x="Year",
    y="Population",
    color="state",
    title="State-wise Population Trend"
)
st.plotly_chart(fig_line)

# scatter plot of growth vs population size

st.subheader("Growth Rate vs Population Size")
fig_scatter = px.scatter(
    df,
    x="Growth_rate",
    y="Population in 2011",
    color="state",
    hover_name="District",
    title="District Growth Rate vs Population Size"
)
st.plotly_chart(fig_scatter)
