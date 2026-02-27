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

# Extra: Top 10 districts by growth rate
st.subheader(f"Top 10 Districts by Growth Rate in {selected_state}")
top10 = filtered_df.sort_values("Growth_rate", ascending=False).head(10)
st.dataframe(top10[['District', 'Growth_rate']])
