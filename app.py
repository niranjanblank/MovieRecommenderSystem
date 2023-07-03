import streamlit as st
import pandas as pd
import pickle
from helper_functions import get_recommendations
import random
from st_aggrid import AgGrid, GridOptionsBuilder

movies_dataset = pd.read_csv("dataset/ml-latest-small/movies.csv")
with open('matrices/cosine_sim.pkl','rb') as f:
    cosine_sim = pickle.load(f)

with open('matrices/indices.pkl','rb') as f:
    indices = pickle.load(f)


st.title("Movie Recommender System")
movies_list = st.multiselect(options=movies_dataset["title"], label="Select movie to get recommendations")

recommendations = get_recommendations(movies_list,cosine_sim,indices)
random.shuffle(recommendations)

if len(recommendations) > 0:
    # select only the movie name and genre
    st.header("Your Recommendations")
    recommended_movie_dataframe = movies_dataset.iloc[recommendations][["title","genres"]]
    # Define grid options
    gridOptions = GridOptionsBuilder.from_dataframe(recommended_movie_dataframe)
    gridOptions.configure_pagination(enabled=True,
                                     paginationPageSize=10,
                                     paginationAutoPageSize=False
                                     )
    gridOptions.configure_column("title", header_name="Movie", editable=False)
    gridOptions.configure_column("genres", header_name="Genres", editable=False)
    gridOptions = gridOptions.build()
    AgGrid(recommended_movie_dataframe, gridOptions=gridOptions, fit_columns_on_grid_load=True)

st.divider()
st.markdown("""
Made with :heart: by Niranjan Shah \n
Repo: https://github.com/niranjanblank/MovieRecommenderSystem
""")