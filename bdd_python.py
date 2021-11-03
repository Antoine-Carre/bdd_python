import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date
import streamlit.components.v1 as components

# option
st.set_page_config(page_title="Base de données - Octobre 2021",
                   page_icon="🚀",
                   layout="wide",)

st.image('https://soliguide.fr/assets/images/logo.png',width=600)

st.write("[Lien vers la documentation et les explications](https://www.notion.so/Suivi-des-indicateurs-mensuels-process-b285b4b9bb3b48f997f7cd8b728605d1)")
st.write("[Lien vers les chiffres](https://airtable.com/appfuLygVTjBO0qk1/tblnFpLaXocYAgoxG/viwXZ2ZkTM5pwPa8Q?blocks=hide)")


df = pd.read_csv("./data_csv/fiche_figure1.csv")
s = pd.read_csv("./data_csv/searchWithDatePresentation3.csv")
compteProCum = pd.read_csv("./data_csv/orga_figure3.csv")
df4 = pd.read_csv("data_csv/GAdata.csv")

df_history_data_grp = pd.read_csv("./data_csv/mise_a_jour.csv")
df_history_data_grp.rename(columns={'status_ADMIN_SOLIGUIDE':'Equipe Solinum',
                                   'status_ADMIN_TERRITORY':'Equipe territoriale',
                                   'status_PRO':'Les acteurs'}, inplace=True)

df_maj_3_months = pd.read_csv("data_csv/mise_a_jour_3_mois.csv")
df_maj_3_months.set_index('departement_x', inplace=True)

df_maj_6_months = pd.read_csv("data_csv/mise_a_jour_6_mois.csv")
df_maj_6_months.set_index('departement_x', inplace=True)
HtmlFile = open("./data_csv/map.html", 'r', encoding='utf-8')

# Define department
TerritoireSoliguide = ['06', '07','13','15','16','21', '33','34','35','36', '44','59','63', '67', '75','76','77', '78','91', '92', '93', '94', '95']
TerrG = ["général"] + TerritoireSoliguide

st.write('Sélectionnez votre secteur :')
TerrG = st.selectbox('', TerrG)

if TerrG=='général':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies général', 'En ligne général', 'Brouillon général', 'Reservées aux pros général',
                     'Mise à jour général', 'Fiches reliées aux comptes pros général'])
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
    
if TerrG=='06':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:06)','En ligne (dep:06)', 'En brouillon (dep:06)','Mise à jour (dep:06)', 
                                                    'Fiches reliées aux comptes pros (dep:06)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:06) cumulé', 'En ligne (dep:06) cumulé', 'En brouillon (dep:06) cumulé', 
                                            'Mise à jour (dep:06) cumulé',  'Fiches reliées aux comptes pros (dep:06) cumulé'])

    s1 = s.filter(regex='06')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(06)']]
    s1_cum['Recherches dep(06) cumulé'] = s1_cum['Recherches dep(06)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(06) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Alpes-Maritimes'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Alpes-Maritimes','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Alpes-Maritimes','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
    
if TerrG=='07':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:07)','En brouillon (dep:07)','Mise à jour (dep:07)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:07) cumulé', 'En brouillon (dep:07) cumulé', 
                                            'Mise à jour (dep:07) cumulé'])

    s1 = s.filter(regex='07')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(07)']]
    s1_cum['Recherches dep(07) cumulé'] = s1_cum['Recherches dep(07)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(07) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Ardèche'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
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

if TerrG=='13':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:13)','En ligne (dep:13)', 'En brouillon (dep:13)','Mise à jour (dep:13)', 
                                                    'Fiches reliées aux comptes pros (dep:13)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:13) cumulé', 'En ligne (dep:13) cumulé', 'En brouillon (dep:13) cumulé', 
                                            'Mise à jour (dep:13) cumulé',  'Fiches reliées aux comptes pros (dep:13) cumulé'])

    s1 = s.filter(regex='13')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(13)']]
    s1_cum['Recherches dep(13) cumulé'] = s1_cum['Recherches dep(13)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(13) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Bouches-du-Rhône'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Bouches-du-Rhône','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Bouches-du-Rhône','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='15':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:15)','En ligne (dep:15)', 'En brouillon (dep:15)','Mise à jour (dep:15)', 
                                                    'Fiches reliées aux comptes pros (dep:15)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:15) cumulé', 'En ligne (dep:15) cumulé', 'En brouillon (dep:15) cumulé', 
                                            'Mise à jour (dep:15) cumulé',  'Fiches reliées aux comptes pros (dep:15) cumulé'])

    s1 = s.filter(regex='15')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(15)']]
    s1_cum['Recherches dep(15) cumulé'] = s1_cum['Recherches dep(15)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(15) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Cantal'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Cantal','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Cantal','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='16':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:16)','En ligne (dep:16)', 'En brouillon (dep:16)','Mise à jour (dep:16)', 
                                                    'Fiches reliées aux comptes pros (dep:16)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:16) cumulé', 'En ligne (dep:16) cumulé', 'En brouillon (dep:16) cumulé', 
                                            'Mise à jour (dep:16) cumulé',  'Fiches reliées aux comptes pros (dep:16) cumulé'])

    s1 = s.filter(regex='16')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(16)']]
    s1_cum['Recherches dep(16) cumulé'] = s1_cum['Recherches dep(16)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(16) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Charente'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Charente','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Charente','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='21':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:21)', 'En brouillon (dep:21)','Mise à jour (dep:21)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:21) cumulé', 'En brouillon (dep:21) cumulé', 
                                            'Mise à jour (dep:21) cumulé'])

    s1 = s.filter(regex='21')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(21)']]
    s1_cum['Recherches dep(21) cumulé'] = s1_cum['Recherches dep(21)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(21) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Côte-d\'Or'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    #html_string_1 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_3_months.loc["Côte-d'Or",'pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    #"""

    #html_string_2 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_6_months.loc["Côte-d'Or",'pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    #"""

if TerrG=='33':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:33)','En ligne (dep:33)', 'En brouillon (dep:33)','Mise à jour (dep:33)', 
                                                    'Fiches reliées aux comptes pros (dep:33)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:33) cumulé', 'En ligne (dep:33) cumulé', 'En brouillon (dep:33) cumulé', 
                                            'Mise à jour (dep:33) cumulé',  'Fiches reliées aux comptes pros (dep:33) cumulé'])

    s1 = s.filter(regex='33')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])

    s1_cum = s1[['datePresentation','Recherches dep(33)']]
    s1_cum['Recherches dep(33) cumulé'] = s1_cum['Recherches dep(33)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(33) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Gironde'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Gironde','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Gironde','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='34':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:34)', 'En brouillon (dep:34)','Mise à jour (dep:34)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:34) cumulé', 'En brouillon (dep:34) cumulé', 'Mise à jour (dep:34) cumulé',])

    s1 = s.filter(regex='34')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(34)']]
    s1_cum['Recherches dep(34) cumulé'] = s1_cum['Recherches dep(34)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(34) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Hérault'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    #html_string_1 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Hérault','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    #"""

    #html_string_2 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Hérault','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    #"""

if TerrG=='35':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:35)', 'En brouillon (dep:35)','Mise à jour (dep:35)'])                                         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:35) cumulé', 'En brouillon (dep:35) cumulé', 'Mise à jour (dep:35) cumulé'])

    s1 = s.filter(regex='35')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])
    
    s1_cum = s1[['datePresentation','Recherches dep(35)']]
    s1_cum['Recherches dep(35) cumulé'] = s1_cum['Recherches dep(35)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(35) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Ille-et-Vilaine'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    #html_string_1 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Ille-et-Vilaine','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    #"""

    #html_string_2 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Ille-et-Vilaine','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    #"""

if TerrG=='36':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:36)','En ligne (dep:36)', 'En brouillon (dep:36)','Mise à jour (dep:36)', 
                                                    'Fiches reliées aux comptes pros (dep:36)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:36) cumulé', 'En ligne (dep:36) cumulé', 'En brouillon (dep:36) cumulé', 
                                            'Mise à jour (dep:36) cumulé',  'Fiches reliées aux comptes pros (dep:36) cumulé'])    

    s1 = s.filter(regex='36')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(36)']]
    s1_cum['Recherches dep(36) cumulé'] = s1_cum['Recherches dep(36)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(36) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Indre'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Indre','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Indre','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='44':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:44)','En ligne (dep:44)', 'En brouillon (dep:44)','Mise à jour (dep:44)', 
                                                    'Fiches reliées aux comptes pros (dep:44)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:44) cumulé', 'En ligne (dep:44) cumulé', 'En brouillon (dep:44) cumulé', 
                                            'Mise à jour (dep:44) cumulé',  'Fiches reliées aux comptes pros (dep:44) cumulé'])    

    s1 = s.filter(regex='44')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(44)']]
    s1_cum['Recherches dep(44) cumulé'] = s1_cum['Recherches dep(44)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(44) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Loire-Atlantiques'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Loire-Atlantique','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Loire-Atlantique','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='59':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:59)','En ligne (dep:59)', 'En brouillon (dep:59)','Mise à jour (dep:59)', 
                                                    'Fiches reliées aux comptes pros (dep:59)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:59) cumulé', 'En ligne (dep:59) cumulé', 'En brouillon (dep:59) cumulé', 
                                            'Mise à jour (dep:59) cumulé',  'Fiches reliées aux comptes pros (dep:59) cumulé'])    

    s1 = s.filter(regex='59')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(59)']]
    s1_cum['Recherches dep(59) cumulé'] = s1_cum['Recherches dep(59)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(59) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Nord'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Nord','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Nord','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='63':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:63)','En ligne (dep:63)', 'En brouillon (dep:63)','Mise à jour (dep:63)', 
                                                    'Fiches reliées aux comptes pros (dep:63)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:63) cumulé', 'En ligne (dep:63) cumulé', 'En brouillon (dep:63) cumulé', 
                                            'Mise à jour (dep:63) cumulé',  'Fiches reliées aux comptes pros (dep:63) cumulé'])    

    s1 = s.filter(regex='63')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(63)']]
    s1_cum['Recherches dep(63) cumulé'] = s1_cum['Recherches dep(63)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(63) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Puy-de-Dôme'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Puy-de-Dôme','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Puy-de-Dôme','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """

if TerrG=='67':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:67)','En ligne (dep:67)', 'En brouillon (dep:67)','Mise à jour (dep:67)', 
                                                    'Fiches reliées aux comptes pros (dep:67)'])         
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:67) cumulé', 'En ligne (dep:67) cumulé', 'En brouillon (dep:67) cumulé', 
                                            'Mise à jour (dep:67) cumulé',  'Fiches reliées aux comptes pros (dep:67) cumulé'])     

    s1 = s.filter(regex='67')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(67)']]
    s1_cum['Recherches dep(67) cumulé'] = s1_cum['Recherches dep(67)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(67) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Bas-Rhin'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Bas-Rhin','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Bas-Rhin','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
    
if TerrG=='75':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:75)','En ligne (dep:75)', 'En brouillon (dep:75)','Mise à jour (dep:75)', 
                                                    'Fiches reliées aux comptes pros (dep:75)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:75) cumulé', 'En ligne (dep:75) cumulé', 'En brouillon (dep:75) cumulé', 
                                            'Mise à jour (dep:75) cumulé',  'Fiches reliées aux comptes pros (dep:75) cumulé'])      

    s1 = s.filter(regex='75')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                           

    s1_cum = s1[['datePresentation','Recherches dep(75)']]
    s1_cum['Recherches dep(75) cumulé'] = s1_cum['Recherches dep(75)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(75) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Paris'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Paris','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Paris','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """


if TerrG=='76':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:76)','En brouillon (dep:76)','Mise à jour (dep:76)', 
                                                    'Fiches reliées aux comptes pros (dep:76)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:76) cumulé', 'En brouillon (dep:76) cumulé', 
                                            'Mise à jour (dep:76) cumulé',  'Fiches reliées aux comptes pros (dep:76) cumulé'])    

    s1 = s.filter(regex='76')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(76)']]
    s1_cum['Recherches dep(76) cumulé'] = s1_cum['Recherches dep(76)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(76) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Seine-Maritime'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    #html_string_1 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Seine-Maritime','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    #"""

    #html_string_2 = f"""<br>
    #<center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Seine-Maritime','pourcentage']} %</font>
    #<br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    #"""

if TerrG=='77':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:77)','En ligne (dep:77)', 'En brouillon (dep:77)','Mise à jour (dep:77)', 
                                                    'Fiches reliées aux comptes pros (dep:77)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:77) cumulé', 'En ligne (dep:77) cumulé', 'En brouillon (dep:77) cumulé', 
                                            'Mise à jour (dep:77) cumulé',  'Fiches reliées aux comptes pros (dep:77) cumulé'])    

    s1 = s.filter(regex='77')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(77)']]
    s1_cum['Recherches dep(77) cumulé'] = s1_cum['Recherches dep(77)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(77) cumulé'])

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Seine-et-Marne'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Seine-et-Marne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Seine-et-Marne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
    
if TerrG=='78':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:78)','En ligne (dep:78)', 'En brouillon (dep:78)','Mise à jour (dep:78)', 
                                                    'Fiches reliées aux comptes pros (dep:78)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:78) cumulé', 'En ligne (dep:78) cumulé', 'En brouillon (dep:78) cumulé', 
                                            'Mise à jour (dep:78) cumulé',  'Fiches reliées aux comptes pros (dep:78) cumulé'])    

    s1 = s.filter(regex='78')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(78)']]
    s1_cum['Recherches dep(78) cumulé'] = s1_cum['Recherches dep(78)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(78) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Yvelines'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Yvelines','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Yvelines','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
        
if TerrG=='91':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:91)','En ligne (dep:91)', 'En brouillon (dep:91)','Mise à jour (dep:91)', 
                                                    'Fiches reliées aux comptes pros (dep:91)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:91) cumulé', 'En ligne (dep:91) cumulé', 'En brouillon (dep:91) cumulé', 
                                            'Mise à jour (dep:91) cumulé',  'Fiches reliées aux comptes pros (dep:91) cumulé'])     

    s1 = s.filter(regex='91')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                           

    s1_cum = s1[['datePresentation','Recherches dep(91)']]
    s1_cum['Recherches dep(91) cumulé'] = s1_cum['Recherches dep(91)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(91) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Essonne'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Essonne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Essonne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
        
if TerrG=='92':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:92)','En ligne (dep:92)', 'En brouillon (dep:92)','Mise à jour (dep:92)', 
                                                    'Fiches reliées aux comptes pros (dep:92)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:92) cumulé', 'En ligne (dep:92) cumulé', 'En brouillon (dep:92) cumulé', 
                                            'Mise à jour (dep:92) cumulé',  'Fiches reliées aux comptes pros (dep:92) cumulé'])   

    s1 = s.filter(regex='92')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(92)']]
    s1_cum['Recherches dep(92) cumulé'] = s1_cum['Recherches dep(92)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(92) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Hauts-de-Seine'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Hauts-de-Seine','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Hauts-de-Seine','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
        
if TerrG=='93':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:93)','En ligne (dep:93)', 'En brouillon (dep:93)','Mise à jour (dep:93)', 
                                                    'Fiches reliées aux comptes pros (dep:93)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:93) cumulé', 'En ligne (dep:93) cumulé', 'En brouillon (dep:93) cumulé', 
                                            'Mise à jour (dep:93) cumulé',  'Fiches reliées aux comptes pros (dep:93) cumulé'])     

    s1 = s.filter(regex='93')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(93)']]
    s1_cum['Recherches dep(93) cumulé'] = s1_cum['Recherches dep(93)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(93) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Seine-Saint-Denis'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Seine-Saint-Denis','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Seine-Saint-Denis','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
            
if TerrG=='94':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:94)','En ligne (dep:94)', 'En brouillon (dep:94)','Mise à jour (dep:94)', 
                                                    'Fiches reliées aux comptes pros (dep:94)'])    
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:94) cumulé', 'En ligne (dep:94) cumulé', 'En brouillon (dep:94) cumulé', 
                                            'Mise à jour (dep:94) cumulé',  'Fiches reliées aux comptes pros (dep:94) cumulé'])     

    s1 = s.filter(regex='94')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                            

    s1_cum = s1[['datePresentation','Recherches dep(94)']]
    s1_cum['Recherches dep(94) cumulé'] = s1_cum['Recherches dep(94)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(94) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Val-de-Marne'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc['Val-de-Marne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>"
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc['Val-de-Marne','pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>"
    """
                
if TerrG=='95':
    fig1 = px.line(df, x="Unnamed: 0", y=['Suivies (dep:95)','En ligne (dep:95)', 'En brouillon (dep:95)','Mise à jour (dep:95)', 
                                                    'Fiches reliées aux comptes pros (dep:95)'])
    figBar = px.bar(df, x="Unnamed: 0",y=['Suivies (dep:95) cumulé', 'En ligne (dep:95) cumulé', 'En brouillon (dep:95) cumulé', 
                                            'Mise à jour (dep:95) cumulé',  'Fiches reliées aux comptes pros (dep:95) cumulé'])      
    s1 = s.filter(regex='95')
    s1 = pd.merge(s['datePresentation'],s1, how='left', left_index=True, right_index=True)

    figSearch = px.line(s1,x='datePresentation', y=s1.columns.values.tolist()[1:])                                               

    s1_cum = s1[['datePresentation','Recherches dep(95)']]
    s1_cum['Recherches dep(95) cumulé'] = s1_cum['Recherches dep(95)'].cumsum()

    fig4Bar = px.bar(s1_cum, x="datePresentation",y=['Recherches dep(95) cumulé'])    

    fig6 = px.bar(df_history_data_grp[df_history_data_grp.departement == 'Val-d\'Oise'].groupby(['monthly'], as_index=False).agg({'Equipe Solinum':'sum',
                                                          'Equipe territoriale':'sum','Les acteurs':'sum'}),
             x="monthly", y=["Equipe Solinum","Equipe territoriale","Les acteurs"], custom_data=['variable'], color_discrete_sequence= [ '#7201a8', '#bd3786', '#2896A0']) 

    html_string_1 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_3_months.loc["Val-d'Oise",'pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 3 derniers mois<br></font></center>
    """

    html_string_2 = f"""<br>
    <center><font face='Helvetica' size='6'>{df_maj_6_months.loc["Val-d'Oise",'pourcentage']} %</font>
    <br/><font size='3'>des fiches ont été mise à jours au moins une fois pendant les 6 derniers mois<br></font></center>
    """
                    
fig1.update_xaxes(title_text="Date de création (de la fiche ou du compte pro de la fiche) ou date de la dernière mise à jour de la fiche", title_standoff=0.6, title_font_family="Times New Roman")
fig1.update_yaxes(title_text="Nombre de fiches (non cumulé)", title_font_family="Times New Roman")

annotations = dict(xref='paper', yref='paper', x=0.055, y=1,
                             xanchor='center', yanchor='top',
                             text='Fait le: ' + str("1 novembre 2021"),
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
                             text='Fait le: ' + str("1 novembre 2021"),
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
                             text='Fait le: ' + str("1 novembre 2021"),
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
                             text='Fait le: ' + str("1 novembre 2021"),
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


if TerrG=='06':
    st.write('Sélectionnez votre secteur :')
    cumul = ['06', '06 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='06':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='06')
      
    if cumul=='06 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='06 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 06'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG=='07':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['07', '07 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='07':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='07')
      
    #if cumul=='07 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='07 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 07'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 

if TerrG=='13':
    st.write('Sélectionnez votre secteur :')
    cumul = ['13', '13 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='13':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='13')
      
    if cumul=='13 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='13 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 13'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
    
if TerrG=='15':
    st.write('Sélectionnez votre secteur :')
    cumul = ['15', '15 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='15':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='15')
      
    if cumul=='15 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='15 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 15'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
        
if TerrG=='16':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['16', '16 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='16':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='16')
      
    #if cumul=='16 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='16 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 16'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
            
if TerrG=='21':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['21', '21 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='21':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='21')
      
    #if cumul=='21 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='21 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 21'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
    
if TerrG=='33':
    st.write('Sélectionnez votre secteur :')
    cumul = ['33', '33 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='33':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='33 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Département 33'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG=='34':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['34', '34 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='34':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='34')
      
    #if cumul=='34 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='34 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 34'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
            
if TerrG=='35':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['35', '35 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='35':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='35')
      
    #if cumul=='35 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='35 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 35'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
                        
if TerrG=='36':
    st.write('Sélectionnez votre secteur :')
    cumul = ['36', '36 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='36':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='36')
      
    if cumul=='36 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='36 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 36'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
            
if TerrG=='44':
    st.write('Sélectionnez votre secteur :')
    cumul = ['44', '44 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='44':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='44 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Département 44'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
                                
if TerrG=='59':
    st.write('Sélectionnez votre secteur :')
    cumul = ['59', '59 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='59':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='59')
      
    if cumul=='59 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='59 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 59'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
                                            
if TerrG=='63':
    st.write('Sélectionnez votre secteur :')
    cumul = ['63', '63 cumulé']
    cumul = st.selectbox('', cumul)
 
    if cumul=='63':
      compteProCum.columns = compteProCum.columns.astype(str)
      figComptePro = px.bar(compteProCum, x='datePresentation', y='63')
      
    if cumul=='59 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y='63 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 63'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
            
if TerrG=='67':
    st.write('Sélectionnez votre secteur :')
    cumul = ['67', '67 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='67':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='67 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Département 67'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])             
        
if TerrG=='75':
    st.write('Sélectionnez votre secteur :')
    cumul = ['75', '75 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='75':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='75 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Paris+ivry'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])           
                                                   
if TerrG=='76':
    #st.write('Sélectionnez votre secteur :')
    #cumul = ['76', '76 cumulé']
    #cumul = st.selectbox('', cumul)
 
    #if cumul=='76':
    #  compteProCum.columns = compteProCum.columns.astype(str)
    #  figComptePro = px.bar(compteProCum, x='datePresentation', y='76')
      
    #if cumul=='76 cumulé':
    #    figComptePro = px.bar(compteProCum, x='datePresentation', y='76 cumulé')

    fig4 = px.line(df4[df4['territoire']=='Département 76'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues']) 
            
if TerrG=='77':
    st.write('Sélectionnez votre secteur :')
    cumul = ['77', '77 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='77':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='77 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Département 77'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
        
if TerrG=='78':
    st.write('Sélectionnez votre secteur :')
    cumul = ['78', '78 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='78':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='78 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)

    fig4 = px.line(df4[df4['territoire']=='Département 78'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
        
if TerrG=='91':
    st.write('Sélectionnez votre secteur :')
    cumul = ['91', '91 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='91':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='91 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

    fig4 = px.line(df4[df4['territoire']=='Département 91'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG=='92':
    st.write('Sélectionnez votre secteur :')
    cumul = ['92', '92 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='92':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='92 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

    fig4 = px.line(df4[df4['territoire']=='Département 92'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
        
if TerrG=='93':
    st.write('Sélectionnez votre secteur :')
    cumul = ['93', '93 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='93':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='93 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

    fig4 = px.line(df4[df4['territoire']=='Département 93'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
        
if TerrG=='94':
    st.write('Sélectionnez votre secteur :')
    cumul = ['94', '94 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='94':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='94 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

    fig4 = px.line(df4[df4['territoire']=='Département 94'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        
        
if TerrG=='95':
    st.write('Sélectionnez votre secteur :')
    cumul = ['95', '95 cumulé']
    cumul = st.selectbox('', cumul)

    if cumul=='95':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul)
    if cumul=='94 cumulé':
        figComptePro = px.bar(compteProCum, x='datePresentation', y=cumul) 

    fig4 = px.line(df4[df4['territoire']=='Département 95'], x='Unnamed: 0', y=['Utilisateurs','Sessions','Pages vues'])        

if TerrG != '07' and TerrG != '34' and TerrG != '35' and TerrG != '76'and TerrG != '16' and TerrG != '21':
    #Compte Pro
    figComptePro.update_xaxes(title_text="Date d'ajout des comptes pro'", title_standoff=0.6,
                                title_font_family="Times New Roman")
    figComptePro.update_yaxes(title_text="Nombre de comptes pro ",
                                title_font_family="Times New Roman")

    annotationsCompte = dict(xref='paper', yref='paper', x=0.055, y=1,
                                xanchor='center', yanchor='top',
                                text='Fait le: ' + str("1 novembre 2021"),
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
                                 text='Fait le: ' + str("1 novembre 2021"),
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

if TerrG != '07' and TerrG != '34' and TerrG != '35' and TerrG != '76' and TerrG != '21':

    st.markdown('### Figure 6 : Evolution des mises à jours autonomes')
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown('### Taux de fiches mises à jour depuis moins de 3 mois, et depuis moins de 6 mois')
    col1, col2 = st.columns(2)

    col1.markdown(html_string_1, unsafe_allow_html=True)

    col2.markdown(html_string_2, unsafe_allow_html=True)
