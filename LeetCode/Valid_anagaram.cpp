#include <unordered_map>
#include <iostream>

// Valid anagaram

// Approach
// count how many unique elements with hash map and compare them

// Complexity
// Time complexity:
// O(n)

// Space complexity:
// O(1)

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) return false;

        std::unordered_map<char,int> counter;
        for (char ch: s){
            counter[ch]  = counter[ch]+1;
        }

        for (char ch: t){
            if (counter.find(ch) == counter.end() || counter[ch] == 0) return false;
            counter[ch] --;
        }
        return true;
    }
};