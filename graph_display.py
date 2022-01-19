import networkx as nx
import matplotlib.pyplot as plt

def graph_display(adjacency_matrix, path, cost):

    # tworzenie grafu
    graph = nx.Graph()

    # iteracja po elementach powyżej przekątnej zer w tablicy sąsiedztwa
    # dodawanie ścieżek - węzłów i wag
    for node in range(len(adjacency_matrix)):
        for node_neighbour in range(node+1, len(adjacency_matrix)):
            graph.add_edge(node, node_neighbour, weight=adjacency_matrix[node][node_neighbour])

    # narysowanie grafu
    nx.draw(
        graph,
        pos=nx.circular_layout(graph),
        with_labels=True,
        font_color="white",
        node_size=300,
        node_color='black',
        edge_color='black'
    )

    #zaznaczenie początku i końca grafu
    nx.draw_networkx_nodes(graph, pos=nx.circular_layout(graph), nodelist=[path[0]], node_color="blue")
    nx.draw_networkx_nodes(graph, pos=nx.circular_layout(graph), nodelist=[path[-1]], node_color="red")

    #ustalenie koloru scieżki
    for node in path[:-1]:
        nx.draw_networkx_edges(
            graph,
            pos=nx.circular_layout(graph),
            edgelist=[(path[node], path[node+1])],
            edge_color="blue",
            arrows=True,
            arrowsize=25
        )

    # oznaczony powrót od końca do początku ścieżki
    nx.draw_networkx_edges(
        graph,
        pos=nx.circular_layout(graph),
        edgelist=[(path[-1], path[0])],
        edge_color="red",
        arrows=True,
        arrowsize=25
    )

    # etykiety krawędzi
    nx.draw_networkx_edge_labels(
        graph,
        pos=nx.circular_layout(graph),
        edge_labels=nx.get_edge_attributes(graph, 'weight'),
        rotate=False,
        font_size=10,
        font_color="black"
    )
    # fig.savefig('whatever.png', facecolor=fig.get_facecolor(), edgecolor='none')
    # ustalenia parametrów okna grafu
    fig = plt.gcf()
    fig.set_size_inches(8, 8)
    fig.canvas.manager.set_window_title('Graf')

    # ustalenie legendy (sciezka, koszt)
    path_text = ""
    for i in path[:-1]:
        path_text += str(i) + '->'
    path_text += str(path[-1])

    fig.text(
        0.025, 0.94,
        'sciezka: ' + path_text + '\n' + 'koszt: ' + str(cost),
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10}
    )

    # wyświetlenie grafu
    plt.show()
