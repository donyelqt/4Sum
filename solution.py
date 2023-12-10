#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        if(n < 4) {
            return {};
        }
        
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        
        for(int i = 0; i < n - 3; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            for(int j = i + 1; j < n - 2; j++) {
                if(j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                
                long long sum = static_cast<long long>(nums[i]) + nums[j] - target;
                
                int left = j + 1;
                int right = n - 1;
                
                while(left < right) {
                    if(nums[left] + nums[right] == -sum) {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        right--;
                        
                        while(left < right && nums[left] == nums[left - 1]) {
                            left++;
                        }
                        
                        while(left < right && nums[right] == nums[right + 1]) {
                            right--;
                        }
                    } else if(nums[left] + nums[right] < -sum) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        
        return res;
    }
};
