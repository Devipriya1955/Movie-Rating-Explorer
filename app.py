import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    file_path = r"C:\Users\devip\Downloads\Python_Mini_Project\archive (2)\imdb4.0.csv"
    try:
        df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip')
    except FileNotFoundError:
        st.error("CSV file not found. Please check the file path.")
        return pd.DataFrame()

    required_cols = ['Score', 'Year', 'Rated']
    if not all(col in df.columns for col in required_cols):
        st.error(f"Missing required columns. Found: {df.columns.tolist()}")
        return pd.DataFrame()

    df['Released_Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')

    return df.dropna(subset=['Score', 'Released_Year', 'Rated'])

df = load_data()

if df.empty:
    st.stop()

st.title("🎬 Movie Rating Explorer (Adapted)")

tab1, tab2, tab3 = st.tabs([
    "Box Plot: Ratings by Rated Category",
    "Line Plot: Scores Over Years",
    "Heatmap: Rated vs Average Score"
])

# Box plot (ratings by Rated category)
with tab1:
    fig1 = px.box(df, x='Rated', y='Score', points='all', color='Rated',
                  title="Movie Scores by Rated Category")
    st.plotly_chart(fig1, use_container_width=True)

# Line plot (average ratings over years)
with tab2:
    df_year = df.groupby('Released_Year')['Score'].mean().reset_index()
    fig2 = px.line(df_year, x='Released_Year', y='Score', markers=True,
                   title="Average Movie Score Over Years")
    st.plotly_chart(fig2, use_container_width=True)

# Heatmap (average Score by Rated)
with tab3:
    # Calculate average Score by Rated
    avg_scores = df.groupby('Rated')['Score'].mean().reset_index()
    
    # For a heatmap, we need a 2D matrix, but we only have one dimension (Rated),
    # so let's make a dummy column to create a 1-row heatmap
    
    avg_scores['dummy'] = 'All Movies'
    
    fig3 = px.imshow(
        avg_scores.pivot(index='dummy', columns='Rated', values='Score'),
        labels=dict(x="Rated Category", y="", color="Avg Score"),
        x=avg_scores['Rated'].unique(),
        y=['All Movies'],
        color_continuous_scale='Viridis',
        title="Heatmap of Average Scores by Rated Category"
    )
    st.plotly_chart(fig3, use_container_width=True)
