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
if __name__ == "__main__":
    

    n = int(input())
    ai = int(input())
    m = int(input())
    pair = []
    for i in range(m):
        l = list(map(int, input().split(',')))
        pair.append(l)
    G = Graph()
    person = [i for i in range(n)]
    graph = G.makegraph(person)
    for m,n in pair:
        G.addedge(graph, m, n)
    def dfs(graph, s):
        stack = []
        stack.append(s)
        seen = set()
        seen.add(s)
        while stack:
            vertex = stack.pop()
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    stack.append(w)
                    seen.add(w)
        return seen
    seen = dfs(graph, ai)
    print(len(seen)-len(graph[ai])-1)