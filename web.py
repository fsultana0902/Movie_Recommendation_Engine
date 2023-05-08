import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as auth
import pandas as pd
import requests
import base64


# login
# names = ("stream", "lit")
# usernames = ("st", "lt")
# passwords = ["abcde","uvxyz"]
# hashed_pwd = pickle.load(open('hashed.pkl', 'rb'))
# authenticator = auth.Authenticate(names, usernames, hashed_pwd, "movie_recommendation_engine", "abc")
#
# name, authentication_status, username = authenticator.login("Login", "main")
#
# if authentication_status is False:
#     st.error("Username or Password is incorrect")
# if authentication_status is None:
#     st.warning("Please enter your username and password")
# if authentication_status:
def add_background(image):
    with open(image, "rb") as image:
        enc_string = base64.b64encode(image.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{enc_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_background('img.jpeg')


def get_poster(movie_id):
    d = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=04aecb59aee36e1d70fa29ee12151ad9&language=en-US'.format(
            movie_id))
    details = d.json()
    return "http://image.tmdb.org/t/p/w500" + details['poster_path']


def recommend(movie):
    index_of_movie = movies[movies.title == movie]['index'].values[0]
    s = similarity[index_of_movie]
    movies_list = sorted(list(enumerate(s)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    movie_posters = []
    genr = []
    tag = []
    ovrvw = []
    sts = []
    cst = []
    dir = []
    for i in movies_list:
        mov_id = movies.iloc[i[0]].id
        rec_movies.append(movies.iloc[i[0]].title)
        movie_posters.append(get_poster(mov_id))
        genr.append(movies.iloc[i[0]].genres)
        tag.append(movies.iloc[i[0]].tagline)
        ovrvw.append(movies.iloc[i[0]].overview)
        sts.append(movies.iloc[i[0]].status)
        cst.append(movies.iloc[i[0]].cast)
        dir.append(movies.iloc[i[0]].director)
    return rec_movies, movie_posters, genr, tag, ovrvw, sts, dir, cst


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('sim.pkl', 'rb'))
st.title('Movie Recommendation Engine')
movie_selected = st.selectbox(
    'Select a movie to watch?',
    movies['title'].values)

if st.button('Recommend'):
    movie_names, posters, genr, taglne, ovr, stss, dr, ct = recommend(movie_selected)
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    with col1:
        st.text(movie_names[0])
        st.image(posters[0])
        st.markdown(f"<p><strong style='color: gold;'>Title : </strong><strong style='color: white;'>{movie_names[0]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Genre : </strong><strong style='color: white;'>{genr[0]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Tagline : </strong><strong style='color: white;'>{taglne[0]}</strong</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Overview : </strong>{ovr[0]}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Status : </strong>{stss[0]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Director : </strong><strong style='color: white;'>{dr[0]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Cast : </strong><strong style='color: white;'>{ct[0]}</strong></p>", unsafe_allow_html=True)
    with col2:
        st.text(movie_names[1])
        st.image(posters[1])
        st.markdown(f"<p><strong style='color: red;'>Title : </strong><strong style='color: white;'>{movie_names[1]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Genre : </strong><strong style='color: white;'>{genr[1]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Tagline : </strong><strong style='color: white;'>{taglne[1]}</p></strong>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Overview : </strong>{ovr[1]}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Status : </strong>{stss[1]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Director : </strong><strong style='color: white;'>{dr[1]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Cast : </strong><strong style='color: white;'>{ct[1]}</strong></p>", unsafe_allow_html=True)
    with col3:
        st.text(movie_names[2])
        st.image(posters[2])
        st.markdown(f"<p><strong style='color: gold;'>Title : </strong><strong style='color: white;'>{movie_names[2]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Genre : </strong><strong style='color: white;'>{genr[2]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Tagline : </strong><strong style='color: white;'>{taglne[2]}</strong></p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Overview : </strong>{ovr[2]}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Status : </strong>{stss[2]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Director : </strong><strong style='color: white;'>{dr[2]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Cast : </strong><strong style='color: white;'>{ct[2]}</strong></p>", unsafe_allow_html=True)
    with col4:
        st.text(movie_names[3])
        st.image(posters[3])
        st.markdown(f"<p><strong style='color: red;'>Title : </strong><strong style='color: white;'>{movie_names[3]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Genre : </strong><strong style='color: white;'>{genr[3]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Tagline : </strong><strong style='color: white;'>{taglne[3]}</strong></p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong >Overview : </strong>{ovr[3]}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Status : </strong>{stss[3]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Director : </strong><strong style='color: white;'>{dr[3]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: red;'>Cast : </strong><strong style='color: white;'>{ct[3]}</strong></p>", unsafe_allow_html=True)
    with col5:
        st.text(movie_names[4])
        st.image(posters[4])
        st.markdown(f"<p><strong style='color: gold;'>Title : </strong><strong style='color: white;'>{movie_names[4]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Genre : </strong><strong style='color: white;'>{genr[4]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Tagline : </strong><strong style='color: white;'>{taglne[4]}</strong></p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Overview : </strong>{ovr[4]}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p><strong>Status : </strong>{stss[4]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Director : </strong><strong style='color: white;'>{dr[4]}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong style='color: gold;'>Cast : </strong><strong style='color: white;'>{ct[4]}</strong></p>", unsafe_allow_html=True)
    #     # with col6:
    #     #     st.text(movie_names[5])
    #     #     st.image(posters[5])
    #     # authenticator.logout("Logout", "sidebar")
    #     # st.sidebar.title(f"Welcome {name}")
