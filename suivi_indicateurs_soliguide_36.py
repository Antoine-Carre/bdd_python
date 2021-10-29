import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date
import streamlit.components.v1 as components

# option
st.set_page_config(page_title="Suivi des indicateurs de la base de données - Octobre 2021",
                   page_icon="https://pbs.twimg.com/profile_images/1321098074765361153/F4UFTeix.png",
                   layout="wide",)

st.image('https://soliguide.fr/assets/images/logo.png',width=600)

df = pd.read_csv("./data_csv/fiche_figure1.csv")
df.rename(columns={"Unnamed: 0": "Date_de_création"}, inplace=True)
df = df[40:]

s = pd.read_csv("./data_csv/searchWithDatePresentation2.csv")
s = s[22:]

compteProCum = pd.read_csv("./data_csv/orga_figure3.csv")
df4 = pd.read_csv("data_csv/GAdata.csv")

HtmlFile = open("./data_csv/Indre_36.html", 'r', encoding='utf-8')


# Define department
TerritoireSoliguide = ['36']

fig1 = px.line(df, x="Date_de_création", y=['Suivies (dep:36)', 'En brouillon (dep:36)','Reservées aux pros (dep:36)', 'Mise à jour (dep:36)','Fiches reliées aux comptes pros (dep:36)'])                                         
figBar = px.bar(df, x="Date_de_création",y=['Suivies (dep:36) cumulé','En brouillon (dep:36) cumulé', 'Reservées aux pros (dep:36) cumulé','Mise à jour (dep:36) cumulé','Fiches reliées aux comptes pros (dep:36) cumulé'])

s1 = s.filter(regex='36')
s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])

    
s1_cum = s1[['datePresentation','Recherches dep(36)']]
s1_cum['Recherches dep(36) cumulé'] = s1_cum['Recherches dep(36)'].cumsum()

fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(36) cumulé'])

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

fig4Bar.update_xaxes(title_text="Date des recherches", title_standoff=0.6, title_font_family="Times New Roman")
fig4Bar.update_yaxes(title_text="Nombre de recherches cumulé", title_font_family="Times New Roman")

titleCompte = {
        'text': 'Figure 2 : Nombre de recherches sur Soliguide cumulé',
        'y': 0.9,
        'x': 0.5,
        'xanchor': "center",
        'yanchor': 'top'}
annotationsSearch = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("1 octobre 2021"),
                             font=dict(family='Arial',
                                       size=12,
                                       color='rgb(150,150,150)'),
                             showarrow=False)

fig4Bar.update_layout(title=titleCompte, title_font_family="Times New Roman",
                               annotations=[annotationsSearch], xaxis_tickformat = '%B %Y')
fig4Bar.update_traces(hovertemplate='Mois: %{x}<br> Nbre de recherches: %{y}') 

st.markdown('### Figure 1: Nombre de fiches crées par mois ')
st.plotly_chart(fig1, use_container_width=True)

st.markdown('### Figure 1bis: Nombre de fiches crées par mois (cumulé)')
st.plotly_chart(figBar, use_container_width=True)

st.markdown('### Figure 2: Evolution du nombre de recherches sur Soliguide')
st.plotly_chart(figSearch, use_container_width=True)

st.plotly_chart(fig4Bar, use_container_width=True)


st.write('Sélectionnez la vue mensuelle ou cumulée :')
cumul = ['Vue mensuelle', 'Vue cumulée']
cumul = st.selectbox('', cumul)

if cumul=='Vue mensuelle':
    figComptePro = px.bar(compteProCum, x='datePresentation', y='36')
if cumul=='Vue cumulée':
    figComptePro = px.bar(compteProCum, x='datePresentation', y='36 cumulé')
    
fig4 = px.line(df4[df4['territoire']=='Département 36'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])

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
                                 text='Fait le: ' + str("1 octobre 2021"),
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

# Création de la carte avec pour centre : le centre de l'Indre
st.markdown('### Figure 5: Nombre de fiches suivies (en ligne et en brouillon) par commune')
source_code = HtmlFile.read() 
components.html(source_code, height = 600)
