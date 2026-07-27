class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int la = 0, sl = 0;
        for (int num : nums){
            if (num > la){
                sl = la;
                la = num;
            }
            else if(num > sl){
                sl = num;
            }
        }
        return (la - 1)*(sl-1);
        
    }
};