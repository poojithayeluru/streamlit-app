import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

file_dir=os.path.dirname(os.path.abspath(__file__))


parent_dir=os.path.join(file_dir,os.pardir)

dir_of_interest=os.path.join(parent_dir,"resources")

image_path=os.path.join(dir_of_interest,"images","diamond.jpg")
data_path=os.path.join(dir_of_interest,"data","diamonds.csv")
st.title("Daimonds DataSet")
img=image.imread(image_path)
st.image(img,width=500)

df=pd.read_csv(data_path)
st.dataframe(df)


color=st.selectbox("Select the color:", df["color"].unique())

col1,col2=st.columns(2)

fig1=px.bar(df[df["color"]==color],x="cut")
col1.plotly_chart(fig1,use_container_width=True,title="Cut vs Color")

fig2=px.histogram(df[df["color"]==color],x="carat",nbins=20)
col2.plotly_chart(fig2,use_container_width=True,title="Distribution of color vs carat")

fig3=px.box(df[df["color"]==color],x="depth")
col1.plotly_chart(fig3,use_container_width=True,title="Color Vs depth")

fig4=px.scatter(df,x="x",y="y")
col2.plotly_chart(fig4,use_container_width=True,title="Relation between X,Y")