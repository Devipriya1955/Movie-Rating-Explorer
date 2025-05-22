# 🎬 Movie Rating Explorer

A Streamlit web app to explore movie ratings based on IMDb data.  
Visualizations include ratings by movie rating category, scores over years, and a heatmap showing ratings distribution.

---

## Features

- **Box Plot**: Visualize movie scores by Rated category (e.g., PG, R).
- **Line Plot**: Track average movie scores over the years.
- **Heatmap**: See how ratings are distributed across Rated categories.

---

## Dataset

This app uses an IMDb dataset (`imdb4.0.csv`). Make sure the CSV file contains the following columns:

- `Score`: Movie rating score
- `Year`: Year of release
- `Rated`: Movie rating category

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie-rating-explorer.git
   cd movie-rating-explorer
