#include <vector>
#include <algorithm>
#include <iostream>

using std::vector;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> result;
        int n = nums.size();
        int sum;

        for(int i = 0; i < n-2; i++){
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            int j = i+1 ,k = n-1;
            while(j < k){
                sum = nums[i] + nums[j] + nums[k];

                if(sum == 0){
                    result.push_back({nums[i] ,nums[j] ,nums[k]});
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j -1])
                        j++;
                } else if(sum < 0){
                    j++;
                } else {
                    k--;
                }
            }
        }
        return result;
    }
};