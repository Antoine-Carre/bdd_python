import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date
import streamlit.components.v1 as components

# option
st.set_page_config(page_title="Base de données - Décembre 2021",
                   page_icon="🚀",
                   layout="wide",)

st.image('https://soliguide.fr/assets/images/logo.png',width=600)

st.write("[Lien vers la documentation et les explications](https://www.notion.so/Suivi-des-indicateurs-mensuels-process-b285b4b9bb3b48f997f7cd8b728605d1)")
st.write("[Lien vers les chiffres](https://airtable.com/appfuLygVTjBO0qk1/tblnFpLaXocYAgoxG/viwXZ2ZkTM5pwPa8Q?blocks=hide)")


df = pd.read_csv("./data_csv/fiche_figure1.csv")
df = df.iloc[:-1]

s = pd.read_csv("./data_csv/searchWithDatePresentation3.csv")
s = s[s.datePresentation != "2022-02-01"]

compteProCum = pd.read_csv("./data_csv/orga_figure3.csv")
compteProCum = compteProCum[compteProCum.createdAt != "2022-02"]

df4 = pd.read_csv("data_csv/GAdata.csv")
df4 = df4[df4['Unnamed: 0'] != "du 2022-02-01 au 2022-03-01"]	

df_history_data_grp = pd.read_csv("./data_csv/mise_a_jour.csv")
df_history_data_grp = df_history_data_grp[df_history_data_grp.monthly != "2022-02"]
df_history_data_grp.rename(columns={'status_ADMIN_SOLIGUIDE':'Equipe Solinum',
                                   'status_ADMIN_TERRITORY':'Equipe territoriale',
                                   'status_PRO':'Les acteurs'}, inplace=True)

df_maj_3_months = pd.read_csv("data_csv/mise_a_jour_3_mois.csv")
df_maj_3_months.set_index('territoire', inplace=True)

df_maj_6_months = pd.read_csv("data_csv/mise_a_jour_6_mois.csv")
df_maj_6_months.set_index('territoire', inplace=True)

HtmlFile = open("./data_csv/map.html", 'r', encoding='utf-8')

HtmlFile_2 = open("./data_csv/search_map.html", 'r', encoding='utf-8')


# Define department
TerritoireSoliguide = ['06', '07','13','15','16','21', '33','34','35','36', '44','59','63', '67', '75','76','77', '78','91', '92', '93', '94', '95']
TerrG = ["général"] + TerritoireSoliguide

st.write('Sélectionnez votre secteur :')
TerrG = st.selectbox('', TerrG)

if TerrG=='général':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies général', 'En ligne général', 'Brouillon général', 'Reservées aux pros général','Mise à jour général', 'Fiches reliées aux comptes pros général'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies général cumulé', 'En ligne général cumulé', 'Brouillon général cumulé', 'Reservées aux pros général cumulé',
                                            'Mise à jour général cumulé',  'Fiches reliées aux comptes pros général cumulé'])

    s1 = s.filter(regex='général')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])

    s1_cum = s1[['datePresentation','Recherches général']]
    s1_cum['Recherches général cumulé'] = s1_cum['Recherches général'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches général cumulé'])
        
    figComptePro = px.bar(compteProCum, x='datePresentation', y='Général cumulé')

    fig6 = px.bar(df_history_data_grp.groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Total','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Total','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """


# First batch    
if TerrG=='06' or TerrG=='33' or  TerrG=='13'or TerrG=='44' or TerrG=='67' or TerrG=='75' or TerrG=='77' or TerrG=='78' or TerrG=='91' or TerrG=='92' or TerrG=='93' or TerrG=='94' or TerrG=='95':

    fig1 = px.line(df, x="Unnamed: 0", y=[f'Suivies (dep:{TerrG})',f'En ligne (dep:{TerrG})', f'En brouillon (dep:{TerrG})',f'Mise à jour (dep:{TerrG})', 
                                                    f'Fiches reliées aux comptes pros (dep:{TerrG})'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=[f'Suivies (dep:{TerrG}) cumulé', f'En ligne (dep:{TerrG}) cumulé', f'En brouillon (dep:{TerrG}) cumulé', 
                                            f'Mise à jour (dep:{TerrG}) cumulé',  f'Fiches reliées aux comptes pros (dep:{TerrG}) cumulé'])

    s1 = s.filter(regex=TerrG)
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation',f'Recherches dep({TerrG})']]
    s1_cum[f'Recherches dep({TerrG}) cumulé'] = s1_cum[f'Recherches dep({TerrG})'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=[f'Recherches dep({TerrG}) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.territoire == int(TerrG)].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc[f'{TerrG}','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc[f'{TerrG}','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='13' or TerrG=='16' or TerrG=='36' or TerrG=='59' or TerrG=='63' or TerrG=='16':
    df = df[40:]

    fig1 = px.line(df, x="Unnamed: 0", y=[f'Suivies (dep:{TerrG})',f'En ligne (dep:{TerrG})', f'En brouillon (dep:{TerrG})',f'Mise à jour (dep:{TerrG})', 
                                                    f'Fiches reliées aux comptes pros (dep:{TerrG})'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=[f'Suivies (dep:{TerrG}) cumulé', f'En ligne (dep:{TerrG}) cumulé', f'En brouillon (dep:{TerrG}) cumulé', 
                                            f'Mise à jour (dep:{TerrG}) cumulé',  f'Fiches reliées aux comptes pros (dep:{TerrG}) cumulé'])

    s = s[22:]
    s1 = s.filter(regex=TerrG)
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation',f'Recherches dep({TerrG})']]
    s1_cum[f'Recherches dep({TerrG}) cumulé'] = s1_cum[f'Recherches dep({TerrG})'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=[f'Recherches dep({TerrG}) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.territoire == int(TerrG)].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc[f'{TerrG}','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc[f'{TerrG}','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

# Second batch :    
if TerrG=='07' or TerrG=='15' or TerrG=='21' or TerrG=='34' or TerrG=='35' or TerrG=='76':
    df = df[40:]
    fig1 = px.line(df, x="Unnamed: 0", y=[f'Suivies (dep:{TerrG})',f'En brouillon (dep:{TerrG})',f'Mise à jour (dep:{TerrG})'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=[f'Suivies (dep:{TerrG}) cumulé', f'En brouillon (dep:{TerrG}) cumulé', f'Mise à jour (dep:07) cumulé'])

    s = s[22:]
    s1 = s.filter(regex=f'{TerrG}')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation',f'Recherches dep({TerrG})']]
    s1_cum[f'Recherches dep({TerrG}) cumulé'] = s1_cum[f'Recherches dep({TerrG})'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=[f'Recherches dep({TerrG}) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == f'{TerrG}'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    #html_string_1 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Ardèche','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    #"""

    #html_string_2 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Ardèche','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    #"""


fig1.update_xaxes(title_text="Date de création (de la fiche ou du compte pro de la fiche) ou date de la dernière mise à jour de la fiche", title_standoff=0.6, title_font_family="Times New Roman")
fig1.update_yaxes(title_text="Nombre de fiches (non cumulé)", title_font_family="Times New Roman")

annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("3 janvier 2022"),
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
                             text='Fait le: ' + str("3 janvier 2022"),
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
                             text='Fait le: ' + str("3 janvier 2022"),
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
                             text='Fait le: ' + str("3 janvier 2022"),
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


if TerrG=='06' or TerrG=='13'or TerrG=='15'or TerrG=='33' or TerrG=='34'or TerrG=='36'or TerrG=='44' or TerrG=='59' or TerrG=='63' or TerrG=='67' or TerrG=='75' or TerrG=='76' or TerrG=='77' or TerrG=='78' or TerrG=='91' or TerrG=='92' or TerrG=='93' or TerrG=='94' or TerrG=='95':
    st.write('Sélectionnez votre secteur :')
    cumul = [f'{TerrG}', f'{TerrG} cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul==f'{TerrG}':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
      
    if cumul==f'{TerrG} cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']==f'Département {TerrG}'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG=='07'or TerrG=='16'or TerrG=='21' or TerrG=='35':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['07', '07 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='07':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='07')
      
    #if cumul=='07 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='07 cumulé')

    df4 = df4[df4['territoire']==f'Département {TerrG}'].reset_index()
    df4 = df4[15:]
    fig4 = px.line(df4, x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 

if TerrG != '07' and TerrG != '16' and TerrG != '21' and TerrG != '35':
    #Compte Pro
    figComptePro.update_xaxes(title_text="Date d'ajout des comptes pro'", title_standoff=0.6,
                                title_font_family="Times New Roman")
    figComptePro.update_yaxes(title_text="Nombre de comptes pro ",
                                title_font_family="Times New Roman")

    annotationsCompte = dict(xref='paper', yref='paper', x=0.055, y=1,
                                xanchor='center', yanchor='top',
                             text='Fait le: ' + str("3 janvier 2022"),
                                font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                                showarrow=False)
    figComptePro.update_layout(title_font_family="Times New Roman",
                                annotations=[annotationsCompte])
    figComptePro.update_traces(hovertemplate='Mois: %{x}<br> Nbre de comptes pro : %{y}') 

    st.markdown('### Figure 3: Evolution du nombre de comptes professionnels')
    st.plotly_chart(figComptePro, use_container_width=True)

if TerrG != 'général':
  
    fig4.update_xaxes(title_text="Intervalle de temps en mois", title_standoff=0.6, title_font_family="Times New Roman")
    fig4.update_yaxes(title_text="Nombre d'utilisateurs/sessions/pages vues", title_font_family="Times New Roman")
    annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                                 xanchor='center', yanchor='top',
                             text='Fait le: ' + str("3 janvier 2022"),
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


fig6.update_traces(hovertemplate='<br>Nombre de mises à jour :%{y}') 
fig6.update_layout(xaxis_tickformat = '%B %Y')
fig6.update_layout(hovermode="x unified")

if TerrG != '07' and TerrG != '15' and TerrG != '34' and TerrG != '35' and TerrG != '76' and TerrG != '21':

    st.markdown('### Figure 6 : Evolution des mises à jours autonomes')
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown('### Taux de fiches mises à jour depuis moins de 3 mois, et depuis moins de 6 mois')
    col1, col2 = st.columns(2)

    col1.markdown(html_string_1, unsafe_allow_html=True)

    col2.markdown(html_string_2, unsafe_allow_html=True)

# Création de la carte avec pour centre : le centre de la France
st.markdown('### Figure 7: Nombre de recherches sur Soliguide effectuées par commune')
source_code = HtmlFile_2.read() 
components.html(source_code, height = 600)
