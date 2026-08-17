class Solution {
public:
    
    void dfs(int room, vector<vector<int>>& rooms, vector<bool>& visited) {
        visited[room] = true;

        for (int key : rooms[room]) {
            if (!visited[key]) {
                dfs(key, rooms, visited);
            }
        }
    }


    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();

        vector<bool> visited(n, false);

        // Start traversal from room 0
        dfs(0, rooms, visited);

        // Check whether every room was visited
        for (bool isVisited : visited) {
            if (!isVisited) {
                return false;
            }
        }

        return true;
    }
};