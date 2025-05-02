import networkx as nx
import matplotlib.pyplot as plt

def odczytaj_liste_sasiedztwa(sciezka_pliku):
    grafy = []
    biezacy_graf = {}

    with open(sciezka_pliku, 'r') as plik:
        for linia in plik:
            linia = linia.strip()
            if not linia or linia.startswith("#"):  # Pusta linia lub komentarz
                if biezacy_graf:
                    grafy.append(biezacy_graf)
                    biezacy_graf = {}
                continue
            
            wierzcholek, sasiedzi = linia.split(":")
            wierzcholek = wierzcholek.strip()
            sasiedzi = sasiedzi.strip().split()
            biezacy_graf[wierzcholek] = sasiedzi
        
        if biezacy_graf:
            grafy.append(biezacy_graf)
    
    return grafy

def rysuj_grafy(grafy):
    liczba_grafow = len(grafy)
    kolumny = 2  # Liczba kolumn na rysunku
    wiersze = (liczba_grafow + kolumny - 1) // kolumny  # Wyliczenie liczby wierszy
    
    fig, osie = plt.subplots(wiersze, kolumny, figsize=(12, 6))
    osie = osie.flatten()  # Spłaszczenie tablicy, aby łatwo iterować
    
    for i, lista_sasiedztwa in enumerate(grafy):
        G = nx.Graph()
        for wierzcholek, sasiedzi in lista_sasiedztwa.items():
            for sasiad in sasiedzi:
                G.add_edge(wierzcholek, sasiad)
        
        nx.draw(G, ax=osie[i], with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
        osie[i].set_title(f"Graf {i + 1}")
    
    for j in range(i + 1, len(osie)):
        osie[j].axis('off')
    
    plt.tight_layout()
    plt.show()

sciezka_pliku = "grafy.txt"

grafy = odczytaj_liste_sasiedztwa(sciezka_pliku)
rysuj_grafy(grafy)
