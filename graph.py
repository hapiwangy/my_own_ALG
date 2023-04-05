class Dijkstra:
    def __init__(self, graph) -> None:
        #  {"start":{"b":10}, "b":{"c":20}, "c":{"d":1, "finish":30}, "d":{"b":1}, "finish":{}}
        # 定義圖
        self.graph = graph
        self.current_cost = {x:float("inf") for x in graph.keys() if x != "start"}
        self.parent = {x:"start" for x in graph['start'].keys()}
        self.parent['finish'] = None
        self.process = []
        self.set_current_cost()

    def set_current_cost(self):
        # 把start裡面的東西放到current_cost
        for x, y in self.graph["start"].items():
            self.current_cost[x] = y

    # 進行演算
    def find_lowest_cost_node(self, costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.process: # 如果是最小成本且尚未處裡過
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    # dijkstra
    def dijkstra_main(self):
        # 找成本最低的
        node = self.find_lowest_cost_node(self.current_cost)
        # 要對每個點都進行處理
        while node is not None:
            # 查看最小的點的附近所有節點
            cost = self.current_cost[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.current_cost[n] >  new_cost:
                    self.current_cost[n] = new_cost # 更新成本
                    self.parent[n] = node # 放到父節點裡面
            self.process.append(node)
            node = self.find_lowest_cost_node(self.current_cost)
    # 回傳結果
    def solve_dijkstra(self):
        self.dijkstra_main()
        now = "finish"
        path = []
        while True:
            path.append(now)
            if now == "start":
                break
            now = self.parent[now] 
        path.reverse()
        path = " -> ".join(path)
        return f"各點的最低成本為{self.current_cost}\n路徑為{path}"

graph = Dijkstra({"start":{"b":10}, "b":{"c":20}, "c":{"d":1, "finish":30}, "d":{"b":1}, "finish":{}})
print(graph.solve_dijkstra())