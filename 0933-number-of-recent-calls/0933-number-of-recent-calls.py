class RecentCounter:

    def __init__(self):
        self.queue = []
        self.front = 0
        

    def ping(self, t: int) -> int:

        self.queue.append(t)

        while self.queue[self.front] < t - 3000:
            self.front += 1
        return len(self.queue)-self.front
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)