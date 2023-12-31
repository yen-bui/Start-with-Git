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
def page_contexte():
    import streamlit as st
    st.title("Contexte & Méthodologie")
    introduction_text = """
**Objectif :**

Ce projet a pour but d'analyser le marché immobilier en France afin d'aider un ménage sans connaisance particulière souhaitant investir dans de l'immobilier locatif.

**Comment y parvenir :**

Pour ce projet, nous avons chosi l'analyse du marché immobilier principalement sur l'axe du storytelling et de la data visualisation dans une démarche de rétrospection. L’idée est de mieux comprendre ce qu’il s’est passé pour préparer de futures stratégies d'investissement (par exemple).

A la fin, il y a une partie bonus du possible prédictif sur le taux de rendement locatif permettant d’orienter les décisions des ménages investisseurs dans leur projet d’investissement locatif. La contrainte était qu’il fallait que cela fonctionne avec un nombre limité de variables, les plus basiques que nous pouvons retrouver sur une annonce immobilière (Prix, surface, nombre de pièces et arrondissement).

**Choix des datasets:**

Trois datasets (Transactions, Loyers et Foyers fiscaux) à l'origine ont été utilisées (Source : https://www.kaggle.com/datasets/benoitfavier/immobilier-france?select=loyers.csv). Bien que cela soit récupéré sur Kaggle, en réalité l’ensemble de ces données proviennent de sources institutionnelles (INSEE, DGFiP via publicité foncière, cadastre).

"""
    # Afficher le texte introductif
    st.write(introduction_text)

    image_url = " https://i.ibb.co/t49cwd9/3-datasets-origine.png"
    st.image(image_url, caption="Image1", use_column_width=True)

    introduction_text = """       
**Problématiques à régler sur les datasets :**
- Trouver la clé commune pour fusionner les datasets
- Gérer les doublons créés par les fusions du fait de champs communs
- Identifier les NaN et les gérer
- Une quantité de données disponibles qui varie beaucoup selon les départements
- Des valeurs qui varient beaucoup selon les départements en France
- Choisir les champs pertinents et essentiels à notre étude
- Enrichir le dataset afin de créer les champs nécessaires à notre étude
- Gérer les valeurs extrêmes et aberrantes
- etc...

**Démarche :**
- Création d’une clé unique concaténée de l’ID du département et de l’ID de la ville qui sera la clef pour fusionner les datasets
- Identification et suppression des valeurs aberrantes et d’une partie des valeurs extrêmes
- Création de plusieurs colonnes issues de colonnes déjà existantes (par exemple l’année sur la base de la date de transaction, etc…)
- Création de plusieurs colonnes issues de données mathématiques:
"""

    # Afficher le texte introductif
    st.write(introduction_text)

    image_url = "https://i.ibb.co/jLLR4c2/Nouvelles-colonnes-cr-es.png"
    st.image(image_url, caption="Image1", use_column_width=True)

    introduction_text = """
- Choix de focaliser l’étude sur Paris Intramuros : 
    - Les loyers et les prix de Paris Intramuros diffèrent trop du reste de la France pour envisager une étude globale (à la fois sur la visualisation et le prédictif)
    - Le département 75 fait partie des départements qui ont la plus grande quantité de données disponibles
    - Les transactions concernent presque exclusivement des appartements, donc suppression des lignes relatives aux maisons

**Dataset final :**
- Un dataset principal qui a été « clôné », puis allegé  en 2 autres différents pour les besoins de certains graphiques et du machine learning 
"""

    # Afficher le texte introductif
    st.write(introduction_text)

    image_url = "https://i.ibb.co/cyZQkg8/Datasets-finaux.png"
    st.image(image_url, caption="Image1", use_column_width=True)

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
    st.components.v1.html(open("Evolution_nombre_ventes_par_mois_2022_France_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)


    text = """
Au global sur la France entière, on observe là également un **effet de saisonnalité** 
des ventes selon les mois. On identifie très clairement une **chute** sur les mois 
d’**Aout** et de **Novembre**. Il convient de noter qu’ici la date de transaction 
correspond à la signature de l’acte authentique chez le notaire.
"""
    # Afficher le texte introductif
    st.write(text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    text = """
**Intéressons nous maintenant aux données propres à paris intramuros :**
"""
    # Afficher le texte introductif
    st.write(text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    # Générer le troisième graphique "Evolution du nombre total de ventes par arrondissement par année"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_nombre_ventes_par_arrondissement_Paris_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)
   

    introduction_text = """
Il est intéressant de remarquer que le **marché parisien est très tendu**, ainsi nous 
n’observons pas d’**effet de saisonnalité** réellement significatif au niveau des 
années, bien que nous retrouvons la tendance haussière avec la **chute liée au 
covid**, mais moins marquée qu’au global sur toute la  France.
Il est intéressant de faire la même analyse sur les prix :
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")


    # Générer le quatrième graphique "Evolution du prix au m2 moyen par arrondissement par année"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_prix_m2_par_arrondissement_Paris_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)
    
    introduction_text = """
Ici on constate une tendance à la **hausse des prix moyens au m2** dans paris 
intramuros, cela s’explique notamment par le fait que le marché soit tendu, avec 
**une demande croissante** et une **offre stable**.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    # Générer le cinquième graphique "Evolution du nombre total de ventes par mois et par arrondissement"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_ventes_par_arrondissement_par_mois_Paris_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)
    
    introduction_text = """
Ici, on retrouve clairement le même **effet de saisonnalité** par mois au sein de 
l’année 2022 qu’au global avec les chutes au mois d’Aout et de Novembre.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    # Générer le sixième graphique "Evolution du prix au m2 par mois"
    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_prix_m2_par_arrondissement_par_mois_Paris_Plotly.html", 'r').read(), width=800, height=500, scrolling=True)

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

    #Map interactive 

# Fonction pour la page "Carte vision Paris"
def page_map(df_final_used):
    import streamlit as st
    import folium
    import pandas as pd
    import branca.colormap as cm
    import matplotlib.cm as cm_plt
    import matplotlib.colors as colors



    st.title("Carte vision Paris")
    st.write("**Variations selon : Prix du bien - Prix au m2 - Taux de rendement**")

    introduction_text = """
Pour enrichir davantage votre expérience, nous avons créé une **carte interactive**. Elle vous permettra de visualiser la variation des prix immobiliers selon la localisation des biens. 
Cette carte dynamique vous permet notamment d'explorer les **fourchettes de prix, de taux de rendement et de prix au m² des biens**. Une manière visuelle et immersive d'appréhender le marché immobilier parisien.
"""
    st.write(introduction_text)


    # Remplacer les noms des colonnes dans le DataFrame
    df_final_used.rename(columns={'Prix m2': 'Prix au m2', 'Taux rendement i': 'Taux de rendement', 'prix': 'Prix'}, inplace=True)
    
        # Fonction pour arrondir les variables Prix m2 et Taux rendement i
    def round_variables(row):
        row['Prix au m2'] = round(row['Prix au m2'], 2)
        row['Taux de rendement'] = round(row['Taux de rendement'], 2)
        return row
        # Arrondir les variables dans le DataFrame
    df_final_used = df_final_used.apply(round_variables, axis=1)
    
    
    
    # Fonction pour créer une carte Folium interactive
    def create_folium_map(df_sorted, variable_name, colormap_colors, colormap_caption):
        # Créer une carte Folium centrée sur une position initiale
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=10)

        # Obtenir la valeur maximale et minimale de la variable pour la mise à l'échelle des couleurs
        max_value = df_sorted[variable_name].max()
        min_value = df_sorted[variable_name].min()

        # Créer une échelle de couleurs en fonction des couleurs fournies
        colormap = cm.LinearColormap(colors=colormap_colors, index=[min_value, max_value], vmin=min_value, vmax=max_value)

        # Parcourir le DataFrame et ajouter un cercle pour chaque parcelle
        for index, row in df_sorted.iterrows():
            # Récupérer la couleur correspondant à la variable de la parcelle
            color = colormap(row[variable_name])
            # Créer un cercle avec les coordonnées de latitude et longitude de la parcelle
            circle = folium.CircleMarker(location=[row['latitude'], row['longitude']],
                                         radius=5,
                                         color=color,
                                         fill=True,
                                         fill_color=color)
            # Ajouter les informations de prix et surface habitable à la fenêtre contextuelle du cercle
            popup_text = '{} : {}'.format(variable_name, row[variable_name])
            folium.Popup(popup_text).add_to(circle)
            circle.add_to(m)

        # Ajouter l'échelle de couleurs à la carte
        colormap.caption = colormap_caption
        colormap.add_to(m)

        return m
    

    

    # Trier le DataFrame par la colonne de votre choix (prix, Prix m2, Taux rendement i)
    def update_map(variable_name='Prix'):
        df_sorted = df_final_used.sort_values(variable_name, ascending=False)

        

        # Définir les couleurs et la légende de l'échelle de couleurs en fonction de la variable choisie
        if variable_name == 'Prix':
            colormap_colors = ['yellow', 'red']
            colormap_caption = 'Prix'
        elif variable_name == 'Prix au m2':
            colormap_colors = ['yellow', 'red']
            colormap_caption = 'Prix au m2'
        elif variable_name == 'Taux de rendement':
             colormap_colors = ['turquoise', 'magenta']
             colormap_caption = 'Taux de rendement'

        # Créer la carte interactive
        interactive_map = create_folium_map(df_sorted, variable_name, colormap_colors, colormap_caption)

        # Afficher la carte Folium dans Streamlit
        st.markdown('## Carte interactive')
        folium_static(interactive_map)


    # Créer un widget interactif pour choisir la variable à afficher
    variable_selector = st.selectbox("Sélectionnez une variable:", ['Prix', 'Prix au m2', 'Taux de rendement'])
    update_map(variable_name=variable_selector)

import matplotlib.pyplot as plt

# Fonction pour la page "Conclusion"
def page_conclusion():
    import streamlit as st
    st.title("Conclusion")

    introduction_text = """
En conclusion, il convient de retenir les éléments suivants :

Au global, les prix de l’immobilier évoluent et suivent **une évolution que l’on 
pourrait même qualifier d’exponentielle**, alimentée à la fois par des effets réels 
de l’économie réelle mais également par la spéculation sur les marchés.

Si au sein d’une année (sur 12 mois), ou au sein d’un cycle court (3 annés), on 
observe des **variations sur l’offre et la demande** qui impactent les prix qui 
peuvent être plus ou moins significatives selon les arrondissements de Paris, il 
convient de noter que ces effets sont lissés sur une vision plus long terme.

Un investisseur peut donc **maximiser la profitabilité** de on investissement en 
choisissant la bonne année et la bonne période de l’année, mais ce tromper sur 
ce couple de temporalité, n’aura pas réellement d’effet significatif à long terme 
sur sa rentabilité.

Enfin, le choix du **régime et de la modalité de financement auront également un 
fort impact sur la rentabilité** de l’investissement, car en considérant un régime 
LMNP, un investissement locatif en 2022 était rentabilisé au bout de la 32ème 
année si intégralement financé par emprunt sur 25 ans, contrairement au bout 
de la 25ème année si payé cash.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    st.write("**Paiement cash**")

    # Utilisation du style 'default'
    plt.style.use('default')

    # Création du graphique en utilisant matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Première sous-figure
    df_final_used['produits 10 ans'] = df_final_used['Loyer mensuel'] * 120
    PV = df_final_used['prix'] * 0.1
    df_final_used['gain à date 10 ans'] = df_final_used['produits 10 ans'] / df_final_used["prix acquisition cash + notaire"]
    mean_produits_10_ans = df_final_used['produits 10 ans'].mean() + PV.mean()
    mean_mensualite_10_ans = df_final_used["prix acquisition cash + notaire"].mean()
    axes[0].bar(['produits 10 ans', 'prix acquisition cash + notaire'], [mean_produits_10_ans, mean_mensualite_10_ans])
    axes[0].set_xlabel('Colonnes')
    axes[0].set_ylabel('Moyenne')
    axes[0].set_title('Moyenne des valeurs pour chaque colonne (10 ans)')

    # Deuxième sous-figure
    df_final_used['produits 25 ans'] = df_final_used['Loyer mensuel'] * 300
    PV = df_final_used['prix'] * 0.25
    df_final_used['gain à date 25 ans'] = df_final_used['produits 25 ans'] / df_final_used["prix acquisition cash + notaire"]
    mean_produits_25_ans = df_final_used['produits 25 ans'].mean() + PV.mean()
    mean_mensualite_25_ans = df_final_used["prix acquisition cash + notaire"].mean()
    axes[1].bar(['produits 25 ans', 'prix acquisition cash + notaire'], [mean_produits_25_ans, mean_mensualite_25_ans])
    axes[1].set_xlabel('Colonnes')
    axes[1].set_ylabel('Moyenne')
    axes[1].set_title('Moyenne des valeurs pour chaque colonne (25 ans)')

    # Ajustement automatique des espacements
    plt.tight_layout()

    # Afficher les sous-figures
    st.pyplot(fig)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    import streamlit as st
    st.write("**Paiement à crédit**")

    # Générer les 3 graphiques en barres

    # Ajout de la colonne "produits 10 ans"
    df_final_used['produits 10 ans'] = df_final_used['Loyer mensuel'] * 120
    PV = df_final_used['prix'] * 0.1

    # Calcul de la moyenne pour chaque colonne
    mean_produits_10_ans = df_final_used['produits 10 ans'].mean() + PV.mean()
    mean_mensualite_10_ans = (df_final_used['Mensualité'] * 120).mean()

    # Calcul de la colonne "gain à date 10 ans"
    df_final_used['gain à date 10 ans'] = df_final_used['produits 10 ans'] / df_final_used['Mensualité'] * 120

    # Ajout de la colonne "produits 25 ans"
    df_final_used['produits 25 ans'] = df_final_used['Loyer mensuel'] * 300
    PV = df_final_used['prix'] * 0.25

    # Calcul de la colonne "gain à date 25 ans"
    df_final_used['gain à date 25 ans'] = df_final_used['produits 25 ans'] / df_final_used['Mensualité'] * 300

    # Calcul de la moyenne pour chaque colonne
    mean_produits_25_ans = df_final_used['produits 25 ans'].mean() + PV.mean()
    mean_mensualite_25_ans = (df_final_used['Mensualité'] * 300).mean()

    # Ajout de la colonne "produits 32 ans"
    df_final_used['produits 32 ans'] = df_final_used['Loyer mensuel'] * 384
    PV = df_final_used['prix'] * 0.25

    # Calcul de la colonne "gain à date 32 ans"
    df_final_used['gain à date 32 ans'] = df_final_used['produits 32 ans'] / df_final_used['Mensualité'] * 384

    # Calcul de la moyenne pour chaque colonne
    mean_produits_32_ans = df_final_used['produits 32 ans'].mean() + PV.mean()
    mean_mensualite_32_ans = (df_final_used['Mensualité'] * 300).mean()

    # Utilisation du style 'plain'
    plt.style.use('default')

    # Création du graphique en utilisant matplotlib
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Première sous-figure
    axes[0].bar(['produits 10 ans', 'Mensualité * 120'], [mean_produits_10_ans, mean_mensualite_10_ans])
    axes[0].set_xlabel('Colonnes')
    axes[0].set_ylabel('Moyenne')
    axes[0].set_title('Moyenne des valeurs pour chaque colonne (10 ans)')
    axes[0].ticklabel_format(axis='y', style='plain')  # Formater les étiquettes en valeurs

    # Deuxième sous-figure
    axes[1].bar(['produits 25 ans', 'Mensualité * 300'], [mean_produits_25_ans, mean_mensualite_25_ans])
    axes[1].set_xlabel('Colonnes')
    axes[1].set_ylabel('Moyenne')
    axes[1].set_title('Moyenne des valeurs pour chaque colonne (25 ans)')
    axes[1].ticklabel_format(axis='y', style='plain')  # Formater les étiquettes en valeurs

    # Troisième sous-figure
    axes[2].bar(['produits 32 ans', 'Mensualité * 384'], [mean_produits_32_ans, mean_mensualite_32_ans])
    axes[2].set_xlabel('Colonnes')
    axes[2].set_ylabel('Moyenne')
    axes[2].set_title('Moyenne des valeurs pour chaque colonne (32 ans)')
    axes[2].ticklabel_format(axis='y', style='plain')  # Formater les étiquettes en valeurs

    # Ajustement automatique des espacements
    plt.tight_layout()

    # Afficher les sous-figures dans Streamlit
    st.pyplot(fig)

    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")
    # Add an empty line to create space
    st.write("")

    conclusion_text = """
Pour les graphiques, on tient compte des revenus locatifs mais aussi de la plus-value potentielle liée à l’évolution des prix de l’immobilier. 
"""
    st.write(conclusion_text)

# Fonction afficher la page "Bonus"
def page_filtre():
    import streamlit as st
    st.title("Bonus / Votre projet immobilier")

    introduction_text = """
A présent, nous vous invitons à **réaliser une estimation de la rentabilité** de votre projet en fonction des critères de votre choix : emplacement du bien (arrondissement),
prix, nombre de pièces, surface ou encore loyer mensuel du bien. Vous aurez également l'occasion de rechercher un bien en fonction du **taux de rendement souhaité**.
"""
    st.write(introduction_text)

    import pandas as pd
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    data = pd.read_csv("df_streamlit.csv")

    # Modifier la colonne "Taux de rendement" en effectuant le calcul demandé
    data['Taux de rendement'] = ((data['Loyer mensuel'] * 12) / data['Prix']) * 100
    
    # Modifier la colonne "Taux de rendement" en effectuant le calcul et en arrondissant
    data['Taux de rendement'] = round(((data['Loyer mensuel'] * 12) / data['Prix']) * 100, 2)

    def filter_data(data, prix_range, code_postal, nb_pieces_range, surface_range, loyer_mensuel_range, taux_rendement_range):
        filtered_data = data[
            (data["Prix"].between(prix_range[0], prix_range[1])) &
            (data["Code Postal"] == code_postal) &
            (data["Nombre de pièces"].between(nb_pieces_range[0], nb_pieces_range[1])) &
            (data["Surface"].between(surface_range[0], surface_range[1])) &
            (data["Loyer mensuel"].between(loyer_mensuel_range[0], loyer_mensuel_range[1])) &
            (data["Taux de rendement"].between(taux_rendement_range[0], taux_rendement_range[1]))
        ]
        return filtered_data

    st.write("**Recherche de biens immobiliers**")

    st.sidebar.title("Filtres de recherche")

    prix_range = st.sidebar.slider("Prix (€)", float(data["Prix"].min()), float(data["Prix"].max()), (float(data["Prix"].min()), float(data["Prix"].max())))

    code_postal = st.sidebar.selectbox("Code Postal", data["Code Postal"].unique())

    nb_pieces_range = st.sidebar.slider("Nombre de pièces", int(data["Nombre de pièces"].min()), int(data["Nombre de pièces"].max()), (int(data["Nombre de pièces"].min()), int(data["Nombre de pièces"].max())))

    surface_range = st.sidebar.slider("Surface (m²)", float(data["Surface"].min()), float(data["Surface"].max()), (float(data["Surface"].min()), float(data["Surface"].max())))

    loyer_mensuel_range = st.sidebar.slider("Loyer mensuel (€)", float(data["Loyer mensuel"].min()), float(data["Loyer mensuel"].max()), (float(data["Loyer mensuel"].min()), float(data["Loyer mensuel"].max())))

    taux_rendement_range = st.sidebar.slider("Taux de rendement (%)", float(data["Taux de rendement"].min()), float(data["Taux de rendement"].max()), (float(data["Taux de rendement"].min()), float(data["Taux de rendement"].max())))

    filtered_data = filter_data(data, prix_range, code_postal, nb_pieces_range, surface_range, loyer_mensuel_range, taux_rendement_range)

    st.write(f"Nombre de biens correspondants : {len(filtered_data)}")

    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    for index, row in filtered_data.iterrows():
        popup_text = f"Bien immobilier {index + 1}**\n"
        popup_text += f"Prix : {row['Prix']} €\n"
        popup_text += f"Code Postal : {row['Code Postal']}\n"
        popup_text += f"Nombre de pièces : {row['Nombre de pièces']}\n"
        popup_text += f"Surface :** {row['Surface']} m²\n"
        popup_text += f"Loyer mensuel : {row['Loyer mensuel']} €\n"
        popup_text += f"Taux de rendement : {row['Taux de rendement']} %\n"
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(m)

    folium_static(m)

    if len(filtered_data) > 0:
        import streamlit as st
        st.subheader("Biens immobiliers filtrés :")
        for index, row in filtered_data.iterrows():
            st.write(f"Bien immobilier {index + 1}")
            st.write(f"Prix : {row['Prix']} €")
            st.write(f"Code Postal : {row['Code Postal']}")
            st.write(f"Nombre de pièces : {row['Nombre de pièces']}")
            st.write(f"Surface :** {row['Surface']} m²")
            st.write(f"Loyer mensuel : {row['Loyer mensuel']} €")
            st.write(f"Taux de rendement : {row['Taux de rendement']} %")
            st.write("----")
    else:
        st.warning("Aucun bien ne correspond aux critères de recherche.")

# Fonction pour afficher la page ML
def page_ML():
    import streamlit as st
    st.title("Bonus / Machine Learning")
    introduction_text = """
**Préambule :**

A titre accessoire, nous avons voulu nous essayer à une prédiction sur une tranche de taux de rendement (tous les 0,5 points) permettant d’orienter les décisions des ménages investisseurs dans leur projet d’investissement locatif. La contrainte était qu’il fallait que cela fonctionne avec un nombre limité de variables, les plus basiques que nous pouvons retrouver sur une annonce immobilière (Prix, surface, nombre de pièces et arrondissement).

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

Accuracy: 0.892

F1 Score: 0.888

prix: 0.477

surface_habitable: 0.413

loyer_m2_appartement: 0.049

code_postal: 0.042

n_pieces: 0.019

vefa: 7.098e-05 

"""

    # Afficher le texte introductif
    st.write(introduction_text)


# Fonction principale de l'application
# Create a layout with links to the two pages
st.sidebar.title("Projet Data Analyst")
st.sidebar.title("Investissement locatif")
page_links = ["Contexte & Méthodologie", "Vision France","Vision Paris","Carte vision Paris","Conclusion","Bonus / Votre projet immobilier", "Bonus / Machine Learning"]
choice = st.sidebar.radio("Menu", page_links)


    # En fonction du choix de l'utilisateur, appelez la fonction correspondante
if choice == "Contexte & Méthodologie":
    page_contexte()
if choice == "Bonus / Machine Learning":
    page_ML()
elif choice == "Vision France":
    page_France()
elif choice == "Vision Paris":
    page_Paris()
elif choice == "Carte vision Paris":
    page_map(df_final_used)
elif choice == "Conclusion":
    page_conclusion()
elif choice == "Bonus / Votre projet immobilier":
    page_filtre()

    # Afficher les informations des auteurs en bas de la barre latérale
st.sidebar.write("**Auteurs :**")
st.sidebar.write("Yen BUI")
st.sidebar.write("Thomas JOSSIER")
st.sidebar.write("Torkia DRIDER")
