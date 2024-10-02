# задание: распарсить Json строку в однин из форматов представления дерева (формат выбрать самим из тех, что написаны на доске)
# и вернуть в виде этой структры, загрузить на репозиторий 
# структура репозитория папка task1 и в ней файл task1.py

#выбрано представление массивы смежности (список связей)


import json 


with open('example.json') as file:
    graph_dict = json.load(file)


class Node:
    def __init__(self, id, graph_dict):
        self.id = id
        self.dep_array = graph_dict['nodes'][str(id)]
    def __str__(self):
         return f"{self.id}: {self.dep_array}"
     
# node_2 = Node(2, graph_dict)
# node_3 = Node(3, graph_dict)
# print(node_2)


class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node.id] = node.dep_array
    def __str__(self):
        output = ''
        for node_id, dependencies in self.nodes.items():
            output += f"Node {node_id}: {dependencies}\n"
        return output  

# graph = Graph()
# graph.add_node(node_2)
# graph.add_node(node_3)
# print(graph.nodes)
# print(graph)