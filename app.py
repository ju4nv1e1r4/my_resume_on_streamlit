import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import pandas as pd
import numpy as np

import config


def main():
    
    frame1, frame2 = st.columns(2)
    
    with frame1:
        st.markdown('### Olá, seja _bem-vindo_! :sunglasses:    ')
        st.image(config.info.photo)
        st.caption('Você pode me contatar através de:')
        st.markdown(config.info.phone)
        st.markdown(config.info.mail)
        st.markdown(config.info.github)
        st.markdown(config.info.medium)
        st.markdown(config.info.linkedin)

        st.markdown('>### **Educação**')
        st.markdown(config.education.faculdade)
        st.markdown(config.education.status)
        st.markdown(config.education.curso)
        st.markdown(config.education.periodo)

        st.markdown('>### **Experiências**')

        st.markdown(config.vocaliza.employee)
        st.markdown(config.vocaliza.cargo)
        st.markdown(config.vocaliza.periodo)
        st.markdown(config.vocaliza.atividade)
        
        st.markdown(config.SouJunior.employee)
        st.markdown(config.SouJunior.cargo)
        st.markdown(config.SouJunior.periodo)
        st.markdown(config.SouJunior.atividade)

        st.markdown(config.JobHome.employee)
        st.markdown(config.JobHome.cargo)
        st.markdown(config.JobHome.periodo)
        st.markdown(config.JobHome.atividade)

       
    with frame2:
        st.markdown(config.info.my_name)
        st.markdown(config.info.about_me)
        st.divider()

        df_hs = pd.DataFrame(dict(
            r = [3, 3, 2, 1, 2, 4, 4, 
                 2, 2, 3, 1, 3, 3, 2], 
            theta = config.skills.hard_skills))
        
        fig_hard = px.line_polar(df_hs, r='r', theta='theta', line_close=True)
        fig_hard.update_traces(fill='toself')
        st.markdown('>### Hard Skills :brain:')
        st.plotly_chart(fig_hard)

        df_ss = pd.DataFrame(dict(
            r = [3, 4, 3, 5, 4, 4, 3, 4, 3, 2, 3, 4, 4, 3, 3], 
            theta = config.skills.soft_skills))
        
        fig_soft = px.line_polar(df_ss, r='r', theta='theta', line_close=True)
        fig_soft.update_traces(fill='toself')
        st.markdown('>### Soft Skills :heart:')
        st.plotly_chart(fig_soft)

        st.markdown('>### Projetos')

        st.markdown(config.projects.manufacturing_defects)
        st.markdown(config.projects.etl)
        st.markdown(config.projects.prompt_eng)
        st.markdown(config.projects.lung_cancer_predict)
        st.markdown(config.projects.heart_diseases)



    
main()