#include<vector>
// Product of array except itself

// Approach
// prefix product and suffix products

// Complexity
// Time complexity:
// O(n)

// Space complexity:
// O(1)

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> arr(n);
        arr[0] = 1;

        for(int i = 1; i < n; i++){
            arr[i] = arr[i-1]*nums[i-1];
        }

        int r = 1;
        for(int i = n-1; i >= 0; i--){
            arr[i] *= r;
            r *= nums[i];
        }
        return arr;
    }
};