#include <iostream>
#include <vector>
#include <algorithm>
// Longest Sub string in a string

// Approach
// check char already exits in checked remove element from front

// Complexity
// Time complexity:
// O(nlogn) Maybe....

// Space complexity:
// O(1) Maybe.....


class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::vector<char> checked;
        int max_len = 0;

        for (int i = 0; i < s.length(); i++){
            // check char already exits in checked remove element from front
            while (std::find(checked.begin(), checked.end(), s[i]) != checked.end()) {
                checked.erase(checked.begin());
            }
            checked.push_back(s[i]);
            max_len = std::max(max_len, (int)checked.size());
        }
        return max_len;
    }
};