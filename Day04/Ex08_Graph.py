'''
그래프(Graph)
    노드(vertice)와 간서(정점/edge/arcs)로 이루어진 자료구조

'''
class Graph:
    '''
    self.vertices = ['A', 'B', 'C', 'D', 'E']
    adj_list = {
        'A' : [],
        'B' : [],
        'C' : [],
        'D' : [],
        'E' : []
    }
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for vertex in vertices:
            self.adj_list[vertex] = []
    '''
    graph.add_adge('A', 'B')
    graph.add_adge('A', 'C')
    graph.add_adge('B', 'D')
    graph.add_adge('C', 'E')
    '''
    def add_edge(self, u, v):
        '''
            adj_list = {
            'A' : [B, C],
            'B' : [A, D],
            'C' : [A, E],
            'D' : [B],
            'E' : [C]
        }  
        '''
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end=" -> ")
            print(" -> ".join([str(node) for node in self.adj_list[vertex]]))

vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')

graph.print_graph()