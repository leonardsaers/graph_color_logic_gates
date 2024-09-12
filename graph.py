import networkx as nx
import matplotlib.pyplot as plt

class GraphBuilder:
    def __init__(self):
        self.graph = nx.Graph()
        self.graph.add_node("N", color='yellow')
        self.graph.add_node("F", color='red')
        self.graph.add_node("T", color='green')
        self.add_edge("N", "F")
        self.add_edge("N", "T")
        self.add_edge("T", "F")

    # Adds an or gate (using 9 edges and 7 nodes)
    def add_or(self, id, input1, input2, output):
        self.add_node(id + "_1")
        self.add_node(id + "_2")
        self.add_node(id + "_3")
        self.add_node(id + "_4")
        self.add_node(input1)
        self.add_node(input2)
        self.add_node(output)
        self.add_edge("N", input1)
        self.add_edge("N", input2)
        self.add_edge("N", output)
        self.add_edge("T", id + "_2")
        self.add_edge(input1, id + "_1")
        self.add_edge(input2, id + "_1")
        self.add_edge(id + "_1", id + "_2")
        self.add_edge(input1, id + "_3")
        self.add_edge(input2, id + "_4")
        self.add_edge(id + "_3", id + "_4")
        self.add_edge(id + "_3", output)
        self.add_edge(id + "_4", output)
        self.add_edge(id + "_2", output)
        return self

    def add_not(self, input, output):
        self.add_node(input)
        self.add_node(output)
        self.add_edge(input, output)
        self.add_edge("N", input)
        self.add_edge("N", output)
        return self

    def add_and(self, id, input1, input2, output):
        self.add_not(input1, id + "_and1")
        self.add_not(input2, id + "_and2")
        self.add_or(id,id+"_and1", id + "_and2", id + "_and3")
        self.add_not(id + "_and3", output)
        return self

    def add_exor(self, id, input1, input2, output):
        self.add_not(input1, id + "_exor1")
        self.add_not(input2, id + "_exor2")
        self.add_and(id + "a1",input1, id + "_exor2", id + "_exor3")
        self.add_and(id + "a2",input2, id + "_exor1", id + "_exor4")
        self.add_or(id,id + "_exor3", id + "_exor4", output)
        return self

    def add_input(self, node, color='gray'):
        self.graph.add_node(node, color=color)
        self.add_edge("N", node)
        return self

    def add_node(self, node, color='gray'):
        self.graph.add_node(node, color=color)
        return self
    
    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)
        return self
    
    def build(self):
        return self.graph

def color_graph(graph):
    colors = nx.coloring.greedy_color(graph, strategy="independent_set")
    in1 = "0" if colors["in1"] == colors["F"] else "1"
    in2 = "0" if colors["in2"] == colors["F"] else "1"
    out = "0" if colors["in1_OR_in2"] == colors["F"] else "1"
    print(f"{in1} | {in2} | {out}")
    return colors

def show_graph(graph, colors):
    nx.set_node_attributes(graph, colors, "color")

    node_colors = [nx.get_node_attributes(graph, 'color')[node] for node in graph.nodes()]

    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=1000, font_size=15, font_color='black')
    plt.show()

g_or_00 = (GraphBuilder()
         .add_input("in1")
         .add_input("in2")
         .add_or("a1","in1","in2","in1_OR_in2")
         .add_edge("T","in1")
         .add_edge("T","in2")
         .build())

g_or_01 = (GraphBuilder()
         .add_input("in1")
         .add_input("in2")
         .add_or("a1","in1","in2","in1_OR_in2")
         .add_edge("T","in1")
         .add_edge("F","in2")
         .build())

g_or_10 = (GraphBuilder()
         .add_input("in1")
         .add_input("in2")
         .add_or("a1","in1","in2","in1_OR_in2")
         .add_edge("F","in1")
         .add_edge("T","in2")
         .build())

g_or_11 = (GraphBuilder()
         .add_input("in1")
         .add_input("in2")
         .add_or("a1","in1","in2","in1_OR_in2")
         .add_edge("F","in1")
         .add_edge("F","in2")
         .build())


c = color_graph(g_or_00)
color_graph(g_or_01)
color_graph(g_or_10)
color_graph(g_or_11)

# show_graph(g_or_00, c)
