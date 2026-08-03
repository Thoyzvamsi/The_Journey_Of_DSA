#include <vector>

// Container with most water

// Approach
// arrage two pointers to the front and back move the smaller element pointer
// area = min(height[left],height[right]) * (right-left)

// Complexity
// Time complexity:
// O(n)

// Space complexity:
// O(1)

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int max_water = 0;
        int current_area = 0;
        int left = 0;
        int right = height.size() - 1;

        while(left < right){
            current_area = std::min(height[left],height[right]) * (right-left);
            if (max_water < current_area){
                max_water = current_area;
            }
            if (height[left] < height[right]){
                left++;
            } else {
                right--;
            }
        }
        return max_water;
    }
};