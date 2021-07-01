#тут ссылка
#Звдача B. Путь по компонентам
#В графе нашли компоненты реберной двусвязности, сжали их и получили одно или несколько деревьев. У каждой вершины сжатого графа тоже есть вес, который равен сумме весов исходной компоненты реберной двусвязности. В полученном графе найдите самый длинный путь, на котором веса вершин идут строго по возрастанию.

#-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  Операции, добавленные к алгоритму обхода в глубину, работают за константное время. То есть сложность будет такая же, как у dfs — O(∣V∣+∣E∣).

#-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(n) 
 

from collections import defaultdict

def dfs(graph, start, bridges):
  visited = set()
  stack = [start]
  while stack:
    curr = stack.pop()
    if curr in visited:
      continue
    yield curr
    visited.add(curr)
    for neighbor in graph[curr]:
      if hash((curr,neighbor)) in bridges or hash((neighbor,curr)) in bridges:
        continue
      if neighbor not in visited:
        stack.append(neighbor)

class Graph:
  def __init__(self, vertices, weights):
    self.V = vertices + 1
    self.weights = weights
    self.adj_list = defaultdict(list)
    self.adj_list_not_bridges = defaultdict(list)
    self.parent = [-1] * self.V
    self.low = [float('inf')] * self.V
    self.disc = [float('inf')] * self.V
    self.visited = [False] * self.V
    self.time = 0
    self.bridges = {}

  def add_edge(self, v, u):
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)

  def find_bridges(self, u):
    self.visited[u] = True
    self.low[u] = self.time
    self.disc[u] = self.time
    self.time += 1

    for v in self.adj_list[u]:
      if not self.visited[v]:
        self.parent[v] = u
        self.find_bridges(v)
        self.low[u] = min(self.low[u], self.low[v])
        if self.low[v] > self.disc[u]:
          self.bridges[hash((u, v))] = (u, v)

      elif v != self.parent[u]:
        self.low[u] = min(self.low[u], self.disc[v])
  
  def weights_component(self, component):
    sums_component = []
    for i in component:
      sums = 0
      for j in i:
        sums += self.weights[j]
      sums_component.append(sums)
    return sums_component



inp = input().split()
n = int(inp[0])
m = int(inp[1])
j = [0] + [int(i) for i in input().split()]
g = Graph(n,j)
for i in range(m):
  j = input().split()
  g.add_edge(int(j[0]), int(j[1]))

for j in range(1, g.V):
  if not g.visited[j]:
    g.find_bridges(j)

print(g.bridges)
color = [-1 for i in range(n+1)]
color[0] = -2
component_count = 1
components = []
for i in range(1,len(color)):
  if color[i] != -1:
    continue
  l = []
  d = list(dfs(g.adj_list,i,g.bridges))
  for j in d:
    if color[j] == -1:
      l.append(j)
      color[j] = component_count
  components.append(l)
  component_count += 1
res = g.weights_component(components)
res.sort()
for i in res:
  print(i, end=' ')
print()
for i in g.bridges.items():
  print(i)
