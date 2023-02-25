import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import image

st.title(":black[Poojitha Yeluru PortFolio]:princess:")


tab1, tab2, tab3, tab4=st.tabs(["About Me","EducationDetails","Projects","ContactMe"])

with tab1:
    st.header("POOJITHA")
    st.subheader("Iam :blue[*Trainee of*]")
    st.caption("To prove myself Dedicated worthy, and energetic")
    st.caption("as as Data Scientist in a progressive organization")
    st.caption("that gives me scope to apply my knowledge and skills.") 
    st.caption("I wannt to extend my skiils in :blue[IT sector]")   
    
with tab2:
    df=pd.DataFrame([["Bachelors of Technology(B-tech)","Agricultural Engineering","DR.NTR CAE","2022","7.8"],["Intermediate","MPC","Narayana Junior college","2018","9.2"],["SSC","SSC","Ratnam High School","2016","9.5"]],columns=["Qualification","Specaliazation","University","YOP","Grade"])
    st.dataframe(df)
    
with tab3:
    images=["logo.png",  "mysql-tutorial.png"]
    st.image(images  ,caption=["Web Scraping Project", "Mysql project"],width=150)

	
with tab4:
    if st.button("G-mail"):
        st.button("Git-Hub")
        st.button("Linkedin")        
        st.subheader("y.poojitha2000@gmail.com")
        st.caption("Please be free for any queries")
    elif st.button("Git-Hub"):
        st.button("Linkedin")
        st.subheader("https://github.com/poojithayeluru ")
    elif st.button("Linkedin"):
        st.subheader("https://www.linkedin.com/in/poojitha-yeluru-b6224b248/")
        st.caption("Please be free for any queries")
    else:
        st.caption("Have a nice day:full_moon_with_face:")  
        