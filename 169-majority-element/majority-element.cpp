class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        for(int num : nums){
            int frequency = 0;
            for(int ele : nums){
                if(ele == num){
                    frequency++;
                }
            }
            if(frequency > n/2){
                return num;
            }
        }
        return -1;
    }
};