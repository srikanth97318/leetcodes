class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        weights = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            weights.append(w)

        # Remove duplicate weights
        weights = sorted(set(weights))

        # Kahn's Topological Sort without deque
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        front = 0

        while front < len(queue):
            node = queue[front]
            front += 1
            topo.append(node)

            for nei, _ in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        INF = float("inf")

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # Intermediate node must be online
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    if v != 0 and v != n - 1 and not online[v]:
                        continue

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        left = 0
        right = len(weights) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(weights[mid]):
                ans = weights[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans