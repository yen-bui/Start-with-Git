import pandas as pd
import numpy as np
import plotly.graph_objects as go
import locale
from calendar import month_name
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium
import numpy_financial as npf
import plotly.express as px
import os
import streamlit as st

#pip install ipywidgets

import branca.colormap as cm
import matplotlib.cm as cm_plt
import matplotlib.colors as colors
#from ipywidgets import interact, widgets
#from IPython.display import display



# Fonction pour afficher la page ML
def page_ML():
    import streamlit as st
    st.title("Machine Learning")
    introduction_text = """
**Objectif :**

Permettre de **prédire** avec le moins d’informations possibles (loyer au m2, prix de vente, code postal, appartement neuf ou ancien, nombre de pièces, surface habitable) le **niveau de rentabilité potentiel** d’un investissement locatif.

**Démarche :**

Toute l’analyse menée sur le dataset, le choix de la région, la gestion des NaNs, des valeurs aberrantes et extrêmes, l’enrichissement de ce dernier jusqu’au calcul du taux de rendement nous permettaient d’avoir un dataset préparé pour **envisager un modèle predictif de machine learning**.

**Etapes :**

- Suppression de toutes les colonnes non essentielles pour garder celles citées au-dessus

- Création des tranches de rentabilité (la variable cible) sur la base du taux de rendement

- Remplacement de la valeur booléenne True/False de la colonne VEFA par 0 et 1

- Test – Train - Split

- Ordinal encoder de la variable cible

- Normalisation

- Résultats & metrics 

**Résultats :**

Accuracy: 0.8916181311724487

F1 Score: 0.8876209442211274 

prix: 0.4769188103248616

surface_habitable: 0.4134632071728446

loyer_m2_appartement: 0.048852671327828646

code_postal: 0.041553367818537676

n_pieces: 0.019140965476993666

vefa: 7.09778789337547e-05 

"""

    # Afficher le texte introductif
    st.write(introduction_text)




# Fonction pour afficher la page "Vision France"
def page_France():
    import streamlit as st

    st.title("Vision France")

    introduction_text = """
Bienvenue dans notre analyse de l'évolution du **marché de l'immobilier en France de 2014 à 2022**. Cette période a été marquée par divers événements économiques, sociaux et politiques qui ont façonné le paysage immobilier.

Au cours de cette présentation, nous allons **explorer les tendances, les fluctuations et les modèles qui ont caractérisé ce marché**. Des variations saisonnières aux impacts potentiels de facteurs externes, notre objectif sera de fournir un aperçu informatif et visuel de l'évolution dynamique de l'immobilier en France.

Nous allons **plonger dans les données, examiner les statistiques clés et utiliser des visualisations interactives** pour vous offrir une compréhension approfondie des dynamiques qui ont marqué cette période.

Nous vous présenterons également **l'intérêt d'investir dans l'immobilier locatif** en illustrant notamment les rendements potentiels.
"""

    # Afficher le texte introductif
    st.write(introduction_text)
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    
    #Visuel Flourish 1
    flourish_html_code = """
    <div class="flourish-embed" data-src="visualisation/14482386">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code, height=650, scrolling=True)
    text1 = """
Ce graphique représente les 10 départements ayant réalisé **le plus grand nombre de ventes d'appartements et de maisons pour la période de 2014 à 2022**. Les cinq départements les plus recherchés en 2022 se trouvent dans les régions des Hauts-de-France, d'Île-de-France, de Provence-Alpes-Côte d’Azur, de Nouvelle-Aquitaine et d'Auvergne-Rhône-Alpes.
"""
    st.write(text1)
    
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    #Visuel Flourish 2
    flourish_html_code_4 = """
    <div class="flourish-embed" data-src="visualisation/14729530">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_4, height=650, scrolling=True)

    text2 = """
Ce graphique illustre la **répartition du nombre de ventes d'appartements et de maisons** dans tous les départements des cinq régions préalablement présentées. Le filtre nous permet de sélectionner la région souhaitée. De manière générale, dans ces régions, on observe **davantage de ventes d'appartements que de maisons**, à l'exception de deux régions : la Nouvelle-Aquitaine et les Hauts-de-France.
En **Île-de-France**, où le marché immobilier est **particulièrement dynamique**, les appartements dominent nettement les ventes par rapport aux maisons. Cette observation justifie notre décision d'approfondir l'**analyse spécifiquement sur les appartements** dans le cadre de ce projet.
"""
    # Afficher le texte
    st.write(text2)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")


    # Visuel Flourish 3
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14488832">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=650, scrolling=True)

    text3 = """
Le loyer des appartements en Île-de-France est **le plus élevé** de toute la France. Le département **le plus onéreux** en termes de loyer est Paris.
"""
    # Afficher le texte
    st.write(text3)
    
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")


    # Visuel Flourish 4
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14734282">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=650, scrolling=True)

    text4 = """
Le prix d'achat par mètre carré d'appartement atteint son **maximum** à Paris. Les prix par mètre carré sont également plus élevés en Île-de-France, en Auvergne-Rhône-Alpes, ainsi que sur la côte Atlantique et la côte d'Azur.
"""
    # Afficher le texte
    st.write(text4)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    # Visuel Flourish 5
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14734138">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=650, scrolling=True)

    text5 = """
En 2014 et 2022, la plus-value sur le prix d'achat par mètre carré d'appartement est notable dans l'ouest de la France, en particulier sur la côte Atlantique.
La **plus-value reste importante en Ile-de-France**.

"""
    # Afficher le texte
    st.write(text5)


# Fonction pour la page "Vision Paris"
def page_Paris():

    import streamlit as st
    st.title("Vision Paris")

    introduction_text = """
Nous avons évoqué précédemment les raisons qui nous ont poussé à focaliser notre étude sur **Paris Intramuros**, désormais nous allons orienter l’investisseur sur le meilleur **régime fiscal** à adopter suite à son investissement avant de nous poser les questions suivantes : 

Il y a-t-il une **période plus propice** à l’investissement locatif au cours de l’année, en outre, existe-t-il un effet de **saisonnalité** ayant un impact significatif sur la rentabilité du projet ?

Comment évolue le marché au fil des années ? 

"""
    # Afficher le texte introductif
    st.write(introduction_text)
    

    st.write("**Le choix du régime fiscal**")

    fiscalité_text = """
**Prenons l’exemple suivant :** 

- Bien d’une valeur de 400 000 € hors frais de notaire

- Frais d’agence : 2000 €

- Frais de notaire de 30 000 €

- Travaux aménagement (cuisine, murs…) : 30 000 €

- Mobilier : 15 000 €

- Intérêts (yc assurance) année 1 : 1000 €

- Charges : 1000 €

- Taxe foncière : 800 €

- Loyer encaissé annuel : 14 400 €


**Résultat à partir de cet exemple, avec un taux marginal d’imposition de 30% :** 

Cas microfoncier : 3024 € d’IR + 17,2% de prélèvements sociaux

Cas revenus fonciers : 3474 € d’IR + 17,2% de prélèvements sociaux

Cas LMNP : 0€


"""
    # Afficher le texte introductif
    st.write(fiscalité_text)


    st.write("**L'étude sur Paris Intramuros**")

    image_url = "https://i.ibb.co/Cz8P98M/Image1.png"
    st.image(image_url, caption="Image1", use_column_width=True)
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")


    # Générer le premier graphique "Evolution du nombre total de ventes par année"

    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_nombre_ventes_par_annee_France_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)
    text = """
    Ici, on identifie clairement une **incidence de l’évolution** des cycles économiques 
sur le marché de l’immobilier (effet de saisonnalité par année). Bien évidemment,
ici la chute observée en 2020 est faussée, puisqu’il s’agit de l’année de la 
**covid19**.
"""
    # Afficher le texte introductif
    st.write(text)
    
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    # Générer le deuxième graphique "Evolution du nombre total de ventes par mois"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_nombre_ventes_par_mois_2022_France_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)


    text = """
Au global sur la France entière, on observe là également un **effet de saisonnalité** 
des ventes selon les mois. On identifie très clairement une **chute** sur les mois 
d’**Aout** et de **Novembre**. Il convient de noter qu’ici la date de transaction 
correspond à la signature de l’acte authentique chez le notaire.

**Intéressons nous maintenant aux données propres à paris intramuros :**
"""
    # Afficher le texte introductif
    st.write(text)


    # Générer le troisième graphique "Evolution du nombre total de ventes par arrondissement par année"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_nombre_ventes_par_arrondissement_Paris_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)
   

    introduction_text = """
Il est intéressant de remarquer que le **marché parisien est très tendu**, ainsi nous 
n’observons pas d’**effet de saisonnalité** réellement significatif au niveau des 
années, bien que nous retrouvons la tendance haussière avec la **chute liée au 
covid**, mais moins marquée qu’au global sur toute la  France.
Il est intéressant de faire la même analyse sur les prix :
"""
    # Afficher le texte introductif
    st.write(introduction_text)


    # Générer le quatrième graphique "Evolution du prix au m2 moyen par arrondissement par année"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_prix_m2_par_arrondissement_Paris_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)
    

    introduction_text = """
Ici on constate une tendance à la **hausse des prix moyens au m2** dans paris 
intramuros, cela s’explique notamment par le fait que le marché soit tendu, avec 
**une demande croissante** et une **offre stable**.
"""
    # Afficher le texte introductif
    st.write(introduction_text)


    # Générer le cinquième graphique "Evolution du nombre total de ventes par mois et par arrondissement"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_ventes_par_arrondissement_par_mois_Paris_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)
    
    introduction_text = """
Ici, on retrouve clairement le même **effet de saisonnalité** par mois au sein de 
l’année 2022 qu’au global avec les chutes au mois d’Aout et de Novembre.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Générer le sixième graphique "Evolution du prix au m2 par mois"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_prix_m2_par_arrondissement_par_mois_Paris_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)

    introduction_text = """
Ici, on observe que la période de l’année a un impact sur le prix de vente, 
puisqu’il peut exister selon les arrondissements des **variations significatives** du 
prix de vente au m2.
Il y a donc un impact du couple Offre/Demande sur le marché.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

# Chemin vers le fichier CSV
csv_file_path = "df_final_used.csv"

# Charger le fichier CSV dans un DataFrame
df_final_used = pd.read_csv(csv_file_path)

# Fonction principale de l'application
# Create a layout with links to the two pages
st.sidebar.title("Navigation")
#page_links = ["Machine Learning", "Vision France","Vision Paris","Carte vision Paris","Conclusion","Bonus"]
page_links = ["Machine Learning", "Vision France","Vision Paris"]
choice = st.sidebar.radio("Go to", page_links)


    # En fonction du choix de l'utilisateur, appelez la fonction correspondante
if choice == "Machine Learning":
    page_ML()
elif choice == "Vision France":
    page_France()
elif choice == "Vision Paris":
    page_Paris()
#elif choice == "Carte vision Paris":
    #page_map(df_final_used)
#elif choice == "Conclusion":
    #page_conclusion()
#elif choice == "Bonus":
    #page_filtre()
