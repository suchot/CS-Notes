import heapq
class Graph():
    def __init__(self):
        self.graph = dict()
    def  makegraph(self, l, graph=dict()):
        for i in l:
            graph.setdefault(i, [])  
        return graph
    def addedge(self, graph, a, b):
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)
    def makedgraph(self, l , graph = dict()):
        for i in l:
            graph.setdefault(i, dict())  
        return graph
    def adddedge(self, graph, a, b, weight=1):
        if b not in graph[a]:
            graph[a][b]=weight
        if a not in graph[b]:
            graph[b][a]=weight
if __name__ == "__main__":
    n = 4
    G = Graph()
    l = [chr(i) for i in range(65, 71)]
    graph = G.makedgraph(l)
    G.adddedge(graph, 'A','B', 5)
    G.adddedge(graph, 'A','C', 1)
    G.adddedge(graph, 'B','C', 2)
    G.adddedge(graph, 'B','D', 1)
    G.adddedge(graph, 'E','D', 3)
    G.adddedge(graph, 'F','D', 6)
    G.adddedge(graph, 'C','D', 4)
    G.adddedge(graph, 'C','E', 8)

    def bfs(graph, s):
        queue = []
        queue.append(s)
        seen = set()
        seen.add(s)
        parent = {s:None}
        while queue:
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
                    parent[w]= vertex
            print(vertex)
        return parent

    def dfs(graph, s):
        stack = []
        stack.append(s)
        seen = set()
        seen.add(s)
        parent = {s:None}
        while stack:
            vertex = stack.pop()
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    stack.append(w)
                    seen.add(w)
                    parent[w]= vertex
            print(vertex)
        return parent
    def init_distance(graph, s):
        distance = {s:None}
        for vertex in graph.keys():
            if vertex != s:
                distance[vertex]=float('inf')
        return distance

    def dijkstra(graph, s):
        pqueue = []
        heapq.heappush(pqueue, (0,s))
        seen = set()
        parents = {s:None}
        distance = init_distance(graph, s)
        while pqueue:
            pair = heapq.heappop(pqueue)
            dist = pair[0]
            vertex = pair[1]
            seen.add(vertex)
            nodes =graph[vertex].keys()
            for w in nodes:
                if w not in seen:
                    if dist+graph[vertex][w]<distance[w]:
                        heapq.heappush(pqueue, (dist+graph[vertex][w], w))
                        distance[w] = dist+graph[vertex][w]
                        parents[w] = vertex

        return parents, distance

    parents, distance = dijkstra(graph, 'A')
    print(parents, distance)

    parents = bfs(graph, 'E')
    print('========\n')
    dfs(graph, 'E')
    for key in parents:
        print(key, parents[key])
    v = 'B'
    while  v !=None:
        print(v)
        v = parents[v]
