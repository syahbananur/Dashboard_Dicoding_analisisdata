import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_order_reviews_df(df):
    order_reviews_df = df.groupby(by="review_score").review_id.nunique().reset_index()
    order_reviews_df.rename(columns={"review_id": "review_count"}, inplace=True)
    
    return order_reviews_df

def create_customer_city_df(df):
    count_customer_city_df = df.customer_city.value_counts()
    customer_city_df = count_customer_city_df.head(5).reset_index()
    customer_city_df.columns = ["customer_city", "customer_count"]
    
    return customer_city_df

def create_sellers_city_df(df):
    count_sellers_city_df = df.seller_city.value_counts()
    sellers_city_df = count_sellers_city_df.head(5).reset_index()
    sellers_city_df.columns = ["sellers_city", "sellers_count"]
    
    return sellers_city_df

rating = pd.read_csv("order_reviews.csv")
customer_city = pd.read_csv("customer.csv")
sellers_city = pd.read_csv("seller.csv")

rating_df = create_order_reviews_df(rating)
customer_city_df = create_customer_city_df(customer_city)
sellers_city_df = create_sellers_city_df(sellers_city)

st.header('Dashboard Analisis data')
st.subheader('Brazilian E-Commerce Public Dataset')
st.subheader("Kepuasan pelanggan terhadap produk")

plt.figure(figsize=(10, 5))

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"]
plt.title("Kepuasan pelanggan terhadap produk")
plt.bar( x = rating_df["review_score"], height = rating_df["review_count"], color = colors)
plt.ylabel("Jumlah rating")

st.pyplot(plt)

st.subheader("Kota yang ditinggali pelanggan")
plt.figure(figsize=(15, 5))

colors2 = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
plt.title("Kota pelanggan")
plt.bar( x = customer_city_df["customer_city"], height = customer_city_df["customer_count"], color = colors2)
plt.ylabel("Jumlah Pelanggan")


st.pyplot(plt)

st.subheader("Perbandingan antara kota customer dan seller")
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

axes[0].bar(customer_city_df["customer_city"], customer_city_df["customer_count"], color=colors2)
axes[0].set_ylabel("Jumlah customer")
axes[0].tick_params(axis="x")
axes[0].set_title("Kota Customer")

axes[1].bar(sellers_city_df["sellers_city"], sellers_city_df["sellers_count"], color=colors2)
axes[1].set_ylabel("Jumlah Seller")
axes[1].tick_params(axis="x")
axes[1].set_title("Kota seller")

st.pyplot(fig)