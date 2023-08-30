import pandas as pd
import plotly.graph_objects as go
import locale
from calendar import month_name
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium



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


    #Visuel Flourish 1
    flourish_html_code = """
    <div class="flourish-embed" data-src="visualisation/14482386">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code, height=600, scrolling=True)

    text1 = """
Ce graphique représente les 10 départements ayant réalisé **le plus grand nombre de ventes d'appartements et de maisons pour la période de 2014 à 2022**. Les cinq départements les plus recherchés en 2022 se trouvent dans les régions des Hauts-de-France, d'Île-de-France, de Provence-Alpes-Côte d’Azur, de Nouvelle-Aquitaine et d'Auvergne-Rhône-Alpes.
"""
    # Afficher le texte
    st.write(text1)


    #Visuel Flourish 2
    flourish_html_code_4 = """
    <div class="flourish-embed" data-src="visualisation/14729530">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_4, height=600, scrolling=True)

    text2 = """
Ce graphique illustre la **répartition du nombre de ventes d'appartements et de maisons** dans tous les départements des cinq régions préalablement présentées. Le filtre nous permet de sélectionner la région souhaitée. De manière générale, dans ces régions, on observe **davantage de ventes d'appartements que de maisons**, à l'exception de deux régions : la Nouvelle-Aquitaine et les Hauts-de-France.
En **Île-de-France**, où le marché immobilier est **particulièrement dynamique**, les appartements dominent nettement les ventes par rapport aux maisons. Cette observation justifie notre décision d'approfondir l'**analyse spécifiquement sur les appartements** dans le cadre de ce projet.
"""
    # Afficher le texte
    st.write(text2)


    # Visuel Flourish 3
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14488832">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=600, scrolling=True)

    text3 = """
Le loyer des appartements en Île-de-France est **le plus élevé** de toute la France. Le département **le plus onéreux** en termes de loyer est Paris.
"""
    # Afficher le texte
    st.write(text3)


    # Visuel Flourish 4
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14734282">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=600, scrolling=True)

    text4 = """
Le prix d'achat par mètre carré d'appartement atteint son **maximum** à Paris. Les prix par mètre carré sont également plus élevés en Île-de-France, en Auvergne-Rhône-Alpes, ainsi que sur la côte Atlantique et la côte d'Azur.
"""
    # Afficher le texte
    st.write(text4)


    # Visuel Flourish 5
    flourish_html_code_2 = """
    <div class="flourish-embed" data-src="visualisation/14734138">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
    </div>
    """
    st.components.v1.html(flourish_html_code_2, height=600, scrolling=True)

    text5 = """
En 2014 et 2022, la plus-value sur le prix d'achat par mètre carré d'appartement est notable dans l'ouest de la France, en particulier sur la côte Atlantique.
La **plus-value reste important en Ile-de-France**.

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


    def generate_price_chart(dataframe):
     
     dataframe['month'] = dataframe['date_transaction'].dt.month

     mean_price_per_m2_by_month_and_arrondissement = dataframe.groupby(['ville', 'month'])['Prix m2'].mean().reset_index(name='Prix moyen m2')

     mean_price_per_m2_by_month_and_arrondissement = mean_price_per_m2_by_month_and_arrondissement.sort_values(by='month')

     month_names_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

     traces = []
     for arrondissement in mean_price_per_m2_by_month_and_arrondissement['ville'].unique():
            data_arrondissement = mean_price_per_m2_by_month_and_arrondissement[mean_price_per_m2_by_month_and_arrondissement['ville'] == arrondissement]
            arrondissement_name = f'Arrondissement {arrondissement}'
            arrondissement_name = arrondissement_name.replace('Arrondissement ', '')
            hover_text = [f'Ville: {arrondissement}<br>Mois: {month}<br>Prix moyen au m2: {price:.2f}' for month, price in zip(month_names_fr, data_arrondissement['Prix moyen m2'])]
            trace = go.Scatter(x=month_names_fr, y=data_arrondissement['Prix moyen m2'], mode='lines', name=arrondissement_name, hovertemplate='%{text}', text=hover_text)
            traces.append(trace)

     fig = go.Figure(data=traces)

     fig.update_layout(title='Évolution du prix moyen au m2 par mois et par arrondissement de Paris', xaxis_title='Mois', yaxis_title='Prix moyen au m2')

     return fig

    


    import pandas as pd
    import plotly.graph_objects as go
    import locale
    from calendar import month_name
    import numpy as np

    arrays = dict(np.load("transactions.csv"))
    data = {k: [s.decode("utf-8") for s in v.tobytes().split(b"\x00")] if v.dtype == np.uint8 else v for k, v in arrays.items()}
    df_transactions = pd.DataFrame.from_dict(data)

    df_transactions["date_transaction"]=pd.to_datetime(df_transactions.date_transaction)

    df_transactions['annee'] = df_transactions['date_transaction'].dt.year

    #Filtre sur 2022

    df_transactions_filtré = df_transactions.loc[df_transactions['annee'] == 2022].copy()

    #Création de la clef commune
    df_transactions_filtré["departement"] = df_transactions_filtré["departement"].astype(str)

    df_transactions_filtré["KEY"] = df_transactions_filtré["departement"].astype(str) + '-' + df_transactions_filtré["id_ville"].astype(str)



    df_loyers = pd.read_csv("loyers.csv", sep=",")

    #Filtre sur 2022
    df_loyers = df_loyers[df_loyers["date"] == 2022]

    #Création de la  clé pour le futur merge
    df_loyers["id_ville"] = df_loyers["id_ville"].astype(int)

    df_loyers["KEY"] = df_loyers["departement"].astype(str) + '-' + df_loyers["id_ville"].astype(str)

    #On retire les colonnes qui vont créer des doublons lors du merge
    df_loyers = df_loyers.drop(["departement", "id_ville","ville", "date"], axis=1)



    df_foyers = pd.read_csv("foyers_fiscaux.csv", sep=",")


    #Création de la  clé pour le futur merge

    df_foyers["KEY"] = df_foyers["departement"].astype(str) + '-' + df_foyers["id_ville"].astype(str)

    #Ici on fait une moyenne car données 2022 non dispo, et on enlève toutes les colonnes non utiles, et qui vont créer des doublons lors du merge
    df_foyers['moyenne_foyers_fiscaux'] = df_foyers.groupby('KEY')['n_foyers_fiscaux'].transform('mean')
    df_foyers['moyenne_revenu_fiscal'] = df_foyers.groupby('KEY')['revenu_fiscal_moyen'].transform('mean')

    df_foyers_used = df_foyers[["KEY", "moyenne_foyers_fiscaux", "moyenne_revenu_fiscal"]]

    #On enlève les doublons crées mécaniquement par la moyenne, on garde une seule occurence par clé unique
    df_foyers_used= df_foyers_used.drop_duplicates()


    #On merge

    df_final = pd.merge(df_loyers, df_transactions_filtré, on="KEY")

    df_final = pd.merge(df_final, df_foyers_used, on="KEY")


    #On enlève les caractères spéciaux des surfaces

    liste = ["departement", "ville", "adresse", "type_batiment"]
    liste2 = ["surface_dependances", "surface_locaux_industriels", "surface_terrains_agricoles", "surface_terrains_sols", "surface_terrains_nature"]

    caracteres_a_supprimer = ['{', '}']

    for colonne in liste + liste2:
     df_final[colonne] = df_final[colonne].astype(str).str.replace('|'.join(caracteres_a_supprimer), '')

    df_final[liste] = df_final[liste].astype(str)

    df_final[liste2] = df_final[liste2].replace('', pd.NA).apply(pd.to_numeric, errors='coerce')

    df_final[liste2] = df_final[liste2].astype('Int64')


    #On créer de nouvelles colonnes utiles pour notre étude
    df_final["Prix m2"] = df_final["prix"] / df_final["surface_habitable"]
    df_final['moyenne_foyers_fiscaux'] = df_foyers.groupby('KEY')['n_foyers_fiscaux'].transform('mean')


    import numpy as np
    import numpy_financial as npf

    # Taux d'intérêt mensuel et nombre de périodes/mois
    taux_interet_mensuel = 2.11 / 12 / 100
    nombre_mois = 25 * 12

    # Calcul de la mensualité pour chaque montant de prêt
    df_final['Mensualité'] = npf.pmt(taux_interet_mensuel, nombre_mois, -df_final['prix'])

    df_final['Coût total des intérêts'] = (df_final['Mensualité'] * nombre_mois) - df_final['prix']

    df_final['Frais de notaire'] = df_final.apply(lambda row: row['prix'] * 0.08 if not row['vefa'] else row['prix'] * 0.04, axis=1)

    df_final["prix acquisition yc i + notaire"] = df_final["prix"]+df_final["Coût total des intérêts"]+df_final["Frais de notaire"]
    df_final["prix acquisition cash + notaire"] = df_final["prix"]+df_final["Frais de notaire"]


    df_final['Loyer mensuel'] = np.where(df_final['type_batiment'] == "Maison",
                                     df_final['loyer_m2_maison'] * df_final['surface_habitable'],
                                     df_final['loyer_m2_appartement'] * df_final['surface_habitable'])

    df_final["Taux rendement i"] = ( (df_final["Loyer mensuel"] *12 ) / df_final["prix acquisition yc i + notaire"])*100
    df_final["Taux rendement cash"] = ( (df_final["Loyer mensuel"] *12 ) / df_final["prix acquisition cash + notaire"])*100



    # Ajout de la colonne "produits 10 ans"
    df_final['produits 10 ans'] = df_final['Loyer mensuel'] * 120 + df_final['prix'] * 0.1

    # Calcul de la colonne "gain à date 10 ans"
    df_final['gain à date 10 ans'] = df_final['produits 10 ans'] / (df_final['Mensualité'] * 120)


    # Ajout de la colonne "produits 25 ans"
    df_final['produits 25 ans'] = df_final['Loyer mensuel'] * 300 + df_final['prix'] * 0.25

    # Calcul de la colonne "gain à date 25 ans"
    df_final['gain à date 25 ans'] = df_final['produits 25 ans'] / (df_final['Mensualité'] * 300)


    #Bornage des données et suppression d'une colonne non utile
    df_final_used = df_final[df_final["departement"] == "75"]
    df_final_used= df_final_used[df_final_used["type_batiment"] == "Appartement"]
    df_final_used= df_final_used[df_final_used["Prix m2"] <25000]
    df_final_used= df_final_used[df_final_used["Prix m2"] >5000]
    df_final_used= df_final_used[df_final_used["surface_habitable"] >9]
    df_final_used= df_final_used[df_final_used["surface_habitable"] <150]
    df_final_used= df_final_used[df_final_used["prix"] <1000000]
    df_final_used= df_final_used[df_final_used["n_pieces"] <10]
    df_final_used= df_final_used[df_final_used["n_pieces"] >1]

    df_final_used= df_final_used.drop("moyenne_foyers_fiscaux", axis=1)


    import streamlit as st
    from streamlit_folium import folium_static
    import folium


    #Changement de type de données de la colonne date_transactions pour extraire l'année pour nos filtres sur le dataframe.


    df_transactions["date_transaction"]=pd.to_datetime(df_transactions.date_transaction)


    #Extraction de l'année dans une nouvelle colonne pour nos filtres sur le dataframe

    df_transactions['annee'] = df_transactions['date_transaction'].dt.year

    #Filtre sur département 75

    df_transactions_filtré = df_transactions.loc[df_transactions['departement'] == "75"].copy()

    df_transactions_filtré['month'] = df_transactions_filtré['date_transaction'].dt.month

    df_transactions_filtré["Prix m2"] = df_transactions_filtré["prix"] / df_transactions_filtré["surface_habitable"]

    df_final_used_GRAPH = df_transactions_filtré



    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["type_batiment"] == "Appartement"]

    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["Prix m2"] <25000]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["Prix m2"] >5000]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["surface_habitable"] >9]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["surface_habitable"] <150]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["prix"] <1000000]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["n_pieces"] <10]
    df_final_used_GRAPH= df_final_used_GRAPH[df_final_used_GRAPH["n_pieces"] >1]


    # Générer le premier graphique "Evolution du nombre total de ventes par année"

    # Calculer le nombre total de ventes pour chaque année
    total_sales_by_year = df_final_used_GRAPH.groupby('annee').size().reset_index(name='Total Ventes')

    # Trier le DataFrame par la colonne 'YEAR'
    total_sales_by_year = total_sales_by_year.sort_values(by='annee')

    # Tracer la courbe pour représenter l'évolution du nombre total de ventes
    trace4 = go.Scatter(x=total_sales_by_year['annee'], y=total_sales_by_year['Total Ventes'], mode='lines', name='Nombre total de ventes par année')

    # Créer la figure et ajoutez la trace
    fig4 = go.Figure(data=[trace4])

    # Mettre à jour la mise en page du graphique
    fig4.update_layout(title='Évolution du nombre total de ventes par année', xaxis_title='Année', yaxis_title='Nombre total de ventes')
    
    # Afficher le premier graphique dans Streamlit
    st.plotly_chart(fig4, use_container_width=True)


    text = """
    Ici, on identifie clairement une **incidence de l’évolution** des cycles économiques 
sur le marché de l’immobilier (effet de saisonnalité par année). Bien évidemment,
ici la chute observée en 2020 est faussée, puisqu’il s’agit de l’année de la 
**covid19**.
"""
    # Afficher le texte introductif
    st.write(text)


   # Générer le deuxième graphique "Evolution du nombre total de ventes par mois"
   # Définir la langue locale en français
    locale.setlocale(locale.LC_TIME, 'fr_FR')


    df_final_used['month'] = df_final_used['date_transaction'].dt.month

    # Calculer le nombre total de ventes pour chaque mois
    total_sales_by_month = df_final_used.groupby('month').size().reset_index(name='Total Ventes')

    # Trier le DataFrame par la colonne 'month'
    total_sales_by_month = total_sales_by_month.sort_values(by='month')

    # Obtenir les noms des mois en français
    month_names_fr = [month_name[i].capitalize() for i in total_sales_by_month['month']]

    # Tracer la courbe pour représenter l'évolution du nombre total de ventes par mois
    trace3 = go.Scatter(x=month_names_fr, y=total_sales_by_month['Total Ventes'], mode='lines', name='Nombre total de ventes par mois')

    # Créer la figure et ajoutez la trace
    fig3 = go.Figure(data=[trace3])

    # Mettre à jour la mise en page du graphique
    fig3.update_layout(title='Évolution du nombre total de ventes par mois', xaxis_title='Mois', yaxis_title='Nombre total de ventes')

    # Afficher le deuxième graphique dans Streamlit
    st.plotly_chart(fig3, use_container_width=True)


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

    # Calculer le nombre total de ventes pour chaque année et chaque arrondissement
    total_sales = df_final_used_GRAPH.groupby(['ville', 'annee']).size().reset_index(name='Nombre total de ventes')

    # Trier le DataFrame par la colonne 'annee'
    total_sales = total_sales.sort_values(by='annee')

    # Créer une trace pour chaque arrondissement
    traces = []
    for ville in total_sales['ville'].unique():
        data_ville = total_sales[total_sales['ville'] == ville]
        trace5 = go.Scatter(x=data_ville['annee'], y=data_ville['Nombre total de ventes'], mode='lines', name=ville)
        hover_text = [f'Ville: {ville}<br>Année: {annee}<br>Nombre total de ventes: {sales}' for annee, sales in zip(data_ville['annee'], data_ville['Nombre total de ventes'])]
        trace5.hovertemplate = '%{text}'
        trace5.text = hover_text
        traces.append(trace5)

    # Créer la figure et ajoutez les traces
    fig5 = go.Figure(data=traces)

    # Metter à jour la mise en page du graphique
    fig5.update_layout(title='Évolution du nombre total de ventes par arrondissement de Paris', xaxis_title='Année', yaxis_title='Nombre total de ventes')

    # Afficher le cinquième graphique dans Streamlit
    st.plotly_chart(fig5, use_container_width=True)

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

    # Calculer la moyenne du prix au m2 pour chaque année et chaque arrondissement
    mean_prices = df_final_used_GRAPH.groupby(['ville', 'annee'])['Prix m2'].mean().reset_index()

    # Trier le DataFrame par la colonne 'annee'
    mean_prices = mean_prices.sort_values(by='annee')

    # Créer une trace pour chaque arrondissement
    traces = []
    for ville in mean_prices['ville'].unique():
        data_ville = mean_prices[mean_prices['ville'] == ville]
        trace6 = go.Scatter(x=data_ville['annee'], y=data_ville['Prix m2'], mode='lines', name=ville)
        hover_text = [f'Ville: {ville}<br>Année: {annee}<br>Moyenne du prix au m2: {price:.2f}' for annee, price in zip(data_ville['annee'], data_ville['Prix m2'])]
        trace6.hovertemplate = '%{text}'
        trace6.text = hover_text
        traces.append(trace6)

    # Créer la figure et ajoutez les traces
    fig6 = go.Figure(data=traces)

    # Metter à jour la mise en page du graphique
    fig6.update_layout(title='Évolution de la moyenne du prix au m2 par arrondissement de Paris', xaxis_title='Année', yaxis_title='Moyenne du prix au m2')

    # Afficher le cinquième graphique dans Streamlit
    st.plotly_chart(fig6, use_container_width=True)

    introduction_text = """
Ici on constate une tendance à la **hausse des prix moyens au m2** dans paris 
intramuros, cela s’explique notamment par le fait que le marché soit tendu, avec 
**une demande croissante** et une **offre stable**.
"""
    # Afficher le texte introductif
    st.write(introduction_text)


    # Générer le cinquième graphique "Evolution du nombre total de ventes par mois et par arrondissement"
    # Ajoutez une nouvelle colonne 'month' pour extraire le mois à partir de la colonne 'date_transaction'
    df_final_used['month'] = df_final_used['date_transaction'].dt.month

    # Calculer le nombre total de ventes pour chaque mois et chaque arrondissement
    total_sales_by_month_and_arrondissement = df_final_used.groupby(['ville', 'month']).size().reset_index(name='Total Ventes')

    # Trier le DataFrame par la colonne 'month'
    total_sales_by_month_and_arrondissement = total_sales_by_month_and_arrondissement.sort_values(by='month')

    # Obtenir les noms des mois en français
    month_names_fr = [month_name[i].capitalize() for i in range(1, 13)]

    # Créer une liste de courbes pour chaque arrondissement
    traces = []
    for ville in total_sales_by_month_and_arrondissement['ville'].unique():
        data_ville = total_sales_by_month_and_arrondissement[total_sales_by_month_and_arrondissement['ville'] == ville]
        trace = go.Scatter(x=month_names_fr, y=data_ville['Total Ventes'], mode='lines', name=ville)
        hover_text = [f'Ville: {ville}<br>Mois: {month}<br>Total Ventes: {sales}' for month, sales in zip(month_names_fr, data_ville['Total Ventes'])]
        trace.hovertemplate = '%{text}'
        trace.text = hover_text
        traces.append(trace)

    # Créer la figure et ajoutez les courbes pour chaque arrondissement
    fig2 = go.Figure(data=traces)

    # Mettre à jour la mise en page du graphique
    fig2.update_layout(title='Évolution du nombre total de ventes par mois et par arrondissement de Paris', xaxis_title='Mois', yaxis_title='Nombre total de ventes')

    # Afficher le cinquième graphique dans Streamlit
    st.plotly_chart(fig2, use_container_width=True)

    introduction_text = """
Ici, on retrouve clairement le même **effet de saisonnalité** par mois au sein de 
l’année 2022 qu’au global avec les chutes au mois d’Aout et de Novembre.
"""
    # Afficher le texte introductif
    st.write(introduction_text)

    # Générer le sixième graphique "Evolution du prix au m2 par mois"
    fig = generate_price_chart(df_final_used)

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig, use_container_width=True)

    introduction_text = """
Ici, on observe que la période de l’année a un impact sur le prix de vente, 
puisqu’il peut exister selon les arrondissements des **variations significatives** du 
prix de vente au m2.
Il y a donc un impact du couple Offre/Demande sur le marché.
"""
    # Afficher le texte introductif
    st.write(introduction_text)
    

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
    def update_map(variable_name='prix'):
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



##Conclusion

# Chemin vers le fichier CSV
csv_file_path = "df_final_used.csv"

# Charger le fichier CSV dans un DataFrame
df_final_used = pd.read_csv(csv_file_path)

import streamlit as st
import pandas as pd
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

    conclusion_text = """
Pour les graphiques, on tient compte des revenus locatifs mais aussi de la plus-value potentielle liée à l’évolution des prix de l’immobilier. 
"""
    st.write(conclusion_text)


# Fonction afficher la page "Bonus"
def page_filtre():
    import streamlit as st
    st.title("Estimation de la rentabilité de votre projet")

    introduction_text = """
A présent, nous vous invitons à **réaliser une estimation de la rentabilité** de votre projet en fonction des critères de votre choix : emplacement du bien (arrondissement),
prix, nombre de pièces, surface ou encore loyer mensuel du bien. Vous aurez également l'occasion de rechercher un bien en fonction du **taux de rendement souhaité**.
"""
    st.write(introduction_text)

    import pandas as pd
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    csv_file_path = "df_streamlit.csv"

    data = pd.read_csv(csv_file_path)

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



import streamlit as st


# Fonction principale de l'application
# Create a layout with links to the two pages
st.sidebar.title("Navigation")
page_links = ["Machine Learning", "Vision France","Vision Paris","Carte vision Paris","Conclusion","Bonus"]
choice = st.sidebar.radio("Go to", page_links)


    # En fonction du choix de l'utilisateur, appelez la fonction correspondante
if choice == "Machine Learning":
    page_ML()
elif choice == "Vision France":
    page_France()
elif choice == "Vision Paris":
    page_Paris()
elif choice == "Carte vision Paris":
    page_map(df_final_used)
elif choice == "Conclusion":
    page_conclusion()
elif choice == "Bonus":
    page_filtre()


    # Afficher les informations des auteurs en bas de la barre latérale
    # st.sidebar.write("**Auteurs :**")
    # st.sidebar.write("Yen BUI")
    # st.sidebar.write("Thomas JOSSIER")
    # st.sidebar.write("Torkia DRIDER")
