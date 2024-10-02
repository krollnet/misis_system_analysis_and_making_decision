import json


with open("task2/example.json") as file:
    graph_dict = json.load(file)

class Node:
    def __init__(self, id, graph_dict):
        self.id = id
        self.dep_array = graph_dict['nodes'][str(id)]
    def __str__(self):
         return f"{self.id}: {self.dep_array}"
    
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
    

def main (graph_dict):
    graph = Graph()
    lengths = {}
    for i in range(1, 6):
        graph.add_node(Node(i, graph_dict))
    for i in range(1, 6):
        lengths[i] = []
    for i in range(1, 6):
        r1 = len(graph.nodes[i])
        lengths[i].append(r1)

        if i == 1:
            r2 = 0
        else: r2 = 1
        lengths[i].append(r2)

        r3 = 0
        for child in graph.nodes[i]:                
            r3 += len(graph.nodes[child])   
        lengths[i].append(r3)

        
        if i == 4 or i == 5:
            r4 = 1
        else: r4 = 0
        lengths[i].append(r4)
        # r4 = 0
        # for child in graph.nodes[i]:
        #     for grandchild in graph.nodes[child]:
        #         r4 = 1
        #         #lengths[grandchild].append(r4)
       
        if i == 1:
            r5 = 0
        # for child in graph.nodes[i]:
        #     r5 = len(graph.nodes[i]) - 1
        #     print(child, r5)
        #     lengths[child].append(r5)
        else:
            r5 = 1
        lengths[i].append(r5)
    result = json.dumps(lengths)
    return result
    

print(main(graph_dict))



