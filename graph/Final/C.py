#https://contest.yandex.ru/contest/19438/run-report/47323173/
#Задача: C.Кондратиев остов
# Yайти вес максимального остовного дерева в неориентированном графе.

#-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(m * log n)
# Если учесть, что всего будет O(m) пересчётов указателей и O(n) поисков максимального ребра, то суммарная асимптотика составит O(m * log n)

#-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(n) - дополнительной памяти
 

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else :
            parent[yroot] = xroot
            rank[xroot] += 1
            
    def kruskal_mst(self):
        result =[]
  
        i = 0
        e = 0

        self.graph = sorted(self.graph,key=lambda item: item[2], reverse = True)
  
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V -1 :
            if i < len(self.graph):
                u,v,w = self.graph[i]
                i += 1
                x = self.find(parent, u)
                y = self.find(parent ,v)

                if x != y:
                    e += 1
                    result.append([u,v,w])
                    self.union(parent, rank, x, y)
            else:
                e += 1
              
        res = 0
        kol_n = set()
        kol_m = 0
        for u,v,weight in result:
            kol_n.add(u)
            kol_n.add(v)
            kol_m += 1
            res += weight
        if kol_m == len(kol_n) - 1:
            return res
        else:
            return 'Oops! I did it again'

def main():
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    g = Graph(n)
    for i in range(m):
        j = input().split()
        g.add_edge(int(j[0])-1, int(j[1])-1, int(j[2]))

    if n == 1:
        print(0)
    elif m>0:
        print(g.kruskal_mst())
    else:
        print('Oops! I did it again')

main()
