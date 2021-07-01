#https://contest.yandex.ru/contest/19438/run-report/47322642/
#Звдача A. Железные дороги
# нужно исследовать все дороги и понять есть ли хотябы одна точка до которой можно добраться проходя через два типа дорог, если да, то дороги не оптимальные
#Если всего один тип дороги есть - то оптимальные

#-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Для ориентированного графа сумма длин списков смежности для всех вершин равна количеству рёбер в графе, то есть ∣E∣. По каждому ребру пройдём один раз. Получим, что сложность O(∣V∣+∣E∣).
# плюс DFS - поиск цикла O(n)

#-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(n) - дополнительной памяти
 

class Graph:

    def __init__(self, way, vertices):
        self.WHITE = 0
        self.GREY = 1
        self.BLACK = 2
        self.V = vertices
        self.way_r_b = self.build_way(way)

    def build_way(self, way):
        ret = [[] for i in range(self.V + 1)]
        first_type = None

        while way:
            vertices = len(way)
            to_vertices = way.pop()

            for in_vertices, way_type in enumerate(to_vertices, 1):
                destination = vertices + in_vertices

                if first_type is None:
                    first_type = way_type

                if way_type == first_type:
                    ret[vertices].append(destination)
                else:
                    ret[destination].append(vertices)

        return ret

    def get_neighbors(self, city):
        try:
            ret = self.way_r_b[city]
        except IndexError:
            ret = ()

        return ret
        
    def dfs(self):

        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [range(len(self.way_r_b))]
        while stack:
            for curr_city in stack[-1]:
                if curr_city in path_set:
                    return False
                elif curr_city not in visited:
                    visited.add(curr_city)
                    path.append(curr_city)
                    path_set.add(curr_city)
                    stack.append(iter(self.get_neighbors(curr_city)))
                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return True
        

def main():
    n = int(input())
    mas = [list(input()) for _ in range(n - 1)]
    g = Graph(mas, n)
    if g.dfs():
      print("YES")
    else:
      print("NO")

main()

