class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque
        m = len(maze)
        n = len(maze[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        queue = deque()
        start_row,start_col = entrance

        queue.append((start_row,start_col,0))
        maze[start_row][start_col] = '+'
        
        while queue:
            row,col,steps = queue.popleft()
            for dr,dc in directions:
                nr = row +dr
                nc = col +dc

                if  0 <= nr < m and 0 <= nc < n:
                    if maze[nr][nc] == '.':

                        # Check whether it is an exit
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            return steps + 1

                        # Mark visited
                        maze[nr][nc] = '+'

                        # Add to queue
                        queue.append((nr, nc, steps + 1))

        return -1
        