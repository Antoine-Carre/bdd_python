import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date

st.image('https://soliguide.fr/assets/images/logo.png',width=600)

df = pd.read_csv("./data_csv/fiche_figure1.csv")
s = pd.read_csv("./data_csv/searchWithDatePresentation2.csv")


# Define department
TerritoireSoliguide = ['06', '33', '44', '67', '75','77', '78','91', '92', '93', '94', '95']
TerrG = ["général"] + TerritoireSoliguide

st.write('Sélectionnez votre secteur :')
TerrG = st.selectbox('', TerrG)

if TerrG=='général':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies général', 'En ligne général', 'Brouillon général', 'Reservées aux pros général',
                     'Mise à jour général', 'Fiches reliées aux comptes pros général'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies général cumulé', 'En ligne général cumulé', 'Brouillon général cumulé', 'Reservées aux pros général cumulé',
                                            'Mise à jour général cumulé',  'Fiches reliées aux comptes pros général cumulé'])

    s1 = s.filter(regex='général')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])

if TerrG=='06':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:06)','En ligne (dep:06)', 'En brouillon (dep:06)','Mise à jour (dep:06)', 
                                                    'Fiches reliées aux comptes pros (dep:06)'])                                         
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:06) cumulé', 'En ligne (dep:06) cumulé', 'En brouillon (dep:06) cumulé', 
                                            'Mise à jour (dep:06) cumulé',  'Fiches reliées aux comptes pros (dep:06) cumulé'])

    s1 = s.filter(regex='06')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])

if TerrG=='33':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:33)','En ligne (dep:33)', 'En brouillon (dep:33)','Mise à jour (dep:33)', 
                                                    'Fiches reliées aux comptes pros (dep:33)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:33) cumulé', 'En ligne (dep:33) cumulé', 'En brouillon (dep:33) cumulé', 
                                            'Mise à jour (dep:33) cumulé',  'Fiches reliées aux comptes pros (dep:33) cumulé'])

    s1 = s.filter(regex='33')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])

if TerrG=='44':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:44)','En ligne (dep:44)', 'En brouillon (dep:44)','Mise à jour (dep:44)', 
                                                    'Fiches reliées aux comptes pros (dep:44)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:44) cumulé', 'En ligne (dep:44) cumulé', 'En brouillon (dep:44) cumulé', 
                                            'Mise à jour (dep:44) cumulé',  'Fiches reliées aux comptes pros (dep:44) cumulé'])    

    s1 = s.filter(regex='44')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='67':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:67)','En ligne (dep:67)', 'En brouillon (dep:67)','Mise à jour (dep:67)', 
                                                    'Fiches reliées aux comptes pros (dep:67)'])         
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:67) cumulé', 'En ligne (dep:67) cumulé', 'En brouillon (dep:67) cumulé', 
                                            'Mise à jour (dep:67) cumulé',  'Fiches reliées aux comptes pros (dep:67) cumulé'])     

    s1 = s.filter(regex='67')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='75':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:75)','En ligne (dep:75)', 'En brouillon (dep:75)','Mise à jour (dep:75)', 
                                                    'Fiches reliées aux comptes pros (dep:75)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:75) cumulé', 'En ligne (dep:75) cumulé', 'En brouillon (dep:75) cumulé', 
                                            'Mise à jour (dep:75) cumulé',  'Fiches reliées aux comptes pros (dep:75) cumulé'])      

    s1 = s.filter(regex='75')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                           

if TerrG=='77':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:77)','En ligne (dep:77)', 'En brouillon (dep:77)','Mise à jour (dep:77)', 
                                                    'Fiches reliées aux comptes pros (dep:77)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:77) cumulé', 'En ligne (dep:77) cumulé', 'En brouillon (dep:77) cumulé', 
                                            'Mise à jour (dep:77) cumulé',  'Fiches reliées aux comptes pros (dep:77) cumulé'])    

    s1 = s.filter(regex='77')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='78':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:78)','En ligne (dep:78)', 'En brouillon (dep:78)','Mise à jour (dep:78)', 
                                                    'Fiches reliées aux comptes pros (dep:78)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:78) cumulé', 'En ligne (dep:78) cumulé', 'En brouillon (dep:78) cumulé', 
                                            'Mise à jour (dep:78) cumulé',  'Fiches reliées aux comptes pros (dep:78) cumulé'])    

    s1 = s.filter(regex='78')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='91':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:91)','En ligne (dep:91)', 'En brouillon (dep:91)','Mise à jour (dep:91)', 
                                                    'Fiches reliées aux comptes pros (dep:91)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:91) cumulé', 'En ligne (dep:91) cumulé', 'En brouillon (dep:91) cumulé', 
                                            'Mise à jour (dep:91) cumulé',  'Fiches reliées aux comptes pros (dep:91) cumulé'])     

    s1 = s.filter(regex='91')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                           

if TerrG=='92':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:92)','En ligne (dep:92)', 'En brouillon (dep:92)','Mise à jour (dep:92)', 
                                                    'Fiches reliées aux comptes pros (dep:92)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:92) cumulé', 'En ligne (dep:92) cumulé', 'En brouillon (dep:92) cumulé', 
                                            'Mise à jour (dep:92) cumulé',  'Fiches reliées aux comptes pros (dep:92) cumulé'])   

    s1 = s.filter(regex='92')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='93':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:93)','En ligne (dep:93)', 'En brouillon (dep:93)','Mise à jour (dep:93)', 
                                                    'Fiches reliées aux comptes pros (dep:93)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:93) cumulé', 'En ligne (dep:93) cumulé', 'En brouillon (dep:93) cumulé', 
                                            'Mise à jour (dep:93) cumulé',  'Fiches reliées aux comptes pros (dep:93) cumulé'])     

    s1 = s.filter(regex='93')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='94':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:94)','En ligne (dep:94)', 'En brouillon (dep:94)','Mise à jour (dep:94)', 
                                                    'Fiches reliées aux comptes pros (dep:94)'])    
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:94) cumulé', 'En ligne (dep:94) cumulé', 'En brouillon (dep:94) cumulé', 
                                            'Mise à jour (dep:94) cumulé',  'Fiches reliées aux comptes pros (dep:94) cumulé'])     

    s1 = s.filter(regex='94')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                            

if TerrG=='95':
    fig1 = px.line(df, x="Date_saisie", y=['Suivies (dep:95)','En ligne (dep:95)', 'En brouillon (dep:95)','Mise à jour (dep:95)', 
                                                    'Fiches reliées aux comptes pros (dep:95)'])
    figBar = px.bar(df, x="Date_saisie",y=['Suivies (dep:95) cumulé', 'En ligne (dep:95) cumulé', 'En brouillon (dep:95) cumulé', 
                                            'Mise à jour (dep:95) cumulé',  'Fiches reliées aux comptes pros (dep:95) cumulé'])      
    s1 = s.filter(regex='95')
    s1 = pd.merge(s['Unnamed: 0'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='Unnamed: 0', y=s1.columns.values.tolist()[1:])                                               

fig1.update_xaxes(title_text="Date de création (de la fiche ou du compte pro de la fiche) ou date de la dernière mise à jour de la fiche", title_standoff=0.6, title_font_family="Times New Roman")
fig1.update_yaxes(title_text="Nombre de fiches (non cumulé)", title_font_family="Times New Roman")


annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                            xanchor='center', yanchor='top',
                            font=dict(family='Arial',
                                      size=12,
                                      color='rgb(150,150,150)'),
                            showarrow=False)
fig1.update_traces( mode='lines+markers', hovertemplate=None)
fig1.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])

figBar.update_xaxes(title_text="Date de création (de la fiche ou du compte pro de la fiche) ou date de la dernière mise à jour de la fiche", title_standoff=0.6, title_font_family="Times New Roman")
figBar.update_yaxes(title_text="Nombre de fiches (non cumulé)", title_font_family="Times New Roman")


annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                            xanchor='center', yanchor='top',
                            font=dict(family='Arial',
                                      size=12,
                                      color='rgb(150,150,150)'),
                            showarrow=False)
figBar.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])

figSearch.update_xaxes(title_text="Date des recherches", title_standoff=0.6, title_font_family="Times New Roman")
figSearch.update_yaxes(title_text="Nombre de recherches (non cumulé)", title_font_family="Times New Roman")

annotationsSearch = dict(xref='paper', yref='paper', x=0.055, y=1,
                                xanchor='center', yanchor='top',
                                font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                                showarrow=False)
figSearch.update_traces( mode='lines+markers', hovertemplate=None)
figSearch.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotationsSearch])

st.plotly_chart(fig1, use_container_width=True)

st.plotly_chart(figBar, use_container_width=True)

st.plotly_chart(figSearch, use_container_width=True)


