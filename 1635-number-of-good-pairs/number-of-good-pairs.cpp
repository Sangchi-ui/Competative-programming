class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int i = 0;
        int gud_pairs = 0;
        int n = nums.size();
        while(i < n){
            int j = i + 1;
            while(j < n){
                if(nums[i] == nums[j]){
                    gud_pairs = gud_pairs + 1;
                }
                j++;
            }
            i++;
        }
        return gud_pairs;
    }
};