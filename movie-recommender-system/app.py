import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    requests.get()

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = movies_list['title'].values

st.title('Movie Recommender System')
selected_movie_name = st.selectbox("Movies list", movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies_list[movies_list['title'].values == movie]
    distances = similarity[int(movie_index.index[0])]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster from API
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies


if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
