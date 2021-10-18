import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date
import streamlit.components.v1 as components

# option
st.set_page_config(page_title="Base de données - Septembre 2021",
                   page_icon="🚀",
                   layout="wide",)

st.image('https://soliguide.fr/assets/images/logo.png',width=600)

st.write("[Lien vers la documentation et les explications](https://www.notion.so/Suivi-des-indicateurs-mensuels-process-b285b4b9bb3b48f997f7cd8b728605d1)")

df = pd.read_csv("./data_csv/fiche_figure1.csv")
s = pd.read_csv("./data_csv/searchWithDatePresentation2.csv")
compteProCum = pd.read_csv("./data_csv/orga_figure3.csv")
df4 = pd.read_csv("data_csv/GAdata.csv")

HtmlFile = open("./data_csv/map.html", 'r', encoding='utf-8')



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
    
    figComptePro = px.bar(compteProCum, x='datePresentation', y='Général cumulé')


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
                             text='Fait le: ' + str("1 octobre 2021"),
                             font=dict(family='Arial',
                                       size=12,
                                       color='rgb(150,150,150)'),
                             showarrow=False)

fig1.update_traces( mode='lines+markers', hovertemplate=None)
fig1.update_layout(xaxis=dict(tickformat="%B %Y"))
fig1.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])

figBar.update_xaxes(title_text="Date de création (de la fiche ou du compte pro de la fiche) ou date de la dernière mise à jour de la fiche", title_standoff=0.6, title_font_family="Times New Roman")
figBar.update_yaxes(title_text="Nombre de fiches (non cumulé)", title_font_family="Times New Roman")


annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("1 octobre 2021"),
                             font=dict(family='Arial',
                                       size=12,
                                       color='rgb(150,150,150)'),
                             showarrow=False)

figBar.update_layout(xaxis=dict(tickformat="%B %Y"))
figBar.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])

figSearch.update_xaxes(title_text="Date des recherches", title_standoff=0.6, title_font_family="Times New Roman")
figSearch.update_yaxes(title_text="Nombre de recherches (non cumulé)", title_font_family="Times New Roman")

annotationsSearch = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("1 octobre 2021"),
                             font=dict(family='Arial',
                                       size=12,
                                       color='rgb(150,150,150)'),
                             showarrow=False)
figSearch.update_traces( mode='lines+markers', hovertemplate=None)
                         
figSearch.update_layout(xaxis=dict(tickformat="%B %Y"))
figSearch.update_layout(hovermode="x", title_font_family="Times New Roman", annotations=[annotationsSearch])

st.markdown('### Figure 1: Nombre de fiches crées par mois ')
st.plotly_chart(fig1, use_container_width=True)

st.markdown('### Figure 1bis: Nombre de fiches crées par mois (cumulé)')
st.plotly_chart(figBar, use_container_width=True)

st.markdown('### Figure 2: Evolution du nombre de recherches sur Soliguide')
st.plotly_chart(figSearch, use_container_width=True)

if TerrG=='06':
    st.write('Sélectionnez votre secteur :')
    cumul = ['06', '06 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='06':
      figComptePro = px.bar(compteProCum, x='datePresentation', y=6)
      
    if cumul=='06 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='06 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 06'], x='Date', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG=='33':
    st.write('Sélectionnez votre secteur :')
    cumul = ['33', '33 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='33':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='33 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='44':
    st.write('Sélectionnez votre secteur :')
    cumul = ['44', '44 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='44':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='44 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='67':
    st.write('Sélectionnez votre secteur :')
    cumul = ['67', '67 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='67':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='67 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='75':
    st.write('Sélectionnez votre secteur :')
    cumul = ['75', '75 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='75':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='75 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='77':
    st.write('Sélectionnez votre secteur :')
    cumul = ['77', '77 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='77':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='77 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='78':
    st.write('Sélectionnez votre secteur :')
    cumul = ['78', '78 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='78':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='78 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

if TerrG=='91':
    st.write('Sélectionnez votre secteur :')
    cumul = ['91', '91 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='91':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='91 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

if TerrG=='92':
    st.write('Sélectionnez votre secteur :')
    cumul = ['92', '92 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='92':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='92 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

if TerrG=='93':
    st.write('Sélectionnez votre secteur :')
    cumul = ['93', '93 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='93':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='93 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

if TerrG=='94':
    st.write('Sélectionnez votre secteur :')
    cumul = ['94', '94 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='94':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='94 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

if TerrG=='95':
    st.write('Sélectionnez votre secteur :')
    cumul = ['95', '95 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='95':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='94 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

#Compte Pro
figComptePro.update_xaxes(title_text="Date d'ajout des comptes pro'", title_standoff=0.6,
                              title_font_family="Times New Roman")
figComptePro.update_yaxes(title_text="Nombre de comptes pro ",
                              title_font_family="Times New Roman")

annotationsCompte = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("1 octobre 2021"),
                             font=dict(family='Arial',
                                       size=12,
                                       color='rgb(150,150,150)'),
                             showarrow=False)
figComptePro.update_layout(title_font_family="Times New Roman",
                               annotations=[annotationsCompte])
figComptePro.update_traces(hovertemplate='Mois: %{x}<br> Nbre de comptes pro : %{y}') 

st.markdown('### Figure 3: Evolution du nombre de comptes professionnels')
st.plotly_chart(figComptePro, use_container_width=True)

fig4.update_xaxes(title_text="Intervalle de temps en mois", title_standoff=0.6, title_font_family="Times New Roman")
fig4.update_yaxes(title_text="Nombre d'utilisateurs/sessions/pages vues", title_font_family="Times New Roman")
annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                       xanchor='center', yanchor='top',
                       font=dict(family='Arial',
                                 size=12,
                                 color='rgb(150,150,150)'),
                       showarrow=False)
fig4.update_traces( mode='lines+markers', hovertemplate=None)
fig4.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])
fig4.update_layout(xaxis=dict(tickformat="%B-%Y"))
fig4.update_layout(hovermode="x unified", title_font_family="Times New Roman", annotations=[annotations])

st.markdown('### Figure 4 : Evolution du nombre d\'utilisateurs, de sessions et pages vues')
st.plotly_chart(fig4, use_container_width=True)

# Création de la carte avec pour centre : le centre de la France
st.markdown('### Figure 5: Nombre de fiches suivies (en ligne et en brouillon) par commune')
source_code = HtmlFile.read() 
components.html(source_code, height = 600)




