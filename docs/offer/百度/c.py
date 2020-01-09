# 题目描述：
# 给定一个点数为N的树，即包含N个点和N-1条边的无向连通图，每条边有各自的长度，那么树上距离最近的两个叶子之间的距离是多少？叶子即度数为1的点，一个点的度数是以其为端点的边的数量，两个点之间的距离是它们之间的简单路径上边的长度之和。

# 输入
# 第一行输入一个整数N，1≤N≤10^5

# 接下来N-1行，每行输入三个整数x、y和l，1≤x，y≤N，1≤l≤10^9，表示第x个点和第y个点之间有一条长度为l的边。

# 输出
# 输出距离最近的两个叶子之间的距离


# 样例输入
# 5
# 1 2 1
# 1 3 1
# 3 4 3
# 3 5 1
# 样例输出
# 3

# 提示
# 第2个点和第5个点是距离最近的两个叶子。





import heapq
class Graph():
    def __init__(self):
        self.graph = dict()
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
    n = int(input())
    G = Graph()
    l = [str(i) for i in range(1,6)]
    graph = G.makedgraph(l)
    for i in range(n-1):
        x,y,weight = map(int, input().split())
        G.adddedge(graph, str(x), str(y), weight)
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

        return  distance
    res = float('inf')
    temp = float('inf')
    leaf = []
    for node in l:
        if len(graph[node])==1:
            leaf.append(node)
    for node in leaf:
        dis = dijkstra(graph, node)
        for other_leaf in leaf:
            if not dis[other_leaf]:
                continue
            temp = dis[other_leaf]
            res = min(res, temp)
    print(res)            

    
