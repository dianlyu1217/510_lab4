import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
from db import Database

load_dotenv()


def get_data():
    with Database(os.getenv('DATABASE_URL')) as pg:
        pg.create_table()
        return pd.read_sql('SELECT * FROM books', pg.con)


def app():
    st.title('Book Catalog Display')

    data = get_data()

    # price slip
    min_price, max_price = int(data['price'].min()), int(data['price'].max())
    selected_price_range = st.slider("Filter by Price", min_value=min_price, max_value=max_price,
                                     value=(min_price, max_price))
    data = data[(data['price'] >= selected_price_range[0]) & (data['price'] <= selected_price_range[1])]

    # rating select
    unique_ratings = ['All Ratings'] + sorted(data['rating'].unique())
    selected_rating = st.selectbox("Filter by Rating", options=unique_ratings)
    if selected_rating != 'All Ratings':
        data = data[data['rating'] == selected_rating]

    # search
    search_query = st.text_input("Search Books")
    if search_query:
        data = data[data['title'].str.contains(search_query, case=False)]

    # page
    batch_size = st.selectbox("Page Size", options=[10, 20, 50], index=1)
    total_pages = (len(data) - 1) // batch_size + 1
    current_page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1) - 1
    start_idx = current_page * batch_size
    end_idx = start_idx + batch_size
    st.write('total data: ' + str(len(data)))
    st.dataframe(data.iloc[start_idx:end_idx])
    st.write(f"page {current_page + 1} of {total_pages}")


if __name__ == '__main__':
    app()
