#import std libraries

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px


# Write a title
st.title('Book Recommendation Engine for Bookworms')
# st.write("**Starting** the *build* of `penguin` app :penguin: :mag: ")

# # Write data taken from https://allisonhorst.github.io/palmerpenguins/
# st.write("Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)")

# # Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
# st.image("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png")

# # Write heading for Data
# st.header('Data')

# # Read csv file and output a sample of 20 data points
# df = pd.read_csv('data/penguins.csv')
# st.write('Displaying a sample of 20 points in our dataset',df.sample(20))

# # Add a selectbox for species
# species = st.selectbox("Select which species you want",df.species.unique())

# # Display a sample of 20 data points according to the species selected with corresponding title
# st.write(f'Displaying data points of {species}',df[df['species']==species])

# # Plotting seaborn
# fig, ax =plt.subplots()
# # ax = sns.scatterplot(data=df[df['species']==species],x='bill_length_mm',y='flipper_length_mm',hue='species')
# ax = sns.scatterplot(data=df,x='bill_length_mm',y='flipper_length_mm',hue='species')
# st.pyplot(fig)

# # Plotting plotly
# fig = px.scatter(data_frame=df,x='bill_length_mm',y='flipper_length_mm',color='species',animation_frame='species',range_x=[0,100],range_y=[170,250])
# st.plotly_chart(fig)

# # Bar chart count of species per island
# st.bar_chart(df.groupby('island')['species'].count())

# # Maps
# st.map(df)

# # Upload image as input
# img_variable = st.sidebar.file_uploader('Upload an image',type=['png','jpg','svg'])
# from PIL import Image
# if img_variable is not None:
#     st.image(Image.open(img_variable))

# # Upload csv as input
# csv_variable = st.sidebar.file_uploader('Upload a csv file',type=['csv'])
# if csv_variable is not None:
#     df = pd.read_csv(csv_variable)
#     st.write(df)

# # Set a background image
# st.markdown(f"""
# <style>
# .stApp{{
#     background-image: url(https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGVuZ3VpbnN8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60);
#     background-size: cover;
# }}
# </style>
# """,unsafe_allow_html=True)






