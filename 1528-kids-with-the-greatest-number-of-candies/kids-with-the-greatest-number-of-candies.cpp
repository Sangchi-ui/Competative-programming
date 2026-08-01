class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> max_can;
        int n = candies.size();
        int max_candie = *max_element(candies.begin(), candies.end());
        for(int i = 0; i < n; i++){
            if (candies[i]+extraCandies >= max_candie){
                max_can.push_back(true);
            }
            else{
                max_can.push_back(false);
            }
        }
        return max_can;
    }
};