class Solution {
private:
    void dfs(int c, const vector<vector<int>>& isConnected,vector<bool>& visited){
        visited[c] = true;
        for (int n = 0; n < isConnected.size(); ++n){
            if(isConnected[c][n] == 1 && !visited[n]){
                dfs(n, isConnected, visited);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        const int n = isConnected.size();
        vector<bool> visited(n, false);

        int count = 0;
        for (int i = 0; i < n; ++i){
            if(!visited[i]){ 
                ++count;
                dfs(i,isConnected, visited);
            }
        }

        return count;
        
    }
};