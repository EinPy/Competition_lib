import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




class Graph:
    def __init__(self, adj, adj_rev):
        self.adj = adj
        self.adj_rev = adj_rev
        self.n = len(adj)
        self.used = [False] * self.n
        self.order = []
        self.component_cnt = 0
        self.components = []
        self.component = []
        self.roots = [0] * self.n
        self.root_nodes = []
        self.separate =  []
        self.adj_scc = [[] for _ in range(self.n)]

    def dfs1(self, v):
        self.used[v] = True
        for u in self.adj[v]:
            if not self.used[u]:
                self.dfs1(u)
        self.order.append(v)

    def dfs2(self, v):
        self.used[v] = True
        #self.component.append(v)
        for u in self.adj_rev[v]:
            if not self.used[u]:
                self.dfs2(u)

    def compute_sccs(self):
        for i in range(self.n):
            if not self.used[i]:
                self.dfs1(i)
                
        self.used = [False] * self.n
        rev_order = self.order[::-1]

        for i in range(self.n-1, -1, -1):
            v = self.order[i]
            if not self.used[v]:
                self.component_cnt += 1
                self.separate.append(v)
                self.dfs2(v)
                
                #self.components.append(self.component)
                # root = self.component[0]
                # for u in self.component:
                #     self.roots[u] = root
                # self.root_nodes.append(root)
                # self.component = []

    def build_reduction_graph(self):
        for v in range(self.n):
            for u in self.adj[v]:
                root_v = self.roots[v]
                root_u = self.roots[u]
                if root_u != root_v and root_u not in self.adj_scc[root_v]:
                    self.adj_scc[root_v].append(root_u)

        return self.adj_scc
            
            
n, m = nl()
adj = [[] for _ in range(n)]
adj_rev = [[] for _ in range(n)]
for _ in range(m):
    a, b = nl()
    adj[a-1].append(b-1)
    adj_rev[b-1].append(a-1)
    
T = Graph(adj, adj_rev)
T.compute_sccs()
#print(T.components)
if T.component_cnt == 1:
    print("YES")
else:
    print("NO")
    print(T.separate[1]+1, T.separate[0]+1)