from data import example_data as example
import nearest_neighbor as nn
import graph_display as gd



if __name__ == '__main__':
    # wygeneruj macierz sąsiedztwa grafu
    graf = example.data_generator.przyklad_prezka

    # uruchom algorytm najbliższego sąsiada
    trasa_najblizszy_sasiad, koszt_najblizszy_sasiad = nn.nearest_neighbor_search(graf)

    # wydrukuj wyniki algorytmu najbliższego sąsiada
    # print('Najlepsza ścieżka wg. algorytmu najbliższego sąsiada:')
    print(trasa_najblizszy_sasiad)
    # print('Całkowity koszt ścieżki: ', koszt_najblizszy_sasiad)
    gd.graph_display(graf, trasa_najblizszy_sasiad, koszt_najblizszy_sasiad)
