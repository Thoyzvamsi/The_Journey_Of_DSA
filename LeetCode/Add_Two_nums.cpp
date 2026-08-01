#include <vector>
#include <iostream>
// Approach
// It is Brute force approuch , found complement for the target and looped for other number

// Complexity 

// Time complexity: O(logn)

// Space complexity: O(1)

// Code
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> arr;
        int comp = 0;
        for(int i = 0; i < nums.size(); i++){
            comp = target - nums[i];
            for(int j = i+1; j < nums.size(); j++){
                if (comp == nums[j]){
                    arr.push_back(i);
                    arr.push_back(j);
                    return arr;
                }
            }
        }
        return arr;
    }
};