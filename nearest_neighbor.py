def nearest_neighbor_search(neighbor_matrix):
    # zmienne na najlepszą ścieżkę
    najlepszy_koszt = 0
    najlepsza_trasa = []
    # wybrane parametry grafu
    ile_wierzcholkow = len(neighbor_matrix)
    max_krawedz = (max(neighbor_matrix))[0] + 1

    # powtórz algorytm dla każdego wierzchołka startowego
    for i in range(ile_wierzcholkow):
        # resetuj zmienne tymczasowe
        obecny_koszt = 0
        obecna_trasa = []
        obecny_wierzcholek = i
        # lista pamiętająca odwiedzone wierzchołki
        odwiedzone = [False] * ile_wierzcholkow

        # dodaj wierchołek startowy do obecnej trasy i oznacz go jako odwiedzony
        obecna_trasa = [i]
        odwiedzone[i] = True

        # dopóki nie wszystkie wierzchołki zostały odwiedzone
        while len(obecna_trasa) < ile_wierzcholkow:
            # znajdź najbliższego nieodwiedzonego sąsiada obecnego wierzchołka
            min_koszt = max_krawedz + 1
            najblizszy_wierzcholek = obecny_wierzcholek
            for u in range(ile_wierzcholkow):
                if odwiedzone[u] is False and neighbor_matrix[obecny_wierzcholek][u] < min_koszt:
                    min_koszt = neighbor_matrix[obecny_wierzcholek][u]
                    najblizszy_wierzcholek = u

            # dodaj sąsiada i zaktualizuj trasę
            obecny_koszt = obecny_koszt + min_koszt
            obecna_trasa = obecna_trasa + [najblizszy_wierzcholek]
            odwiedzone[najblizszy_wierzcholek] = True
            obecny_wierzcholek = najblizszy_wierzcholek

        # sprawdź czy nowo znaleziona trasa jest najlepsza
        if i != 0:
            if obecny_koszt < najlepszy_koszt:
                najlepszy_koszt = obecny_koszt
                najlepsza_trasa = obecna_trasa
        else:
            najlepsza_trasa = obecna_trasa
            najlepszy_koszt = obecny_koszt

    return najlepsza_trasa, najlepszy_koszt
