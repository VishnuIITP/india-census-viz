# Indian Census Visualization (2001–2011)
This Streamlit app visualizes district-level population growth in India using census data. It combines geospatial centroids with census population figures to provide an interactive map, bar chart comparisons, and insights.

--- ## ✨ Features
- Interactive **map** using Plotly scatter_mapbox
- **Sidebar filter** to explore data state by state
- **Bar chart comparisons** of growth rates across districts
- **Top 10 districts** by growth rate displayed in a table - Easy-to-run Streamlit app with clean UI
- Cross-state growth rate comparison bar chart
- Line chart showing population trends (2001 vs 2011)
- Scatter plot linking growth rate with population size


---

## 📂 Project Structure

project/

│── app.py                # Streamlit app

│── requirements.txt      # Dependencies

│── district_population_centroids.csv  # Dataset (add if included)

│── README.md             # Documentation


---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/VishnuIITP/india-census-viz.git
   cd india-census-viz
2. Install dependencies.
   ```bash
    pip install -r requirements.txt
   
3. Run the app
    ```bash
   streamlit run app.py
   
4. Open the link shown in terminal (usually http://localhost:8501).

📊 Dataset
Source: Indian Census Data with Geospatial Indexing

Contains district-level population data for 2001 and 2011, along with latitude/longitude centroids.

🔮 Future Enhancements
Add district-level filtering

Include bar charts for growth comparisons

Deploy on Streamlit Cloud for public access

👨‍💻 Author
Vishnu Kumar  
Computer Science & Data Analysis, IIT Patna
Passionate about geospatial visualization and data storytelling
