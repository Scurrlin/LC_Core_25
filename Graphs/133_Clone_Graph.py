class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        newGraph = {}

        def dfs(node):
            if node in newGraph:
                return newGraph[node]

            copy = Node(node.val)
            newGraph[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else None