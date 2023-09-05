import streamlit as st
import pandas as pd
import plotly.express as px
# from streamlit.components.v1 import components

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

    # Display the Plotly graph using an IFrame
    st.write("Plotly Graph on Page 1:")
    
    # Provide the path to the local HTML file (assuming it's in the same directory)
    # local_html_path = "plotly_graph.html"
    
    # Use the components function to embed the HTML content
    st.components.v1.html(open("plotly_graph.html", 'r').read(), width=1000, height=600, scrolling=True)
    # Générer le premier graphique "Evolution du nombre total de ventes par année"

    # Use the components function to embed the HTML content
    st.components.v1.html(open("Evolution_nombre_ventes_par_annee_France_Plotly.html", 'r').read(), width=1000, height=600, scrolling=True)


    text = """
    Ici, on identifie clairement une **incidence de l’évolution** des cycles économiques 
sur le marché de l’immobilier (effet de saisonnalité par année). Bien évidemment,
ici la chute observée en 2020 est faussée, puisqu’il s’agit de l’année de la 
**covid19**.
"""
    # Afficher le texte introductif
    st.write(text)


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

    
def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

# Create a navigation menu
pages = {
    "Page 1": page1,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()
