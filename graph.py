import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv


# Метод визуализации графа
def draw_graph(edges: list, point_positions: dict, image_filename: str) -> None:
    G = nx.from_edgelist(edges, create_using=nx.MultiDiGraph())
    nx.draw_networkx(
        G,
        pos=point_positions,
        with_labels=True,
        arrows=True,
        font_family="JetBrains Mono",
        arrowstyle="-",
        node_size=30,
        node_color="orange",
        edge_color="gray",
        width=1,
        arrowsize=20,
        alpha=0.85,
    )  # Стилизация визуализации
    plt.savefig(image_filename, dpi=600)  # Сохранение изображения
    plt.close("all")  # Очистка модели


# Метод считывающий данные с csv файла
def read_and_parse_csv(csv_filename: str) -> tuple[list, dict]:
    with open(csv_filename, "r") as file:
        rows = [row for row in csv.reader(file)]
    return rows


# Метод возвращающий вершины
def parse_points(rows: list) -> list:
    points = []
    for edge in rows[2:rows.index(["positions"])]:
        points.append(edge[0].capitalize())
        points.append(edge[1].capitalize())
    return points


# Метод возвращающий пути
def parse_edges(rows: list) -> list:
    points = []
    for edge in rows[2 : rows.index(["positions"])]:
        points.append((edge[0].capitalize(), edge[1].capitalize()))
    return points


# Метод возвращающий позиции вершин в формате (x, y)
def parse_point_positions(rows: list) -> dict:
    point_positions = {}
    for point in rows[rows.index(["positions"]) + 2:]:
        point_positions[point[0].capitalize()] = np.array(
            (float(point[1]), float(point[2]))
        )
    return point_positions


# Метод нахождения избыточных вершин (возможно добавление новых условий)
def point_to_delete(points: list) -> list:
    return [point for point in points if points.count(point) == 2]


# Метод оптимизации графа
def alghoritm(edges: list, to_delete: list) -> list:
    newedges = set()
    for edge in edges:
        if copy_ := set(edge) & set(to_delete):
            point1 = copy_ ^ set(edge)
            newedges.add(list(point1)[0])
    edges.append(tuple(newedges))
    for edge in edges:
        if set(edge) & set(to_delete):
            edges.remove(edge)
    return edges


# Метод для отображения исходного графа
def without_algorithm(csv_filename: str, image_filename: str):
    rows = read_and_parse_csv(csv_filename)
    edges = parse_edges(rows)
    point_positions = parse_point_positions(rows)
    draw_graph(edges, point_positions, image_filename)


# Метод для отображения оптимизированного графа
def with_algorithm(csv_filename: str, image_filename: str):
    rows = read_and_parse_csv(csv_filename)
    edges = alghoritm(parse_edges(rows), point_to_delete(parse_points(rows)))
    point_positions = parse_point_positions(rows)
    draw_graph(edges, point_positions, image_filename)
