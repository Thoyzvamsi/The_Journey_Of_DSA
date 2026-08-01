#include <iostream>
#include <vector>
#include <algorithm>

// Approach
// Linear approuch , sorting the array based on first element then,
// Check the last is greater to the next first element

// Complexity 

// Time complexity: O(n)

// Space complexity: O(1)

// Code

using std::vector;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> results;
        std::sort(intervals.begin(), intervals.end()); //sorts based on first element

        for(auto interval : intervals){
            if (results.empty() || results.back()[1] < interval[0]){
                results.push_back(interval);
            } else {
                results.back()[1] = std::max(results.back()[1] ,interval[1]);
            }
        }
        return results;
    }
};